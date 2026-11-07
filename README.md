# Energy-Efficient AI Performance

End-to-end machine learning project that classifies and predicts the efficiency level of AI system runs
(**High**, **Moderate**, **Low**) from execution metrics, thermal output, and resource consumption.

- **Problem type:** multi-class classification
- **Target variable:** `efficiency_class` (`High_Efficiency`, `Moderate_Efficiency`, `Low_Efficiency`)
- **Dataset:** `data/energy_efficient_dataset.csv`, 7,167 rows, 10 numeric features and the target (plus an `id` column)
- **Dataset source:** [Kaggle](https://www.kaggle.com/datasets/colabsss/energy-efficient-ai-system-performance-dataset)
- **Team:**
  - Ala' Ahmed Saad Hassan
  - Ahmad Amjad Fawzi Ramadan
  - Abdalrahman Omar Dhefallah Almomani
  - Ahmad Ayman Wasef Toubeh
  - Yasmin Samih Ahmad Rabi

## Project progress

| Milestone | Topic | Status | Folder |
|---|---|---|---|
| 1 | Problem definition and dataset understanding | Done | [`milestone-1-problem-and-dataset`](milestone-1-problem-and-dataset) |
| 2 | Data understanding and cleaning | Done | [`milestone-2-data-cleaning`](milestone-2-data-cleaning) |
| 3 | Data preparation for modeling (encoding, scaling, train/test split) | Done | [`milestone-3-data-preparation`](milestone-3-data-preparation) |
| 4 | Modeling, cross-validated comparison and results | Done | [`milestone-4-modeling`](milestone-4-modeling) |

## Repository structure

```
Energy-Efficient-AI-Performance/
├── README.md                              <- you are here
├── data/                                  <- datasets shared by all milestones
│   ├── energy_efficient_dataset.csv       <- raw data (never edited)
│   ├── energy_efficient_dataset.xlsx      <- Excel version of the raw data
│   ├── clean_data.csv                     <- clean data (Milestone 2)
│   └── prepared/                          <- scaled train and test sets (Milestone 3)
├── milestone-1-problem-and-dataset/
│   ├── README.md
│   ├── analysis.ipynb
│   └── Energy-Efficient AI Performance - Milestone 1.pptx
├── milestone-2-data-cleaning/
│   ├── README.md                          <- cleaning decisions, data dictionary, before/after
│   ├── cleaning_notebook.ipynb
│   └── figures/
├── milestone-3-data-preparation/
│   ├── README.md                          <- encoding, scaling, split, leakage checks
│   ├── preparation_notebook.ipynb
│   └── figures/
└── milestone-4-modeling/
    ├── README.md                          <- models, comparison, final model, limits
    ├── modeling_notebook.ipynb
    ├── feature_engineering_experiment.py   <- extra experiment (8 new features)
    ├── feature_engineering_output.txt      <- its printed results
    └── figures/
```

Each milestone has its own folder with its own README and notebook. Datasets live in one shared `data/` folder, so nothing is copied twice.
Milestone 3 reads `data/clean_data.csv` and saves its output in `data/prepared/`. Milestone 4 reads `data/prepared/`.

## Key findings

- The dataset has **no missing values, no duplicate rows, and no outliers** (checked with the IQR rule and box plots).
- The only cleaning changes were converting column names to lowercase and dropping the `id` column.
- The target is **imbalanced**: `High_Efficiency` is only 8% of the rows, so we report macro-F1 next to accuracy.
- The class `efficiency_class` follows a simple rule on two columns (`energy_consumption_kwh` and `execution_time_ms`) that matches all 7,167 rows.
  Details are in [Milestone 3](milestone-3-data-preparation/README.md).
- **Final model:** a Decision Tree (depth 3, 4 leaves) with 99.9% test accuracy and macro-F1 0.998. It mostly recovers the rule above.
- **Without energy and time**, no model beats the 50.5% baseline (best test accuracy 0.505), even with 8 extra engineered features
  (best 0.504, energy cannot be rebuilt from the other columns). See [Milestone 4](milestone-4-modeling/README.md).
- **Limit:** energy and time are known only after a run, so the model cannot predict efficiency in advance.

Full details are in the README of each milestone.

## How to run

1. Install Python 3.11 or newer and the libraries: `pip install pandas numpy matplotlib scikit-learn`.
2. Open a notebook from any milestone folder in VS Code (or Jupyter), select the Python kernel, and choose **Run All**.
3. Notebooks use relative paths (`../data/...`), so keep the folder structure exactly as shown above.
