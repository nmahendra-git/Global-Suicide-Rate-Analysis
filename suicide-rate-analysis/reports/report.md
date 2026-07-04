# Report: Global Suicide Rate Analysis

## 1. Objective
Analyze global suicide trends using demographic (sex, age, generation), economic (GDP per capita), and population-level (HDI) indicators.

## 2. Dataset
- **Source:** _Name the dataset and where you got it, e.g. "Suicide Rates Overview 1985 to 2016" (WHO / Kaggle)_
- **Rows:** _fill in after loading_
- **Countries covered:** _fill in_
- **Years covered:** _fill in_
- **Key columns:** country, year, sex, age, suicides_no, population, suicide_rate, gdp_per_capita, hdi, generation

## 3. Data Cleaning Notes
- _Note any missing values you found (HDI is commonly sparse in this dataset) and how you handled them_
- _Note any duplicate rows removed_
- _Note any countries/years excluded due to insufficient data_

## 4. Trend Analysis
**Global rate over time:**
_Insert the trend chart (`visuals/global_trend.png`) and describe: is the global rate rising, falling, or flat? Any notable inflection points?_

## 5. Comparative Analysis

**By country:**
_Insert `visuals/top_countries.png`. Which countries have the highest rates? Any regional patterns?_

**By sex:**
_Insert `visuals/rate_by_sex.png`. State the rate for each sex and the size of the gap._

**By age group:**
_Insert `visuals/rate_by_age.png`. Which age groups are highest-risk at the population level?_

**Sex × age interaction:**
_Insert `visuals/sex_age_heatmap.png`. Does the sex gap widen or narrow with age?_

**By generation:**
_Insert `visuals/generation_comparison.png`. Any generational pattern worth noting?_

## 6. Correlation Analysis

**GDP per capita vs suicide rate:**
- Correlation coefficient: _fill in from notebook output_
- Insert `visuals/gdp_scatter.png`
- Interpretation: _Note that correlation ≠ causation — mention possible confounders (reporting quality differences, cultural stigma affecting reported numbers, healthcare access, etc.)_

**HDI vs suicide rate:**
- Correlation coefficient: _fill in_
- Insert `visuals/hdi_scatter.png`
- Interpretation: _same caveat about confounders_

## 7. Key Insights
1. _Insight 1_
2. _Insight 2_
3. _Insight 3_

## 8. Limitations
- Suicide reporting varies significantly by country due to stigma, legal classification differences, and data collection quality — cross-country comparisons should be read cautiously.
- Correlations shown here are observational, not causal.
- _Add any dataset-specific limitations you noticed_

## 9. Conclusion
_2-3 sentence summary of the overall findings._
