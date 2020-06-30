import pandas as pandas
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pandas.read_csv("./dataset.csv", index_col="Country/Region")

days = df.columns
ticks = days[0::15]
country_names = list(df.index)

length = len(df.index)

for i in range(length):
    
    mpl.style.use('seaborn')
    fig = plt.figure()  
    ax = fig.add_axes([0,0,1,1])        
    
    country = df.loc[country_names[i]]
    ax.bar(days,country,color='#ff7c43')
    ax.set_ylabel("Total confirmed infections")
    ax.set_xlabel("Days(d)")
    ax.set_title(country_names[i])
    ax.set_xticks(ticks)
    
    file_name = "./Plots/"+country_names[i]+".png"
    plt.savefig(file_name,dpi=300,bbox_inches='tight')
    
    plt.show()
