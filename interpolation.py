import pandas as pandas
import matplotlib.pyplot as plt
import numpy as np

from scipy import interpolate
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

dataset = pandas.read_csv('dataset.csv', index_col="Country/Region")
australia = dataset.loc["Brazil"]
australia = australia.to_numpy()

degree = 3

# Now we try yo plot this dataset

days = np.arange(len(australia))

# Dataset
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(days,australia,label='Dataset')

# Interpolation
f = interpolate.interp1d(days,australia,fill_value='extrapolate')
days_new = np.arange(len(days)+15)
australia_new = f(days_new)
ax.plot(days_new,australia_new,color='green',label='Interpolation')

# Regression numpy
regression = np.poly1d(np.polyfit(days,australia,degree))
regression_line = np.linspace(days[0],days_new[len(days_new)-1],100)
ax.plot(regression_line,regression(regression_line),color='red',label='Regression numpy')

# Regression with sklearn
# Fitting the linear regression to the dataset
Input=[('polynomial',PolynomialFeatures(degree=degree)),('modal',LinearRegression())]
pipe = Pipeline(Input)
pipe.fit(days.reshape(-1,1),australia.reshape(-1,1))
poly_pred = pipe.predict(days_new.reshape(-1,1))
sorted_zip = sorted(zip(days_new,poly_pred))

x_poly,poly_pred = zip(*sorted_zip)

ax.plot(days_new,poly_pred,color='black',label='Regression sklearn')


# legend
legend = ax.legend(loc='upper left',shadow=False,fontsize='medium')

plt.xticks(days_new[0::10])
plt.show()

