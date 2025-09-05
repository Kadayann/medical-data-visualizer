import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 reads the file
df = pd.read_csv("medical_examination.csv")

# 2 bmi is the metric for overweight or not
bmi = df["weight"] / ((df["height"] / 100) ** 2)
df["overweight"] = (bmi > 25).astype(int)

# 3 label cholesterol and glucose 1 as normal, 2 and 3 as high
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)

# 4
def draw_cat_plot():
    # 5 define the columns, and create a new dataframe with cardio
    cols = ["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]
    df_cat = df[["cardio"] + cols].copy()

    # 6 long format with cardio as id
    df_cat = pd.melt(
        df_cat,
        id_vars=["cardio"],
        value_vars=cols,
        var_name="variable",
        value_name="value",
    )

    # 7 group and count
    df_cat = (
        df_cat.groupby(["cardio", "variable", "value"])
        .size()
        .reset_index(name="total")
    )

    # 8 plot
    g = sns.catplot(
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar",
    )
    g.set_axis_labels("variable", "total")
    g.set_titles("cardio = {col_name}")
    g.despine(left=True)

    fig = g.fig

    # 9
    fig.savefig("catplot.png")
    return fig


# 10
def draw_heat_map():
    # 11 clean
    df_heat = df.copy()

    cond_bp = df_heat["ap_lo"] <= df_heat["ap_hi"]

    h_low, h_high = df_heat["height"].quantile([0.025, 0.975])
    cond_h = (df_heat["height"] >= h_low) & (df_heat["height"] <= h_high)

    w_low, w_high = df_heat["weight"].quantile([0.025, 0.975])
    cond_w = (df_heat["weight"] >= w_low) & (df_heat["weight"] <= w_high)

    df_heat = df_heat[cond_bp & cond_h & cond_w]

    # 12 correlation
    corr = df_heat.corr(numeric_only=True)

    # 13 mask
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14 figure
    fig, ax = plt.subplots(figsize=(12, 9))

    # 15 heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        vmin=-0.1,
        vmax=0.25,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        ax=ax,
    )

    # 16
    fig.savefig("heatmap.png")
    return fig

