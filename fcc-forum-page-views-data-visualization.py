import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True, sep=',')

#clean: filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset
df = df[(df['value'] > df['value'].quantile(.025)) & (df['value'] < df['value'].quantile(.975))]

def draw_line_plot():
  # Draw line plot
    '''alternative sns way...
    g = sns.lineplot(data=df)
    fig = g.get_figure()
    '''  
    fig, ax = plt.subplots()
    plt.plot(df['value'])
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Years'] = df_bar.index.year
    df_bar['Months'] = df_bar.index.strftime("%B")
    df_bar_grouped = df_bar.groupby(['Years','Months'], sort=False, as_index=False)
    df_bar_grouped = df_bar_grouped['value'].mean()

    # Draw bar plot
    months = ['January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
    ]

    g = sns.catplot(
        data=df_bar_grouped, 
        x='Years',
        y='value',
        #col='months',
        hue='Months',
        hue_order=months,
        kind='bar',
        legend_out=False,
        #legend=False,
        palette = sns.color_palette()
    )

    g.set(xlabel='Years', ylabel='Average Page Views')
    fig = g.fig

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    shortMonths = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    sns.boxplot(x='month', y='value', order=shortMonths, data=df_box, ax=ax2)
    fig.tight_layout()
    ax1.set(xlabel='Year', ylabel='Page Views', title='Year-wise Box Plot (Trend)')
    ax2.set(xlabel='Month', ylabel='Page Views', title='Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
