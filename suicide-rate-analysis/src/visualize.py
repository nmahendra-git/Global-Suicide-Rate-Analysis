"""
visualize.py
------------
Plotting helpers for the suicide rate analysis project.
Kept separate from analysis.py so charts and numbers can be tested
independently.
"""

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")


def plot_global_trend(yearly_df, save_path=None):
    """Line chart of global suicide rate (per 100k) over time."""
    plt.figure(figsize=(10, 5))
    plt.plot(yearly_df["year"], yearly_df["rate_per_100k"], marker="o", color="#4C72B0")
    plt.title("Global Suicide Rate Trend Over Time")
    plt.xlabel("Year")
    plt.ylabel("Rate per 100,000 population")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()


def plot_top_countries(top_df, save_path=None):
    """Horizontal bar chart of top countries by suicide rate."""
    plt.figure(figsize=(9, 6))
    ordered = top_df.sort_values("rate_per_100k")
    plt.barh(ordered["country"], ordered["rate_per_100k"], color="#DD8452")
    plt.title("Top Countries by Suicide Rate (per 100k)")
    plt.xlabel("Rate per 100,000 population")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()


def plot_rate_by_sex(sex_df, save_path=None):
    """Bar chart comparing suicide rate by sex."""
    plt.figure(figsize=(6, 5))
    plt.bar(sex_df["sex"], sex_df["rate_per_100k"], color=["#55A868", "#C44E52"])
    plt.title("Suicide Rate by Sex")
    plt.ylabel("Rate per 100,000 population")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()


def plot_rate_by_age(age_df, save_path=None):
    """Bar chart of suicide rate by age group."""
    plt.figure(figsize=(9, 5))
    plt.bar(age_df["age"], age_df["rate_per_100k"], color="#8172B2")
    plt.title("Suicide Rate by Age Group")
    plt.ylabel("Rate per 100,000 population")
    plt.xticks(rotation=30)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()


def plot_sex_age_heatmap(pivot_df, save_path=None):
    """Heatmap of suicide rate by sex (rows) and age group (columns)."""
    plt.figure(figsize=(10, 4))
    sns.heatmap(pivot_df, annot=True, fmt=".1f", cmap="Reds")
    plt.title("Suicide Rate (per 100k) by Sex and Age Group")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()


def plot_gdp_scatter(country_level_df, correlation, save_path=None):
    """Scatter plot of GDP per capita vs suicide rate, with correlation in the title."""
    plt.figure(figsize=(8, 6))
    plt.scatter(country_level_df["avg_gdp_per_capita"], country_level_df["rate_per_100k"],
                alpha=0.7, color="#4C72B0")
    plt.title(f"GDP per Capita vs Suicide Rate (corr = {correlation:.2f})")
    plt.xlabel("Average GDP per Capita ($)")
    plt.ylabel("Rate per 100,000 population")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()


def plot_hdi_scatter(country_level_df, correlation, save_path=None):
    """Scatter plot of HDI vs suicide rate, with correlation in the title."""
    plt.figure(figsize=(8, 6))
    plt.scatter(country_level_df["avg_hdi"], country_level_df["rate_per_100k"],
                alpha=0.7, color="#DD8452")
    plt.title(f"HDI vs Suicide Rate (corr = {correlation:.2f})")
    plt.xlabel("Average Human Development Index")
    plt.ylabel("Rate per 100,000 population")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()


def plot_generation_comparison(gen_df, save_path=None):
    """Bar chart of suicide rate by generation cohort."""
    plt.figure(figsize=(9, 5))
    ordered = gen_df.sort_values("rate_per_100k")
    plt.barh(ordered["generation"], ordered["rate_per_100k"], color="#64B5CD")
    plt.title("Suicide Rate by Generation")
    plt.xlabel("Rate per 100,000 population")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()
