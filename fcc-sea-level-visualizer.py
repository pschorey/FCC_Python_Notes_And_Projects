import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', sep=',')

    # Create scatter plot
    plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df)

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = linregress(x,y)

    xArr = [*range(1880, 2050, 1)] #fcc error - should be 2051 -2nd num is exclusive
    yArr = []
    def getY ():
        for x in xArr:
            y = slope * x + intercept
            yArr.append(y)
    getY()      
    plt.plot(xArr, yArr)

    #set range on chart
    axes = plt.gca() #gca -get common axes....
    axes.set_xlim([1870,2060])
    axes.set_ylim([-2,12])

    #plt.show()

    # Create second line of best fit
    x2 = df['Year'][-14:] #years 2000 - 2013
    y2 = df['CSIRO Adjusted Sea Level'][-14:]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x2,y2)

    xArr2 = [*range(2000, 2050, 1)]
    yArr2 = []
    def getY2 ():
        for x in xArr2:
            y = slope2 * x + intercept2
            yArr2.append(y)
    getY2()      
    plt.plot(xArr2, yArr2)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level") 
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()