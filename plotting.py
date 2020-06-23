import pandas as pandas
import matplotlib.pyplot as plt

df = pandas.read_csv("./dataset.csv", index_col="Country/Region")

days = df.columns
ticks = days[0::15]

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

length = len(df.index)
print(length)

country_names = list(df.index)

for i in range(length):
    print(i)
    print(country_names[i])

    fig = plt.figure()  
    ax = fig.add_axes([0,0,1,1])        
    
    country = df.loc[country_names[i]]
    ax.bar(days,country)
    ax.set_ylabel("Total confirmed infections")
    ax.set_xlabel("Days(d)")
    ax.set_title(country_names[i])
    ax.set_xticks(ticks)
    
    file_name = "./Plots/"+country_names[i]+".png"
    plt.savefig(file_name,dpi=300,bbox_inches='tight')
    
    plt.show()
