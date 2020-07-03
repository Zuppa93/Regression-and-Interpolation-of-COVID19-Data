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

ticks = days_after[0::10]

length = len(dataset_before.index)
countries = list(dataset_before.index)

color_before        = '#ff7c43'
color_after         = '#ffa600'
color_regression    = '#03a9f4'
color_interpolation = '#01579b'

# Constants for errorcalculation
prediction_interval  = days_after[len(days_before):]
milestones           = prediction_interval[::7]
last_day             = prediction_interval[len(prediction_interval)-1] 
milestones           = np.append(milestones,last_day)

# Variables to save the differences between prediction and real values in percent
differences_interpolation = np.zeros(len(milestones),dtype=np.float64)
differences_regression    = np.zeros(len(milestones),dtype=np.float64)

average_difference_interpolation = np.zeros(len(milestones),dtype=np.float64)
average_difference_regression    = np.zeros(len(milestones),dtype=np.float64)

# dataframe in which the information will be stored
# First the dictionary
strings = milestones.astype(str)



for i in range(length):
#for i in range(0):
    
    mpl.style.use('seaborn')
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])

    country_after = dataset_after.loc[countries[i]]
    ax.bar(days_after,country_after,color=color_after,label='Before prediction date')
    
    country = dataset_before.loc[countries[i]]
    ax.bar(days_before,country,color=color_before,label='After prediction date')
    
    # Interpolation
    f = interpolate.interp1d(days_before,country,fill_value='extrapolate')
    country_pred_interpolation = f(days_after)
    ax.plot(days_after,country_pred_interpolation,color=color_interpolation,label='Interpolation')
    
    # Regression numpy
    regression = np.poly1d(np.polyfit(days_before,country,3))
    country_pred_regression = regression(days_after)
    ax.plot(days_after,country_pred_regression,color=color_regression,label='Regression')

    # Titles
    ax.set_ylabel("Total confirmed infections")
    ax.set_xlabel("Days(d)")
    ax.set_title(countries[i])
    ax.set_xticks(ticks)
    
    # Legend
    legend = ax.legend(loc='upper left',shadow=False,fontsize='medium')
    
    file_name = "./Extrapolations/"+countries[i]+".png"
    plt.savefig(file_name,dpi=300,bbox_inches='tight')
    
    plt.show()
    
    # Errorcalculation
    # We want to calculate the differences in seven day intervals plus the last and first day
    for j in range(len(milestones)):
        temp = country_pred_interpolation[milestones[j]] / country_after[milestones[j]]
        differences_interpolation[j] = abs(temp-1)
        
        temp = country_pred_regression[milestones[j]] / country_after[milestones[j]]
        differences_regression[j] = abs(temp-1)
        
        average_difference_interpolation[j] += differences_interpolation[j]
        average_difference_regression[j]    += differences_regression[j]
        
# Calculating the average and plotting it
for i in range(len(milestones)):
    
    average_difference_interpolation[i] = (average_difference_interpolation[i]/ length) * 100
    average_difference_regression[i]    = (average_difference_regression[i]   / length) * 100


bar_width = 0.8
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

b1 = ax.bar(milestones          ,average_difference_interpolation,width=bar_width,label='Interpolation',color=color_interpolation)
b2 = ax.bar(milestones+bar_width,average_difference_regression   ,width=bar_width,label='Regression',color=color_regression)

legend = ax.legend(loc='upper left',shadow=False,fontsize='medium')

plt.savefig('AverageBarChart.png',dpi=300,bbox_inches='tight')

plt.show()
     
    
