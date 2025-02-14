import pandas as pd
import matplotlib.pyplot as plt
from textwrap import wrap
from matplotlib.cm import Greens
import numpy as np

df = pd.read_csv('survey.csv')
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

