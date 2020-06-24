import pandas as pandas

# First we read the data from the file
data = pandas.read_csv("./time_series_covid19_confirmed_global.csv")

# Working with the Dataframe

# First we will delete all Columns we don't need
data = data.drop(columns=['Province/State','Lat','Long'])

# We will now note all Countries that have more than 1 province or state the sends information
# Australia
# Canada
# China
# Denmark
# France
# Netherlands
# United Kingdom

Australia   = data[data["Country/Region"] == "Australia"]
Canada      = data[data["Country/Region"] == "Canada"]
China       = data[data["Country/Region"] == "China"]        
Denmark     = data[data["Country/Region"] == "Denmark"]
France      = data[data["Country/Region"] == "France"]
Netherlands = data[data["Country/Region"] == "Netherlands"]
UK          = data[data["Country/Region"] == "United Kingdom"]

# We will need to collapse the provinces and states of each country into one dataframe. 

Australia   =   Australia.groupby('Country/Region').agg('sum')
Canada      =      Canada.groupby('Country/Region').agg('sum')
China       =       China.groupby('Country/Region').agg('sum')
Denmark     =     Denmark.groupby('Country/Region').agg('sum')
France      =      France.groupby('Country/Region').agg('sum')
Netherlands = Netherlands.groupby('Country/Region').agg('sum')
UK          =          UK.groupby('Country/Region').agg('sum')

# Next step is to delete those 7 countries from the data Dataframe and to replace them with the new collapsed ones
# The result will be written into a new .csv file

# The countries, that occur multiple times, must be deleted from die data DataFrame first.

data = data[data['Country/Region'] != 'Australia']
data = data[data['Country/Region'] != 'Canada']
data = data[data['Country/Region'] != 'China']
data = data[data['Country/Region'] != 'Denmark']
data = data[data['Country/Region'] != 'France']
data = data[data['Country/Region'] != 'Netherlands']
data = data[data['Country/Region'] != 'United Kingdom']

# Now we concatenate the new DataFrames

countries = pandas.concat([Australia,Canada,China,Denmark,France,Netherlands,UK])


countries = countries.reset_index()
countries = countries.set_index(pandas.Index([8,9,10,11,12,13,14]))

result = pandas.concat([data,countries])

result.to_csv("./dataset.csv",index=False)