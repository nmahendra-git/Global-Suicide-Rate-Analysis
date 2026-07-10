+

## Global Suicide Rate Analysis

Analyzes global suicide trends using demographic (sex, age, generation), economic (GDP per capita), and population-level (HDI) indicators. This is a statistical/demographic study of aggregate public data — comparable to how public-health researchers use WHO datasets.

## Project Structure

suicide-rate-analysis/
├── notebooks/
│   └── 01_suicide_rate_analysis.ipynb           # Main notebook: run this end-to-end
├── src/
│   ├── data_loader.py                           # Loads & cleans the raw CSV
│   ├── analysis.py                              # All aggregation / statistics functions
│   └── visualize.py                             # All plotting functions
├── data/
│   └── sample_data.csv                          # Small synthetic dataset (so the project runs out of the box)
├── visuals/                                     # Saved chart images (generated when you run the notebook)
├── reports/
│   └── report.md                                # Report template — fill in your findings
├── requirements.txt
├── .gitignore
└── README.md


## Tech Stack
Python, Pandas, Matplotlib, Seaborn

## Setup

1. **Clone the repo**
   bash
   git clone https://github.com/<your-username>/suicide-rate-analysis.git
   cd suicide-rate-analysis


2. **Create a virtual environment**
   bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate         # Windows
   

3. **Install dependencies**
   bash
   pip install -r requirements.txt


## Getting the Real Dataset

This repo ships with `data/sample_data.csv` — a small **synthetic** dataset so the notebook runs immediately without any downloads. For the actual analysis, download a real dataset:

- **"Suicide Rates Overview 1985 to 2016"** (WHO data, mirrored on Kaggle): search Kaggle for this exact title, download `master.csv`, and place it in `data/master.csv`
- Alternative: **WHO Global Health Observatory** (https://www.who.int/data/gho) has raw suicide mortality data by country/year/sex/age if you want the most authoritative source

Once downloaded, open the notebook and change:
```python
DATA_PATH = '../data/sample_data.csv'
```
to:
```python
DATA_PATH = '../data/master.csv'
```
The `data_loader.py` module is built to handle that dataset's exact (messy) column names automatically.

## How to Run

```bash
jupyter notebook notebooks/01_suicide_rate_analysis.ipynb
```
Run all cells top to bottom. The notebook covers: data cleaning → EDA → trend analysis → comparative analysis (country/sex/age/generation) → correlation analysis (GDP, HDI) → summary of insights. Charts are automatically saved into `visuals/`.

## Learning Outcomes
- Cleaning a real-world dataset with inconsistent column names and missing values
- Computing population-weighted rates correctly (not just averaging raw percentages)
- Trend analysis over time
- Comparative analysis across multiple demographic dimensions
- Correlation analysis between economic/development indicators and an outcome variable, with appropriate causal caveats

## Deliverables Checklist
- [x] Analysis notebook (`notebooks/01_suicide_rate_analysis.ipynb`)
- [x] Charts and visual summaries (`visuals/`)
- [x] Interpretation report (`reports/report.md`)

## A Note on This Topic
This project analyzes aggregate, anonymized population statistics for the purpose of understanding public-health trends — not individual cases. If this subject affects you personally, please see the Crisis Resources section below rather than relying on this analysis for anything personal.

## License
This project is for educational purposes.
