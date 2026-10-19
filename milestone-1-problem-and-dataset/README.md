# Milestone 1: Problem Definition and Dataset Understanding

## Business problem

AI workloads use a lot of energy. Teams need a quick way to tell which runs are energy efficient and which are not, using measurements that
are already collected (power draw, CPU and GPU use, memory, execution time, heat). This project builds a model that predicts the
**efficiency class** of a run.

## Project objectives

- Predict `efficiency_class` (High, Moderate, Low) from system performance measurements.
- Find which measurements matter most for efficiency.
- Build and evaluate a classification model that works well on all three classes.

*(Adjust the text above so it matches the proposal you presented.)*

## Dataset

| Item | Detail |
|---|---|
| File | `data/energy_efficient_dataset.csv` (Excel version: `data/energy_efficient_dataset.xlsx`) |
| Source | *[Add the dataset source here]* |
| Size | 7,167 rows, 12 columns (10 numeric measurements, `id`, and the target) |
| Target variable | `efficiency_class` (3 classes) |

The full list of columns and their meanings is in the [Milestone 2 README](../milestone-2-data-cleaning/README.md#3-data-dictionary).

## Files in this folder

| File | What it is |
|---|---|
| `analysis.ipynb` | Initial dataset loading and first look at the data |
| `Energy-Efficient AI Performance - Milestone 1.pptx` | Milestone 1 presentation slides |

## Note on file paths

The dataset is stored in the shared `data/` folder at the root of the repository. In `analysis.ipynb`, load it with:

```python
df = pd.read_csv("../data/energy_efficient_dataset.csv")
```
