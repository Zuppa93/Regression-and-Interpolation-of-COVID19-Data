import pandas as pandas
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

from scipy import interpolate

# First the data must be read from the csv files
dataset_before = pandas.read_csv('dataset.csv', index_col="Country/Region")
dataset_after = pandas.read_csv('dataset_after.csv', index_col="Country/Region")

# Then we declare variables that we will need
days_before = np.arange(len(dataset_before.loc['Australia']))
days_after  = np.arange(len(dataset_after.loc['Australia']))


#ticks = days_before[0::10]
ticks = days_after[0::10]

length = len(dataset_before.index)
countries = list(dataset_before.index)

color_before        = '#ff7c43'
color_after         = '#ffa600'
color_regression    = '#03a9f4'
color_interpolation = '#01579b'



#for i in range(length):
for i in range(1):
    
    mpl.style.use('seaborn')
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])

    country_after = dataset_after.loc[countries[i]]
    ax.bar(days_after,country_after,color=color_after,label='Before prediction date')
    
    country = dataset_before.loc[countries[i]]
    ax.bar(days_before,country,color=color_before,label='After prediction date')
    
    # Interpolation
    f = interpolate.interp1d(days_before,country,fill_value='extrapolate')
    country_pred = f(days_after)
    ax.plot(days_after,country_pred,color=color_interpolation,label='Interpolation')
    
    # Regression numpy
    # @TODO Regression überarbeiten
    y_fit = np.polyfit(days_before,country,3)
    
    '''
    regression = np.poly1d(np.polyfit(days_before,country,5))
    regression_line = np.linspace(days_before[0],days_after[len(days_after)-1],1000)
    ax.plot(regression_line,regression(regression_line),color=color_regression,label='Regression')
    '''
    # Titles
    ax.set_ylabel("Total confirmed infections")
    ax.set_xlabel("Days(d)")
    ax.set_title(countries[i])
    ax.set_xticks(ticks)
    
    # Legend
    legend = ax.legend(loc='upper left',shadow=False,fontsize='medium')
    
    plt.show()