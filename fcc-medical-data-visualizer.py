import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv', index_col=0, sep=',')

# Add 'overweight' column
df['overweight'] = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = np.where(df['overweight']>25, 1, 0) #if value over 25 return 1, else retun 0

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.where(df['cholesterol']==1, 0, 1)
df['gluc'] = np.where(df['gluc']==1, 0, 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat['total'] = 0
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count() #using groupby idea from: https://repl.it/@JooVictorVict33/fcc-medical-data-visualizer#medical_data_visualizer.py

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(
        data=df_cat, 
        x="variable", 
        y="total", 
        col="cardio",
        hue="value",
        kind="bar",
        legend_out=True,
    )
    fig = g.fig #From https://forum.freecodecamp.org/t/fcc-medical-data-visualizer/408460/3

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    heightCap = np.percentile(df['height'], 97.5)
    weightMin = np.percentile(df['weight'], 2.5)
    weightMax = np.percentile(df['weight'], 97.5)
    #print(heightCap, weightMin, weightMax)
    df_heat = df
    df_heat = df_heat[((df_heat['ap_lo'] <= df_heat['ap_hi']) & (df_heat['height'] >= df_heat['height'].quantile(0.025)))]
    df_heat = df_heat[(df_heat['height'] <= heightCap)]
    df_heat = df_heat[((df_heat['weight'] >= weightMin) & (df_heat['weight'] <= weightMax))]

    #no idea why, but fcc wants id to be included with heatmap, I can't make it work unless adding an id arr....
    df_heat['id'] = range(len(df_heat)) 
    df_heat= df_heat[['id','age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight']]
    df_heat = df_heat.astype('float')

    
    # Calculate the correlation matrix
    #corr = df_heat.corr(method="spearman") -close but slightly wrong ansers, setting vmax and vmin fixed....instead of spearman method
    corr = df_heat.corr()
    # Generate a mask for the upper triangle
    #from documentation: https://seaborn.pydata.org/generated/seaborn.heatmap.html?highlight=heatmap#seaborn.heatmap
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    with sns.axes_style("white"):
      fig, ax = plt.subplots(figsize=(12, 12))
      
      # Draw the heatmap with 'sns.heatmap()'
      ax = sns.heatmap(corr, square=True, 
      mask=mask, annot=True, fmt='.1f', vmin='0.0', vmax='0.25')

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
