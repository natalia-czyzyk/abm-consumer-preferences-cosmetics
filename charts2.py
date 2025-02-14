import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import Greens
from textwrap import wrap
from datetime import datetime

df = pd.read_csv('survey.csv')
df = df.drop(columns = ['Sygnatura czasowa'])

# Dataframe for the plots

df.columns = ['D1', 'D2', 'D3', 'D4', 'D5', 'S1', 'A1', 'F1', 'F2', 'F3', 'F4', 'F5', 'MC1', 'MC2', 'MC3', 'PI1', 'PI2', 'PI3', 'SI1', 'SI2', 'SI3', 'IB1', 'EA1', 'EA2', 'EA3', 'R1']
df = df.replace(['kobieta', 'mężczyzna', 'inne/nie chcę podawać'], ['female', 'male', 'other/prefer not to disclose'])
df = df.replace(['20 i poniżej', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51 i powyżej'], ['20 and below', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51 and above'])
df = df.replace(['wieś', 'miejscowość do 100 tys. mieszkańców', 'miejscowość do 250 tys. mieszkańców', 'miejscowość do 500 tys. mieszkańców', 'miejscowość powyżej 500 tys. mieszkańców'], ['village', 'city up to 100k inhabitants', 'city up to 250k inhabitants', 'city up to 500k inhabitants', 'city above 500k inhabitants'])
df = df.replace(['podstawowe', 'zasadnicze zawodowe', 'średnie', 'wyższe', 'inne/nie chcę podawać'], ['primary', 'other/prefer not to disclose', 'secondary', 'higher', 'other/prefer not to disclose'])
df = df.replace(['3000 i poniżej', '3001 - 4000', '4001 - 5000', '5001 - 6000', '6001 - 7000', '7001 i powyżej', 'nie chcę podawać'], ['3000 and below', '3001 - 4000', '4001 - 5000', '5001 - 6000', '6001 - 7000', '7001 and above', 'other/prefer not to disclose'])
df = df.replace(['tak', 'nie'], ['yes', 'no'])
df = df.replace(['bardzo ważne', 'ważne', 'średnio ważne', 'trochę ważne', 'w ogóle nieważne'], ['very important', 'important', 'somewhat important', 'slightly important', 'not important at all'])
df = df.replace(['zdecydowanie się zgadzam', 'raczej się zgadzam', 'nie mam zdania/trudno powiedzieć', 'raczej się nie zgadzam', 'zdecydowanie się nie zgadzam'], ['strongly agree', 'somewhat agree', 'no opinion/difficult to say', 'somewhat disagree', 'strongly disagree'])

# Triple plots for SI, PI, EA and MC

df_triple = df[['SI1', 'SI2', 'SI3', 'PI1', 'PI2', 'PI3', 'MC1', 'MC2', 'MC3', 'EA1', 'EA2', 'EA3']]
df_triple = df_triple.dropna()
column_list = ['SI1', 'SI2', 'SI3', 'PI1', 'PI2', 'PI3', 'MC1', 'MC2', 'MC3', 'EA1', 'EA2', 'EA3']

# function for the plots

font_plot = {'family': 'serif', 'color': 'black', 'weight': 'normal', 'size': 14}
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12

def plot_data_with_labels(data, categories, label_names, figname):
    questions = list(data.keys())
    values = {category: [data[question].get(category, 0) for question in questions] for category in categories}
    
    fig, ax = plt.subplots(figsize=(10, 6)) 
    index = np.arange(len(questions))
    bar_width = 0.14
    spacing = 0.02 

    for i, category in enumerate(categories):
        bars = ax.bar(index + i * (bar_width + spacing), values[category], bar_width, label=category,
                      color=Greens(0.4 + i * 0.15))
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval + 0.2, f'{yval:.0f}%', ha='center', va='bottom', fontdict=font_plot)

    ax.set_ylabel('Frequency [%]', fontdict=font_plot)
    ax.set_xticks(index + (bar_width + spacing) * (len(categories) - 1) / 2)
    wrapped_labels = ['\n'.join(wrap(label_names.get(q, q), width=24)) for q in questions]
    ax.set_xticklabels(wrapped_labels, fontdict=font_plot) 
    
    # Remove top and right frames
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Positioning legend outside the chart
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    
    filename = f"{figname}.png"
    plt.savefig(filename, bbox_inches='tight')
    plt.show()
    
# SI:
category_order = ['strongly agree', 'somewhat agree', 'no opinion/difficult to say', 'somewhat disagree', 'strongly disagree']
label_names = {
    'SI1': 'When choosing sustainable cosmetics, I often rely on the opinions or recommendations of my friends',
    'SI2': 'If my friends use and recommend a specific sustainable cosmetic, there is a greater chance that I will decide to purchase it',
    'SI3': 'I believe that my friends are able to influence my opinion and/or attitude regarding sustainable cosmetics'
}
figname = 'SI'
value_counts_dict_SI = {}
for col in ['SI1', 'SI2', 'SI3']:
    value_counts_dict_SI[col] = df_triple[col].value_counts(normalize=True) * 100
value_counts_dict_SI['SI2']['strongly disagree'] = 0.69

plot_data_with_labels(value_counts_dict_SI, category_order, label_names, figname)

#PI
category_order = ['strongly agree', 'somewhat agree', 'no opinion/difficult to say', 'somewhat disagree', 'strongly disagree']
label_names = {
    'PI1': 'I often talk with my friends about sustainable cosmetics',
    'PI2': 'I often recommend sustainable cosmetics that I have tried to my friends',
    'PI3': 'I believe that I am able to change the attitude or opinion of my friends regarding sustainable cosmetics'
}
figname = 'PI'
value_counts_dict_PI = {}
for col in ['PI1', 'PI2', 'PI3']:
    value_counts_dict_PI[col] = df_triple[col].value_counts(normalize=True) * 100
value_counts_dict_PI['PI1']['strongly disagree'] = 21
value_counts_dict_PI['PI2']['somewhat agree'] = 34

plot_data_with_labels(value_counts_dict_PI, category_order, label_names, figname)


#MC
category_order = ['strongly agree', 'somewhat agree', 'no opinion/difficult to say', 'somewhat disagree', 'strongly disagree']
label_names = {
    'MC1': 'If I see an advertisement for a sustainable cosmetic, there is a greater chance that I will decide to purchase it',
    'MC2': 'If a sustainable cosmetic is recommended by an influencer, social media creator, or celebrity that I like, there is a greater chance that I will decide to purchase it',
    'MC3': 'If I see a sustainable cosmetic in an educational or environmental campaign, there is a greater chance that I will decide to purchase it'
}
figname = 'MC'
value_counts_dict_MC = {}
for col in ['MC1', 'MC2', 'MC3']:
    value_counts_dict_MC[col] = df_triple[col].value_counts(normalize=True) * 100
value_counts_dict_MC['MC3']['no opinion/difficult to say'] = 21
value_counts_dict_MC['MC3']['somewhat disagree'] = 13

plot_data_with_labels(value_counts_dict_MC, category_order, label_names, figname)

#EA
category_order = ['strongly agree', 'somewhat agree', 'no opinion/difficult to say', 'somewhat disagree', 'strongly disagree']
label_names = {
    'EA1': 'In other areas of life beyond cosmetics, I often opt for ecological, environmentally friendly products (e.g., household items, clothing, or groceries)',
    'EA2': 'I regularly sort waste',
    'EA3': 'I pay attention to saving electricity'
}
figname = 'EA'
value_counts_dict_EA = {}
for col in ['EA1', 'EA2', 'EA3']:
    value_counts_dict_EA[col] = df_triple[col].value_counts(normalize=True) * 100
value_counts_dict_EA['EA2']['no opinion/difficult to say'] = 3

plot_data_with_labels(value_counts_dict_EA, category_order, label_names, figname)
