import csv
import statistics
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv("medium_data.csv")
df_list = df["reading_time"].tolist()

fig = ff.create_distplot([df_list], ["reading time"], show_hist=False)
fig.show()

meanPop = statistics.mean(df_list)
sDevPop = statistics.stdev(df_list)

print("mean =", meanPop)
print("standard deviation =", sDevPop)






def randomSet_mean(counter):
    data_set = []

    for i in range(0,counter):
        index = random.randint(0,len(df_list) - 1)
        value = df_list[index]
        data_set.append(value)

    mean = statistics.mean(data_set)
    sDev = statistics.stdev(data_set)

    return(mean)



def mean_graph(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["average"], show_hist=False)
    fig.show()


def setup():
    mean_list = []

    for i in range(0,100):
        set_means = randomSet_mean(30)
        mean_list.append(set_means)
    
    mean_graph(mean_list)

    mean = statistics.mean(mean_list)
    sDev = statistics.stdev(mean_list)
    print("sample mean = ",mean)
    print("sample standard deviation = ",sDev)



setup()


    
    
