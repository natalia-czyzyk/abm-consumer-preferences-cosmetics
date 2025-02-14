# Combined Python Script for Data Analysis and Modeling
# This script includes:
# 1. Exploratory Data Analysis (EDA)
# 2. Statistical Analysis
# 3. Data Visualization (Plots)
# 4. Correlation Analysis
# 5. Model Parameters & Training

# -------------------------------
# SECTION 1: EXPLORATORY DATA ANALYSIS (EDA)
# -------------------------------

import pandas as pd
import pandas as pd

df = pd.read_csv('data.csv')
df = df.drop(columns = ['Sygnatura czasowa'])
df_num = df

# Numerical dataframe for correlations

df_num.columns = ['D1', 'D2', 'D3', 'D4', 'D5', 'S1', 'A1', 'F1', 'F2', 'F3', 'F4', 'F5', 'MC1', 'MC2', 'MC3', 'PI1', 'PI2', 'PI3', 'SI1', 'SI2', 'SI3', 'IB1', 'EA1', 'EA2', 'EA3', 'R1']
df_num['D1'] = df_num['D1'].replace(['kobieta', 'mężczyzna', 'inne/nie chcę podawać'], [1, 3, 2])
df_num = df_num.replace(['20 i poniżej', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51 i powyżej'], [1, 2, 3, 4, 5, 6, 7, 8])
df_num = df_num.replace(['wieś', 'miejscowość do 100 tys. mieszkańców', 'miejscowość do 250 tys. mieszkańców', 'miejscowość do 500 tys. mieszkańców', 'miejscowość powyżej 500 tys. mieszkańców'], [1, 2, 3, 4, 5])
df_num = df_num.replace(['podstawowe', 'zasadnicze zawodowe', 'średnie', 'wyższe', 'inne/nie chcę podawać'], [2, 3, 4, 5, 1])
df_num = df_num.replace(['3000 i poniżej', '3001 - 4000', '4001 - 5000', '5001 - 6000', '6001 - 7000', '7001 i powyżej', 'nie chcę podawać'], [2, 3, 4, 5, 6, 7, 1])
df_num = df_num.replace(['tak', 'nie'], [1, 2])
df_num = df_num.replace(['bardzo ważne', 'ważne', 'średnio ważne', 'trochę ważne', 'w ogóle nieważne'], [5, 4, 3, 2, 1])
#df_num = df_num.replace(['bio (min. 50% składników z upraw biologicznych)', 'cruelty-free (nietestowane na zwierzętach)', 'carbon-neutral (o neutralnym śladzie węglowym)', 'ekologiczne', 'fair-trade (sprawiedliwy handel)', 'naturalne (min. 95% składników pochodzenia naturalnego)', 'opakowanie z recyklingu', 'organiczne (min. 95% składników pochodzenia naturalnego i z upraw ekologicznych)', 'wegańskie', 'zero-waste (zero odpadów)'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
df_num = df_num.replace(['zdecydowanie się zgadzam', 'raczej się zgadzam', 'nie mam zdania/trudno powiedzieć', 'raczej się nie zgadzam', 'zdecydowanie się nie zgadzam'], [5, 4, 3, 2, 1])
#df_num = df_num.replace(['zbyt wysoka cena', 'niska dostępność w sklepach stacjonarnych', 'brak dostrzegalnej różnicy w porównaniu z konwencjonalnymi kosmetykami', 'krótki okres przydatności do użycia', 'niski stopień wiedzy na temat kosmetyków zrównoważonych'], [1, 2, 3, 4, 5])

columns_names = ['D1', 'D2', 'D3', 'D4', 'D5', 'S1', 'F1', 'F2', 'F3', 'F4', 'F5', 'MC1', 'MC2', 'MC3', 'PI1', 'PI2', 'PI3', 'SI1', 'SI2', 'SI3', 'IB1', 'EA1', 'EA2', 'EA3']


# Metrics (count, avg, median, std)

df = df_num
column_status = {}

for column in df.columns:
    # Count the frequency of each unique value in the column
    value_counts = df[column].value_counts().to_dict()
    
    # Store the frequency counts in the dictionary
    column_status[column] = value_counts



# -------------------------------
# SECTION 2: DATA VISUALIZATION (PLOTS)
# -------------------------------

import matplotlib.pyplot as plt
from textwrap import wrap
from matplotlib.cm import Greens
import numpy as np

df = pd.read_csv('data.csv')
df = df.drop(columns = ['Sygnatura czasowa'])
df_num = df
df_pl = df

# Dataframe for the plots

df.columns = ['D1', 'D2', 'D3', 'D4', 'D5', 'S1', 'A1', 'F1', 'F2', 'F3', 'F4', 'F5', 'MC1', 'MC2', 'MC3', 'PI1', 'PI2', 'PI3', 'SI1', 'SI2', 'SI3', 'IB1', 'EA1', 'EA2', 'EA3', 'R1']
df = df.replace(['kobieta', 'mężczyzna', 'inne/nie chcę podawać'], ['female', 'male', 'other/prefer not to disclose'])
df = df.replace(['20 i poniżej', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51 i powyżej'], ['20 and below', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51 and above'])
df = df.replace(['wieś', 'miejscowość do 100 tys. mieszkańców', 'miejscowość do 250 tys. mieszkańców', 'miejscowość do 500 tys. mieszkańców', 'miejscowość powyżej 500 tys. mieszkańców'], ['village', 'city up to 100k inhabitants', 'city up to 250k inhabitants', 'city up to 500k inhabitants', 'city above 500k inhabitants'])
df = df.replace(['podstawowe', 'zasadnicze zawodowe', 'średnie', 'wyższe', 'inne/nie chcę podawać'], ['primary', 'other/prefer not to disclose', 'secondary', 'higher', 'other/prefer not to disclose'])
df = df.replace(['3000 i poniżej', '3001 - 4000', '4001 - 5000', '5001 - 6000', '6001 - 7000', '7001 i powyżej', 'nie chcę podawać'], ['3000 and below', '3001 - 4000', '4001 - 5000', '5001 - 6000', '6001 - 7000', '7001 and above', 'prefer not to disclose'])
df = df.replace(['tak', 'nie'], ['yes', 'no'])
df = df.replace(['bardzo ważne', 'ważne', 'średnio ważne', 'trochę ważne', 'w ogóle nieważne'], ['very important', 'important', 'somewhat important', 'slightly important', 'not important at all'])
df = df.replace(['zdecydowanie się zgadzam', 'raczej się zgadzam', 'nie mam zdania/trudno powiedzieć', 'raczej się nie zgadzam', 'zdecydowanie się nie zgadzam'], ['strongly agree', 'somewhat agree', 'no opinion / hard to say', 'somewhat disagree', 'strongly disagree'])

df.loc[128,'F1'] = 'slightly important'
df.loc[121,'F2'] = 'slightly important'

replacement_dict = {
    'bio (min. 50% składników z upraw biologicznych)': 'bio',
    'cruelty-free (nietestowane na zwierzętach)': 'cruelty-free',
    'carbon-neutral (o neutralnym śladzie węglowym)': 'carbon-neutral',
    'ekologiczne': 'ecological',
    'fair-trade (sprawiedliwy handel)': 'fair-trade',
    'naturalne (min. 95% składników pochodzenia naturalnego)': 'natural',
    'opakowanie z recyklingu': 'recyclable packaging',
    'organiczne (min. 95% składników pochodzenia naturalnego i z upraw ekologicznych)': 'organic',
    'wegańskie': 'vegan',
    'zero-waste (zero odpadów)': 'zero-waste',
    'zbyt wysoka cena': 'too expensive',
    'niska dostępność w sklepach stacjonarnych': 'low availability in stationary stores',
    'brak dostrzegalnej różnicy w porównaniu z konwencjonalnymi kosmetykami': 'lack of noticeable difference compared to conventional cosmetics',
    'krótki okres przydatności do użycia': 'short shelf life',
    'niski stopień wiedzy na temat kosmetyków zrównoważonych': 'low level of knowledge about sustainable cosmetics'
}

# Plots without A1, R1, D4, EA2, EA3

plot_names = ['D1', 'D2', 'D3', 'D5', 'S1', 'F1', 'F2', 'F3', 'F4', 'F5', 'MC1', 'MC2', 'MC3', 'PI1', 'PI2', 'PI3', 'SI1', 'SI2', 'SI3', 'IB1', 'EA1']
num_answers = np.array([3, 8, 5, 7, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])

for i in plot_names:
    plt.figure(figsize=(8, 6))
    num_colors = num_answers[plot_names.index(i)]
    colors = Greens(np.linspace(0.4, 0.8, num_colors))
    font_plot = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 20}
    counts = df[i].value_counts()
    wrapped_labels = [ '\n'.join(wrap(label, 15)) for label in counts.index]
    plt.pie(counts, labels=wrapped_labels, colors=colors, autopct='%1.0f%%', textprops=font_plot)
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(f'{i}.png', bbox_inches='tight')
    plt.show()
    
# Plots for D4, EA2, EA3

plot_names_2 = ['D4', 'EA2', 'EA3']
num_answers_2 = np.array([4, 5, 5])

for i in plot_names_2:
    plt.figure(figsize=(8, 6))
    num_colors = num_answers_2[plot_names_2.index(i)]
    colors = Greens(np.linspace(0.4, 0.8, num_colors))
    font_plot = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 18}
    counts = df[i].value_counts()
    plt.pie(counts, labels=counts.index, colors=colors, autopct='%1.0f%%', textprops=font_plot)
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(f'{i}.png', bbox_inches='tight')
    plt.show()


# Data cleaning for A1

elements_A1 = []

A1_values = df['A1'].dropna()
A1_values = A1_values.reset_index(drop=True)

for i in range(len(A1_values)):
    element = A1_values[i]
    element_split = element.split(', ')
    elements_A1.append(element_split)
    
flat_elements_A1 = []

for sublist in elements_A1:
    for item in sublist:
        flat_elements_A1.append(item)
        
flat_elements_A1_a = [replacement_dict.get(item, item) for item in flat_elements_A1]
unique_A1 = set(flat_elements_A1_a)

element_count = len(A1_values)
percentage_A1 = {element: (flat_elements_A1_a.count(element) / element_count) * 100 for element in unique_A1}
        
# Plot for A1

plt.figure(figsize=(8, 6))
font_plot = {'family': 'serif', 'color': 'black', 'weight': 'normal', 'size': 18}
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12

unique_values = list(unique_A1)
counts = [percentage_A1[value] for value in unique_values]

sorted_data = sorted(zip(unique_values, counts), key=lambda x: x[1], reverse=False)
unique_values, counts = zip(*sorted_data)

wrapped_labels = ['\n'.join(wrap(label, 30)) for label in unique_values]
bars = plt.barh(wrapped_labels, counts, color=Greens(0.7))

plt.xlabel('Frequency [%]', fontdict=font_plot)

label_margin = max(counts) * 0.02 
for i, count in enumerate(counts):
    rounded_count = round(count)
    plt.text(rounded_count + label_margin, i, f"{rounded_count}%", va='center', fontdict=font_plot)
  
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

plt.tight_layout()
plt.savefig('A1.png', bbox_inches='tight')
plt.show()
    
# Data cleaning for R1

elements_R1 = []

R1_values = df['R1'].dropna()
R1_values = R1_values.reset_index(drop=True)

for i in range(len(R1_values)):
    element = R1_values[i]
    element_split = element.split(', ')
    elements_R1.append(element_split)
    
flat_elements_R1 = []


for sublist in elements_R1:
    for item in sublist:
        flat_elements_R1.append(item)
        
flat_elements_R1_a = [replacement_dict.get(item, item) for item in flat_elements_R1]
        
unique_R1 = set(flat_elements_R1_a)

element_count = len(R1_values)
percentage_R1 = {element: (flat_elements_R1_a.count(element) / element_count) * 100 for element in unique_R1}


# Plot for R1

plt.figure(figsize=(8, 6))
font_plot = {'family': 'serif', 'color': 'black', 'weight': 'normal', 'size': 18}
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12

unique_values = list(unique_R1)
counts = [percentage_R1[value] for value in unique_values]

sorted_data = sorted(zip(unique_values, counts), key=lambda x: x[1], reverse=False)
unique_values, counts = zip(*sorted_data)

wrapped_labels = ['\n'.join(wrap(label, 30)) for label in unique_values]
bars = plt.barh(wrapped_labels, counts, color=Greens(0.7))

plt.xlabel('Frequency [%]', fontdict=font_plot)

label_margin = max(counts) * 0.02  # Adjust as needed
for i, count in enumerate(counts):
    rounded_count = round(count)
    plt.text(rounded_count + label_margin, i, f"{rounded_count}%", va='center', fontdict=font_plot)

    
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
    
plt.tight_layout()
plt.savefig('R1.png', bbox_inches='tight')
plt.show()


from matplotlib.cm import Greens

# Create a dictionary for the data
data = {
    "Tested parameter": [
        "num-agents", "num-agents", "num-agents", "num-agents",
        "Percentage of influencers [%]", "Percentage of influencers [%]", "Percentage of influencers [%]", "Percentage of influencers [%]", "Percentage of influencers [%]",
        "Price", "Price", "Price", "Price", "Price",
        "Quality", "Quality", "Quality", "Quality", "Quality",
        "Attribute value", "Attribute value", "Attribute value", "Attribute value", "Attribute value", "Attribute value", "Attribute value",
        "campaign-freq", "campaign-freq", "campaign-freq", "campaign-freq",
        "Reach of campaigns [%]", "Reach of campaigns [%]", "Reach of campaigns [%]", "Reach of campaigns [%]", "Reach of campaigns [%]"
    ],
    "Parameter value": [
        250, 500, 750, 1000,
        1, 2, 3, 4, 5,
        20, 40, 60, 80, 100,
        20, 40, 60, 80, 100,
        33, 44, 55, 66, 77, 88, 99,
        500, 1000, 2500, 5000,
        2, 4, 6, 8, 10
    ],
    "% of green": [
        10.49, 22.02, 30.5, 37.28,
        8.24, 15.54, 22.15, 27.07, 31.82,
        18.82, 20.69, 22.76, 26.76, 28.33,
        18.79, 20.18, 22.74, 26.99, 26.96,
        19.13, 21.47, 22.68, 23.19, 24.63, 27.06, 28.01,
        31.5, 24.95, 21.82, 21.71,
        21.71, 21.75, 22.3, 21.99, 22.91
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define markers and marker size
markers = ['o', 's', '^', 'D', 'v', 'p', '*', 'h', 'x']
marker_size = 170

# Define font properties
font_properties = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 18}

# Plot 1: num-agents
fig, ax = plt.subplots(figsize=(8, 6))
subset1 = df[df["Tested parameter"] == "num-agents"]
for i, param in enumerate(subset1["Tested parameter"].unique()):
    subset = subset1[subset1["Tested parameter"] == param]
    ax.scatter(subset["Parameter value"], subset["% of green"], marker=markers[i % len(markers)], s=marker_size, color=Greens(0.7), label=f"{param} - % of green", zorder=5)

ax.set_xlabel("Number of agents", fontdict=font_properties)
ax.set_ylabel("Percentage of green agents [%]", fontdict=font_properties)
#ax.set_title("% of Green by Tested Parameter (num-agents)", fontdict=font_properties)
#ax.legend()
ax.tick_params(axis='both', which='major', labelsize=14)
ax.grid(True)
plt.tight_layout()
plt.savefig('num_agents.png')
plt.show()
plt.close()

# Plot 2: %-of-influencers, campaign-reach
fig, ax = plt.subplots(figsize=(8, 6))
subset2 = df[df["Tested parameter"].isin(["Percentage of influencers [%]", "Reach of campaigns [%]"])]
for i, param in enumerate(subset2["Tested parameter"].unique()):
    subset = subset2[subset2["Tested parameter"] == param]
    ax.scatter(subset["Parameter value"], subset["% of green"], marker=markers[i % len(markers)], s=marker_size, color=Greens(0.7), label=f"{param}",zorder=5)

ax.set_xlabel("Parameter value", fontdict=font_properties)
ax.set_ylabel("Percentage of green agents [%]", fontdict=font_properties)
#ax.set_title("% of Green by Tested Parameter (%-of-influencers, campaign-reach)", fontdict=font_properties)
ax.legend(prop={'size': 16})
ax.tick_params(axis='both', which='major', labelsize=14)
ax.grid(True)
plt.tight_layout()
plt.savefig('influencers_campaign_reach.png')
plt.show()
plt.close()

# Plot 3: price, quality, attr-value
fig, ax = plt.subplots(figsize=(8, 6))
subset3 = df[df["Tested parameter"].isin(["Price", "Quality", "Attribute value"])]
for i, param in enumerate(subset3["Tested parameter"].unique()):
    subset = subset3[subset3["Tested parameter"] == param]
    ax.scatter(subset["Parameter value"], subset["% of green"], marker=markers[i % len(markers)], s=marker_size, color=Greens(0.7), label=f"{param}",zorder=5)

ax.set_xlabel("Parameter value", fontdict=font_properties)
ax.set_ylabel("Percentage of green agents [%]", fontdict=font_properties)
#ax.set_title("% of Green by Tested Parameter (price, quality, attr-value)", fontdict=font_properties)
ax.legend(prop={'size': 16})
ax.tick_params(axis='both', which='major', labelsize=14)
ax.grid(True)
plt.tight_layout()
plt.savefig('price_quality_attr_value.png')
plt.show()
plt.close()

# Plot 4: campaign-freq
fig, ax = plt.subplots(figsize=(8, 6))
subset4 = df[df["Tested parameter"] == "campaign-freq"]
for i, param in enumerate(subset4["Tested parameter"].unique()):
    subset = subset4[subset4["Tested parameter"] == param]
    ax.scatter(subset["Parameter value"], subset["% of green"], marker=markers[i % len(markers)], s=marker_size, color=Greens(0.7), label=f"{param} - % of green",zorder=5)

ax.set_xlabel("Frequency of campaigns", fontdict=font_properties)
ax.set_ylabel("Percentage of green agents [%]", fontdict=font_properties)
#ax.set_title("% of Green by Tested Parameter (campaign-freq)", fontdict=font_properties)
#ax.legend()
ax.tick_params(axis='both', which='major', labelsize=14)
ax.grid(True)
plt.tight_layout()
plt.savefig('campaign_freq.png')
plt.show()
plt.close()


from textwrap import wrap
from datetime import datetime

df = pd.read_csv('data.csv')
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


# -------------------------------
# SECTION 3: CORRELATION ANALYSIS
# -------------------------------

df = pd.read_csv('data.csv')
df = df.drop(columns = ['Sygnatura czasowa'])
df_num = df

# Numerical dataframe for correlations

df_num.columns = ['D1', 'D2', 'D3', 'D4', 'D5', 'S1', 'A1', 'F1', 'F2', 'F3', 'F4', 'F5', 'MC1', 'MC2', 'MC3', 'PI1', 'PI2', 'PI3', 'SI1', 'SI2', 'SI3', 'IB1', 'EA1', 'EA2', 'EA3', 'R1']
df_num['D1'] = df_num['D1'].replace(['kobieta', 'mężczyzna', 'inne/nie chcę podawać'], [1, 3, 2])
df_num = df_num.replace(['20 i poniżej', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51 i powyżej'], [1, 2, 3, 4, 5, 6, 7, 8])
df_num = df_num.replace(['wieś', 'miejscowość do 100 tys. mieszkańców', 'miejscowość do 250 tys. mieszkańców', 'miejscowość do 500 tys. mieszkańców', 'miejscowość powyżej 500 tys. mieszkańców'], [1, 2, 3, 4, 5])
df_num = df_num.replace(['podstawowe', 'zasadnicze zawodowe', 'średnie', 'wyższe', 'inne/nie chcę podawać'], [2, 3, 4, 5, 1])
df_num = df_num.replace(['3000 i poniżej', '3001 - 4000', '4001 - 5000', '5001 - 6000', '6001 - 7000', '7001 i powyżej', 'nie chcę podawać'], [2, 3, 4, 5, 6, 7, 1])
df_num = df_num.replace(['tak', 'nie'], [1, 2])
df_num = df_num.replace(['bardzo ważne', 'ważne', 'średnio ważne', 'trochę ważne', 'w ogóle nieważne'], [5, 4, 3, 2, 1])
#df_num = df_num.replace(['bio (min. 50% składników z upraw biologicznych)', 'cruelty-free (nietestowane na zwierzętach)', 'carbon-neutral (o neutralnym śladzie węglowym)', 'ekologiczne', 'fair-trade (sprawiedliwy handel)', 'naturalne (min. 95% składników pochodzenia naturalnego)', 'opakowanie z recyklingu', 'organiczne (min. 95% składników pochodzenia naturalnego i z upraw ekologicznych)', 'wegańskie', 'zero-waste (zero odpadów)'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
df_num = df_num.replace(['zdecydowanie się zgadzam', 'raczej się zgadzam', 'nie mam zdania/trudno powiedzieć', 'raczej się nie zgadzam', 'zdecydowanie się nie zgadzam'], [5, 4, 3, 2, 1])
#df_num = df_num.replace(['zbyt wysoka cena', 'niska dostępność w sklepach stacjonarnych', 'brak dostrzegalnej różnicy w porównaniu z konwencjonalnymi kosmetykami', 'krótki okres przydatności do użycia', 'niski stopień wiedzy na temat kosmetyków zrównoważonych'], [1, 2, 3, 4, 5])

columns_names = ['D1', 'D2', 'D3', 'D4', 'D5', 'S1', 'F1', 'F2', 'F3', 'F4', 'F5', 'MC1', 'MC2', 'MC3', 'PI1', 'PI2', 'PI3', 'SI1', 'SI2', 'SI3', 'IB1', 'EA1', 'EA2', 'EA3']

# Pearson correlation

corr_data = []

for i in range(len(columns_names)):
    for j in range(len(columns_names)):
        x = df_num[columns_names[i]]
        y = df_num[columns_names[j]]
        correlation = x.corr(y)
        corr_data.append({'x': columns_names[i], 'y': columns_names[j], 'corr': correlation})

corr_df = pd.DataFrame(corr_data)


# Kendall correlation

corr_data_kn = []

for i in range(len(columns_names)):
    for j in range(len(columns_names)):
        x = df_num[columns_names[i]]
        y = df_num[columns_names[j]]
        correlation = x.corr(y, method='kendall')
        corr_data_kn.append({'x': columns_names[i], 'y': columns_names[j], 'corr': correlation})

corr_df_kn = pd.DataFrame(corr_data_kn)
    
#same results, for Spearman as well


# -------------------------------
# SECTION 4: MODEL PARAMETERS & TRAINING
# -------------------------------

df = pd.read_csv('data.csv')
df = df.drop(columns = ['Sygnatura czasowa'])
df_num = df

# Explanatory data analysis + dataframe

df_num.columns = ['D1', 'D2', 'D3', 'D4', 'D5', 'S1', 'A1', 'F1', 'F2', 'F3', 'F4', 'F5', 'MC1', 'MC2', 'MC3', 'PI1', 'PI2', 'PI3', 'SI1', 'SI2', 'SI3', 'IB1', 'EA1', 'EA2', 'EA3', 'R1']
df_num['D1'] = df_num['D1'].replace(['kobieta', 'mężczyzna', 'inne/nie chcę podawać'], [1, 3, 2])
df_num = df_num.replace(['20 i poniżej', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51 i powyżej'], [1, 2, 3, 4, 5, 6, 7, 8])
df_num = df_num.replace(['wieś', 'miejscowość do 100 tys. mieszkańców', 'miejscowość do 250 tys. mieszkańców', 'miejscowość do 500 tys. mieszkańców', 'miejscowość powyżej 500 tys. mieszkańców'], [1, 2, 3, 4, 5])
df_num = df_num.replace(['podstawowe', 'zasadnicze zawodowe', 'średnie', 'wyższe', 'inne/nie chcę podawać'], [2, 4, 4, 5, 1])
df_num = df_num.replace(['3000 i poniżej', '3001 - 4000', '4001 - 5000', '5001 - 6000', '6001 - 7000', '7001 i powyżej', 'nie chcę podawać'], [2, 3, 4, 5, 6, 7, 1])
df_num = df_num.replace(['tak', 'nie'], [1, 2])
df_num = df_num.replace(['bardzo ważne', 'ważne', 'średnio ważne', 'trochę ważne', 'w ogóle nieważne'], [5, 4, 3, 2, 1])
#df_num = df_num.replace(['bio (min. 50% składników z upraw biologicznych)', 'cruelty-free (nietestowane na zwierzętach)', 'carbon-neutral (o neutralnym śladzie węglowym)', 'ekologiczne', 'fair-trade (sprawiedliwy handel)', 'naturalne (min. 95% składników pochodzenia naturalnego)', 'opakowanie z recyklingu', 'organiczne (min. 95% składników pochodzenia naturalnego i z upraw ekologicznych)', 'wegańskie', 'zero-waste (zero odpadów)'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
df_num = df_num.replace(['zdecydowanie się zgadzam', 'raczej się zgadzam', 'nie mam zdania/trudno powiedzieć', 'raczej się nie zgadzam', 'zdecydowanie się nie zgadzam'], [5, 4, 3, 2, 1])
#df_num = df_num.replace(['zbyt wysoka cena', 'niska dostępność w sklepach stacjonarnych', 'brak dostrzegalnej różnicy w porównaniu z konwencjonalnymi kosmetykami', 'krótki okres przydatności do użycia', 'niski stopień wiedzy na temat kosmetyków zrównoważonych'], [1, 2, 3, 4, 5])

columns_names = ['D1', 'D2', 'D3', 'D4', 'D5', 'S1', 'F1', 'F2', 'F3', 'F4', 'F5', 'MC1', 'MC2', 'MC3', 'PI1', 'PI2', 'PI3', 'SI1', 'SI2', 'SI3', 'IB1', 'EA1', 'EA2', 'EA3']


# Average of questions MC, PI, SI, EA
    
df_num['SI1'] = df_num['SI1'].replace([1, 2, 3, 4, 5], [-5, -4, -3, -2, -1])
df_num['SI2'] = df_num['SI2'].replace([1, 2, 3, 4, 5], [-5, -4, -3, -2, -1])
df_num['SI3'] = df_num['SI3'].replace([1, 2, 3, 4, 5], [-5, -4, -3, -2, -1])

for var in ['MC', 'PI', 'EA', 'SI']:
    mean_values = df_num[[f'{var}1', f'{var}2', f'{var}3']].mean(axis=1)
    var_last_index = df_num.columns.get_loc(f'{var}3')
    df_num.insert(var_last_index + 1, var, mean_values)

#df_num.loc['mean'] = df_num.mean()


# Parameters PI (power to influence) and SI (susceptibility to be influenced)

df2 = df_num[['PI', 'SI']]
df2 = df2.dropna()
df2['status'] = df2[['SI', 'PI']].sum(axis=1).round()

status_counts = df2['status'].value_counts()

percentage = ((status_counts / status_counts.sum()) * 100).round(1)
status_df = pd.DataFrame({'count': status_counts, 'percentage': percentage})

red_count = df['S1'].value_counts()
percentage_red = ((red_count / red_count.sum()) * 100).round(1)

'''
df_num.columns = ['D1', 'D2', 'D3', 'D4', 'D5', 'S1', 'A1', 'F1', 'F2', 'F3', 'F4', 'F5', 'MC1', 'MC2', 'MC3', 'PI1', 'PI2', 'PI3', 'SI1', 'SI2', 'SI3', 'IB1', 'EA1', 'EA2', 'EA3', 'R1']
df_num['D1'] = df_num['D1'].replace(['kobieta', 'mężczyzna', 'inne/nie chcę podawać'], [1, 3, 2])
df_num = df_num.replace(['20 i poniżej', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51 i powyżej'], [1, 2, 3, 4, 5, 6, 7, 8])
df_num = df_num.replace(['wieś', 'miejscowość do 100 tys. mieszkańców', 'miejscowość do 250 tys. mieszkańców', 'miejscowość do 500 tys. mieszkańców', 'miejscowość powyżej 500 tys. mieszkańców'], [1, 2, 3, 4, 5])
df_num = df_num.replace(['podstawowe', 'zasadnicze zawodowe', 'średnie', 'wyższe', 'inne/nie chcę podawać'], [2, 3, 4, 5, 1])
df_num = df_num.replace(['3000 i poniżej', '3001 - 4000', '4001 - 5000', '5001 - 6000', '6001 - 7000', '7001 i powyżej', 'nie chcę podawać'], [2, 3, 4, 5, 6, 7, 1])
df_num = df_num.replace(['tak', 'nie'], [1, 2])
df_num = df_num.replace(['bardzo ważne', 'ważne', 'średnio ważne', 'trochę ważne', 'w ogóle nieważne'], [5, 4, 3, 2, 1])
#df_num = df_num.replace(['bio (min. 50% składników z upraw biologicznych)', 'cruelty-free (nietestowane na zwierzętach)', 'carbon-neutral (o neutralnym śladzie węglowym)', 'ekologiczne', 'fair-trade (sprawiedliwy handel)', 'naturalne (min. 95% składników pochodzenia naturalnego)', 'opakowanie z recyklingu', 'organiczne (min. 95% składników pochodzenia naturalnego i z upraw ekologicznych)', 'wegańskie', 'zero-waste (zero odpadów)'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
df_num = df_num.replace(['zdecydowanie się zgadzam', 'raczej się zgadzam', 'nie mam zdania/trudno powiedzieć', 'raczej się nie zgadzam', 'zdecydowanie się nie zgadzam'], [5, 4, 3, 2, 1])
#df_num = df_num.replace(['zbyt wysoka cena', 'niska dostępność w sklepach stacjonarnych', 'brak dostrzegalnej różnicy w porównaniu z konwencjonalnymi kosmetykami', 'krótki okres przydatności do użycia', 'niski stopień wiedzy na temat kosmetyków zrównoważonych'], [1, 2, 3, 4, 5])
 df_num.columns = ['D1', 'D2', 'D3', 'D4', 'D5', 'S1', 'A1', 'F1', 'F2', 'F3', 'F4', 'F5', 'MC1', 'MC2', 'MC3', 'PI1', 'PI2', 'PI3', 'SI1', 'SI2', 'SI3', 'IB1', 'EA1', 'EA2', 'EA3', 'R1']
df_num['D1'] = df_num['D1'].replace(['kobieta', 'mężczyzna', 'inne/nie chcę podawać'], [1, 3, 2])
df_num = df_num.replace(['20 i poniżej', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51 i powyżej'], [1, 2, 3, 4, 5, 6, 7, 8])
df_num = df_num.replace(['wieś', 'miejscowość do 100 tys. mieszkańców', 'miejscowość do 250 tys. mieszkańców', 'miejscowość do 500 tys. mieszkańców', 'miejscowość powyżej 500 tys. mieszkańców'], [1, 2, 3, 4, 5])
df_num = df_num.replace(['podstawowe', 'zasadnicze zawodowe', 'średnie', 'wyższe', 'inne/nie chcę podawać'], [2, 3, 4, 5, 1])
df_num = df_num.replace(['3000 i poniżej', '3001 - 4000', '4001 - 5000', '5001 - 6000', '6001 - 7000', '7001 i powyżej', 'nie chcę podawać'], [2, 3, 4, 5, 6, 7, 1])
df_num = df_num.replace(['tak', 'nie'], [1, 2])
df_num = df_num.replace(['bardzo ważne', 'ważne', 'średnio ważne', 'trochę ważne', 'w ogóle nieważne'], [5, 4, 3, 2, 1])
#df_num = df_num.replace(['bio (min. 50% składników z upraw biologicznych)', 'cruelty-free (nietestowane na zwierzętach)', 'carbon-neutral (o neutralnym śladzie węglowym)', 'ekologiczne', 'fair-trade (sprawiedliwy handel)', 'naturalne (min. 95% składników pochodzenia naturalnego)', 'opakowanie z recyklingu', 'organiczne (min. 95% składników pochodzenia naturalnego i z upraw ekologicznych)', 'wegańskie', 'zero-waste (zero odpadów)'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
df_num = df_num.replace(['zdecydowanie się zgadzam', 'raczej się zgadzam', 'nie mam zdania/trudno powiedzieć', 'raczej się nie zgadzam', 'zdecydowanie się nie zgadzam'], [5, 4, 3, 2, 1])
#df_num = df_num.replace(['zbyt wysoka cena', 'niska dostępność w sklepach stacjonarnych', 'brak dostrzegalnej różnicy w porównaniu z konwencjonalnymi kosmetykami', 'krótki okres przydatności do użycia', 'niski stopień wiedzy na temat kosmetyków zrównoważonych'], [1, 2, 3, 4, 5])
df_num.columns = ['D1', 'D2', 'D3', 'D4', 'D5', 'S1', 'A1', 'F1', 'F2', 'F3', 'F4', 'F5', 'MC1', 'MC2', 'MC3', 'PI1', 'PI2', 'PI3', 'SI1', 'SI2', 'SI3', 'IB1', 'EA1', 'EA2', 'EA3', 'R1']
df_num['D1'] = df_num['D1'].replace(['kobieta', 'mężczyzna', 'inne/nie chcę podawać'], [1, 3, 2])
df_num = df_num.replace(['20 i poniżej', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51 i powyżej'], [1, 2, 3, 4, 5, 6, 7, 8])
df_num = df_num.replace(['wieś', 'miejscowość do 100 tys. mieszkańców', 'miejscowość do 250 tys. mieszkańców', 'miejscowość do 500 tys. mieszkańców', 'miejscowość powyżej 500 tys. mieszkańców'], [1, 2, 3, 4, 5])
df_num = df_num.replace(['podstawowe', 'zasadnicze zawodowe', 'średnie', 'wyższe', 'inne/nie chcę podawać'], [2, 3, 4, 5, 1])
df_num = df_num.replace(['3000 i poniżej', '3001 - 4000', '4001 - 5000', '5001 - 6000', '6001 - 7000', '7001 i powyżej', 'nie chcę podawać'], [2, 3, 4, 5, 6, 7, 1])
df_num = df_num.replace(['tak', 'nie'], [1, 2])
df_num = df_num.replace(['bardzo ważne', 'ważne', 'średnio ważne', 'trochę ważne', 'w ogóle nieważne'], [5, 4, 3, 2, 1])
#df_num = df_num.replace(['bio (min. 50% składników z upraw biologicznych)', 'cruelty-free (nietestowane na zwierzętach)', 'carbon-neutral (o neutralnym śladzie węglowym)', 'ekologiczne', 'fair-trade (sprawiedliwy handel)', 'naturalne (min. 95% składników pochodzenia naturalnego)', 'opakowanie z recyklingu', 'organiczne (min. 95% składników pochodzenia naturalnego i z upraw ekologicznych)', 'wegańskie', 'zero-waste (zero odpadów)'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
df_num = df_num.replace(['zdecydowanie się zgadzam', 'raczej się zgadzam', 'nie mam zdania/trudno powiedzieć', 'raczej się nie zgadzam', 'zdecydowanie się nie zgadzam'], [5, 4, 3, 2, 1])
#df_num = df_num.replace(['zbyt wysoka cena', 'niska dostępność w sklepach stacjonarnych', 'brak dostrzegalnej różnicy w porównaniu z konwencjonalnymi kosmetykami', 'krótki okres przydatności do użycia', 'niski stopień wiedzy na temat kosmetyków zrównoważonych'], [1, 2, 3, 4, 5])
'''
