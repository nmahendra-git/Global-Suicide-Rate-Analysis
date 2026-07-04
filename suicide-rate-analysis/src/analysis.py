"""
analysis.py
-----------
Core analysis functions for the global suicide rate dataset.
Each function returns a DataFrame (or Series) ready to be plotted or
printed — kept separate from visualize.py so the numbers can be
inspected/tested independently of the charts.
"""

import pandas as pd
import numpy as np


def global_trend_by_year(df):
    """Aggregate global suicide rate by year.

    Note: averaging a per-100k rate across rows isn't population-weighted,
    so we compute the rate properly as total suicides / total population.
    """
    yearly = df.groupby("year").agg(
        total_suicides=("suicides_no", "sum"),
        total_population=("population", "sum"),
    ).reset_index()
    yearly["rate_per_100k"] = (
        yearly["total_suicides"] / yearly["total_population"] * 100000
    )
    return yearly


def top_countries_by_rate(df, n=10, min_years=5):
    """Ranks countries by average suicide rate (population-weighted).

    Args:
        df: cleaned dataframe
        n: how many top countries to return
        min_years: exclude countries with fewer than this many years of data
                   (avoids one-off spikes from sparse data dominating the ranking)
    """
    country_stats = df.groupby("country").agg(
        total_suicides=("suicides_no", "sum"),
        total_population=("population", "sum"),
        years_of_data=("year", "nunique"),
    ).reset_index()

    country_stats = country_stats[country_stats["years_of_data"] >= min_years]
    country_stats["rate_per_100k"] = (
        country_stats["total_suicides"] / country_stats["total_population"] * 100000
    )
    return country_stats.sort_values("rate_per_100k", ascending=False).head(n)


def rate_by_sex(df):
    """Suicide rate broken down by sex."""
    grouped = df.groupby("sex").agg(
        total_suicides=("suicides_no", "sum"),
        total_population=("population", "sum"),
    ).reset_index()
    grouped["rate_per_100k"] = (
        grouped["total_suicides"] / grouped["total_population"] * 100000
    )
    return grouped


def rate_by_age_group(df):
    """Suicide rate broken down by age group."""
    grouped = df.groupby("age").agg(
        total_suicides=("suicides_no", "sum"),
        total_population=("population", "sum"),
    ).reset_index()
    grouped["rate_per_100k"] = (
        grouped["total_suicides"] / grouped["total_population"] * 100000
    )
    return grouped.sort_values("rate_per_100k", ascending=False)


def rate_by_sex_and_age(df):
    """Pivot table: rate_per_100k by sex (rows) and age group (columns)."""
    grouped = df.groupby(["sex", "age"]).agg(
        total_suicides=("suicides_no", "sum"),
        total_population=("population", "sum"),
    ).reset_index()
    grouped["rate_per_100k"] = (
        grouped["total_suicides"] / grouped["total_population"] * 100000
    )
    pivot = grouped.pivot(index="sex", columns="age", values="rate_per_100k")
    return pivot


def gdp_vs_suicide_rate(df):
    """Country-level average GDP per capita vs suicide rate, for correlation analysis."""
    country_level = df.groupby("country").agg(
        total_suicides=("suicides_no", "sum"),
        total_population=("population", "sum"),
        avg_gdp_per_capita=("gdp_per_capita", "mean"),
    ).reset_index()
    country_level["rate_per_100k"] = (
        country_level["total_suicides"] / country_level["total_population"] * 100000
    )
    correlation = country_level[["avg_gdp_per_capita", "rate_per_100k"]].corr().iloc[0, 1]
    return country_level, correlation


def hdi_vs_suicide_rate(df):
    """Country-level average HDI vs suicide rate, for correlation analysis.

    Drops rows with missing HDI, which is common in the real-world dataset.
    """
    df_hdi = df.dropna(subset=["hdi"])
    if df_hdi.empty:
        return None, None

    country_level = df_hdi.groupby("country").agg(
        total_suicides=("suicides_no", "sum"),
        total_population=("population", "sum"),
        avg_hdi=("hdi", "mean"),
    ).reset_index()
    country_level["rate_per_100k"] = (
        country_level["total_suicides"] / country_level["total_population"] * 100000
    )
    correlation = country_level[["avg_hdi", "rate_per_100k"]].corr().iloc[0, 1]
    return country_level, correlation


def generation_comparison(df):
    """Suicide rate broken down by generation cohort."""
    grouped = df.groupby("generation").agg(
        total_suicides=("suicides_no", "sum"),
        total_population=("population", "sum"),
    ).reset_index()
    grouped["rate_per_100k"] = (
        grouped["total_suicides"] / grouped["total_population"] * 100000
    )
    return grouped.sort_values("rate_per_100k", ascending=False)
