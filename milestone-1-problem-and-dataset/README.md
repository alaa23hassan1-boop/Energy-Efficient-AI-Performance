# Milestone 1: Problem Definition and Dataset Understanding

**Project:** Energy-Efficient AI Performance Prediction
**Deliverable:** Project proposal and technical proof for classifying AI system energy efficiency levels

## Team

- Ala' Ahmed Saad Hassan
- Ahmad Amjad Fawzi Ramadan
- Abdalrahman Omar Dhefallah Almomani
- Ahmad Ayman Wasef Toubeh
- Yasmin Samih Ahmad Rabi

## Business problem

High power consumption and operational costs in AI infrastructure lead to a growing carbon footprint and a risk of thermal throttling.

## Project objectives

- **Technical objective:** develop a robust machine learning classifier that accurately predicts hardware energy efficiency levels from execution metrics.
- **Commercial objective:** optimize workload scheduling and hardware resource allocation to reduce data center electricity costs and support green computing.

## Problem type

Multi-class classification. The target variable is `efficiency_class` with three classes: High, Moderate, and Low efficiency.

## Dataset

| Item | Detail |
|---|---|
| Name | AI Execution Performance Log |
| Files | `data/energy_efficient_dataset.csv` and `data/energy_efficient_dataset.xlsx` (same data) |
| Source | [Kaggle](https://www.kaggle.com/datasets/colabsss/energy-efficient-ai-system-performance-dataset) |
| Size | 7,167 rows and 12 columns: 10 numeric measurements, an `id` column, and the target |
| Measurements | Power draw, temperature, execution time, throughput, CPU and GPU utilization, memory usage, energy consumption, system load, and a resource utilization index |
| Target variable | `efficiency_class` (High, Moderate, Low) |

The exact column names and their meanings are in the [data dictionary](../milestone-2-data-cleaning/README.md#3-data-dictionary).

> **Note:** the Milestone 1 slides used approximate feature names (for example `Power_Draw_W` and `Temperature_C`) and mentioned 12 features.
> The real file has 10 numeric measurements plus `id` and the target (12 columns in total), and the real names are listed in the data dictionary.

## Technical proof

The notebook `analysis.ipynb` loads the dataset with Pandas and runs three checks:

1. `df.head()` previews the first rows to confirm the data loads correctly.
2. `df.info()` checks column types, null values, and the number of columns.
3. `value_counts()` checks the distribution of `efficiency_class`.

> **Update from Milestone 2:** a deeper check showed that the classes are **not balanced**. `High_Efficiency` is only 8% of the rows
> (576 of 7,167). See [Milestone 2](../milestone-2-data-cleaning/README.md) for the full analysis and how we plan to handle it.

## Files in this folder

| File | What it is |
|---|---|
| `analysis.ipynb` | Dataset loading and first look at the data |
| `Energy-Efficient AI Performance - Milestone 1.pptx` | Milestone 1 presentation slides |

The notebook reads the dataset from the shared data folder:

```python
df = pd.read_csv("../data/energy_efficient_dataset.csv")
```
