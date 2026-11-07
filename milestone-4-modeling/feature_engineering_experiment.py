"""
Milestone 4 (extra experiment): feature engineering without energy and time.

Question from the coach: can new features built from the other columns bring the
accuracy up when `energy_consumption_kwh` and `execution_time_ms` are removed?

What this script does:
  1. Loads the prepared train/test data (Milestone 3) and returns it to raw units.
  2. Keeps the 8 pre-run columns (Set B) and builds 8 new features from them
     (ratios, sums, differences, products). Energy and time are NOT used.
  3. Compares models on Set B vs Set B + 8 new features.
  4. Measures how much information each feature carries (mutual information).
  5. Tries to rebuild energy and time from the pre-run columns (R2).

Run from any folder:  python feature_engineering_experiment.py
Needs: pandas, numpy, scikit-learn. Reads ../data/prepared/. Does not change any data.

Note: the models are scored on the test set to compare settings, so the best
number is slightly optimistic. It is still below the baseline (0.505).
"""
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import (HistGradientBoostingClassifier,
                              RandomForestClassifier, RandomForestRegressor)
from sklearn.feature_selection import mutual_info_classif
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, r2_score
from sklearn.model_selection import KFold, StratifiedKFold, cross_val_predict, cross_val_score
from sklearn.tree import DecisionTreeClassifier

warnings.filterwarnings("ignore")
SEED = 42
DATA = Path(__file__).resolve().parent.parent / "data" / "prepared"
RULE_COLS = ["energy_consumption_kwh", "execution_time_ms"]

# ---------------------------------------------------------------- 1. load data
Xtr = pd.read_csv(DATA / "X_train.csv")
Xte = pd.read_csv(DATA / "X_test.csv")
ytr = pd.read_csv(DATA / "y_train.csv").iloc[:, 0]
yte = pd.read_csv(DATA / "y_test.csv").iloc[:, 0]
scaler = pd.read_csv(DATA / "scaler_params.csv", index_col=0)


def to_raw(X):
    """Undo the scaling from Milestone 3 so ratios make physical sense."""
    return X * scaler.loc[X.columns, "std"].values + scaler.loc[X.columns, "mean"].values


Rtr, Rte = to_raw(Xtr), to_raw(Xte)
pre_run = [c for c in Rtr.columns if c not in RULE_COLS]  # Set B (8 columns)
print("Set B columns:", pre_run)


# ------------------------------------------------------ 2. build new features
def add_features(R):
    d = R[pre_run].copy()
    d["power_per_throughput"] = R.power_draw_watts / R.throughput_ops_per_sec
    d["cpu_gpu_total"] = R.cpu_utilization_percent + R.gpu_utilization_percent
    d["cpu_gpu_gap"] = R.cpu_utilization_percent - R.gpu_utilization_percent
    d["heat_per_watt"] = R.thermal_output_c / R.power_draw_watts
    d["memory_per_throughput"] = R.memory_usage_mb / R.throughput_ops_per_sec
    d["load_x_power"] = R.system_load_level * R.power_draw_watts
    d["power_per_util"] = R.power_draw_watts / (R.cpu_utilization_percent + R.gpu_utilization_percent + 1)
    d["throughput_per_load"] = R.throughput_ops_per_sec / (R.system_load_level + 0.01)
    return d


Ftr, Fte = add_features(Rtr), add_features(Rte)
new_cols = [c for c in Ftr.columns if c not in pre_run]
print("New features:", new_cols)

# ---------------------------------------------------------- 3. compare models
cv = StratifiedKFold(5, shuffle=True, random_state=SEED)


def run(name, Xa, Xb, model):
    cv_acc = cross_val_score(model, Xa, ytr, cv=cv, scoring="accuracy").mean()
    pred = model.fit(Xa, ytr).predict(Xb)
    f1_high = f1_score(yte, pred, average=None, labels=[0, 1, 2])[2]
    print(f"{name:40s} CV acc {cv_acc:.3f} | test acc {accuracy_score(yte, pred):.3f} "
          f"| macro-F1 {f1_score(yte, pred, average='macro'):.3f} | F1 High {f1_high:.3f}")


print("\n=== Models (baseline accuracy = 0.505) ===")
rf = lambda **kw: RandomForestClassifier(n_estimators=200, random_state=SEED, **kw)
run("Random Forest, 8 raw (Set B)", Rtr[pre_run], Rte[pre_run], rf())
run("Random Forest, 8 + 8 new", Ftr, Fte, rf())
run("Random Forest balanced, depth 8", Ftr, Fte, rf(max_depth=8, class_weight="balanced"))
run("Gradient boosting, 8 + 8 new", Ftr, Fte, HistGradientBoostingClassifier(random_state=SEED))
run("Decision Tree depth 4, 8 + 8 new", Ftr, Fte, DecisionTreeClassifier(max_depth=4, random_state=SEED))
mu, sd = Ftr.mean(), Ftr.std()
run("Logistic Regression, 8 + 8 new (scaled)", (Ftr - mu) / sd, (Fte - mu) / sd, LogisticRegression(max_iter=2000))

# ---------------------------------------------- 4. how much information is in each feature
print("\n=== Mutual information with the class ===")
print("New + pre-run features:")
print(pd.Series(mutual_info_classif(Ftr, ytr, random_state=SEED), index=Ftr.columns).sort_values(ascending=False).round(4))
print("Original 10 features (energy and time included):")
print(pd.Series(mutual_info_classif(Rtr, ytr, random_state=SEED), index=Rtr.columns).sort_values(ascending=False).round(4))

# ------------------------------------------ 5. can energy and time be rebuilt?
print("\n=== Can we rebuild energy and time from the pre-run features? (5-fold R2) ===")
for target in RULE_COLS:
    reg = RandomForestRegressor(n_estimators=100, random_state=SEED, n_jobs=-1)
    pred = cross_val_predict(reg, Ftr, Rtr[target], cv=KFold(5, shuffle=True, random_state=SEED))
    print(f"R2 for {target}: {r2_score(Rtr[target], pred):.3f}   (0 = no better than the mean)")
print("Correlation energy vs power*time:",
      round(np.corrcoef(Rtr.energy_consumption_kwh, Rtr.power_draw_watts * Rtr.execution_time_ms)[0, 1], 3))
print("Max |correlation| of any other raw column with energy:",
      round(Rtr.corr()["energy_consumption_kwh"].drop("energy_consumption_kwh").abs().max(), 3))
