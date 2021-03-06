import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = 0
df.loc[((df['weight'] / (df['height'] / 100) ** 2) > 25), 'overweight'] = 1

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] >= 1, 'gluc'] = 1


# Draw Categorical Plot
def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=[
                     "active", "alco", "cholesterol", "gluc", "overweight", "smoke"])
    df_cat['total'] = 1
    df_cat = df_cat.groupby(
        ['variable', 'cardio', 'value'], as_index=False).count()

    graph = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar'
    )

    fig = graph.fig
    fig.savefig('generated_catplot.png')
    return fig


def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    fig, ax = plt.subplots(figsize=(12, 12))

    ax = sns.heatmap(
        data=corr,
        vmin=-0.1,
        vmax=0.25,
        center=0,
        annot=True,
        fmt='.1f',
        linewidths=0.5,
        cbar_kws={'shrink': .45, 'format': '%.2f'},
        square=True,
        mask=mask
    )

    fig.savefig('generated_heatmap.png')
    return fig
