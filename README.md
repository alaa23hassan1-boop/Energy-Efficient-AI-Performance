# Energy-Efficient AI Performance

End-to-end machine learning project that classifies and predicts the efficiency level of AI system runs
(**High**, **Moderate**, **Low**) from execution metrics, thermal output, and resource consumption.

- **Problem type:** multi-class classification
- **Target variable:** `efficiency_class` (`High_Efficiency`, `Moderate_Efficiency`, `Low_Efficiency`)
- **Dataset:** `data/energy_efficient_dataset.csv`, 7,167 rows and 11 features (plus an `id` column)
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
└── milestone-3-data-preparation/
    ├── README.md                          <- encoding, scaling, split, leakage checks
    ├── preparation_notebook.ipynb
    └── figures/
```

Each milestone has its own folder with its own README and notebook. Datasets live in one shared `data/` folder, so nothing is copied twice.
Milestone 3 reads `data/clean_data.csv` and saves its output in `data/prepared/`.

## Key findings so far

- The dataset has **no missing values, no duplicate rows, and no outliers** (checked with the IQR rule and box plots).
- The only cleaning changes were converting column names to lowercase and dropping the `id` column.
- The target is **imbalanced**: `High_Efficiency` is only 8% of the rows. This will be handled during modeling.
- The target is almost decided by `energy_consumption_kwh` (one column alone reaches 92% accuracy), so we will confirm with the coach if this column should be a feature. Details in [Milestone 3](milestone-3-data-preparation/README.md).

Full details are in [Milestone 2](milestone-2-data-cleaning/README.md) and [Milestone 3](milestone-3-data-preparation/README.md).

## How to run

1. Install Python 3.11 or newer and the libraries: `pip install pandas numpy matplotlib scikit-learn`.
2. Open a notebook from any milestone folder in VS Code (or Jupyter), select the Python kernel, and choose **Run All**.
3. Notebooks use relative paths (`../data/...`), so keep the folder structure exactly as shown above.
