import csv
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics as st
import random

file_data = pd.read_csv('/Users/prathamarora/Downloads/Python_Projects/sampling_distribution/medium_data.csv')
data = file_data['reading_time'].to_list()

standard_deviation = st.stdev(data)
mean = st.mean(data)

print('Population Mean : ', mean)
print('Population Standard Deviation : ', standard_deviation)

#figure = ff.create_distplot([data], ['reading_time'], show_hist = False)
#figure.add_trace(go.Scatter(x = [mean, mean], y = [0, 1.5], mode = 'lines', name = 'MEAN'))

#figure.show()

def showFigure(lists):
    mean = st.mean(lists)

    figure = ff.create_distplot([lists], ['Sampling Distribution'], show_hist = False)
    figure.add_trace(go.Scatter(x = [mean, mean], y = [0, 1.5], mode='lines', name = 'MEAN'))
    figure.show()

def random_sets_of_mean(counter):
    data_sets = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        values = data[random_index]
        data_sets.append(values)
    mean_of_sample_data = st.mean(data_sets)

    return mean_of_sample_data

def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_sets_of_mean(30)
        mean_list.append(set_of_means)
    
    showFigure(mean_list)

    standard_deviation = st.stdev(mean_list)
    mean = st.mean(mean_list)

    print('Mean of Sampling Distribution : ', mean)
    print('Standard Deviation of Sampling Distribution : ', standard_deviation)

setup()