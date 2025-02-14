import pandas as pd
import matplotlib.pyplot as plt
from textwrap import wrap
from matplotlib.cm import Greens
import numpy as np

df = pd.read_csv('survey.csv')
df = df.drop(columns = ['Sygnatura czasowa'])
df_num = df

# Numerical dataframe for correlations

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

# Columns to compare

columns_names = ['D1', 'D2', 'D3', 'D4', 'D5', 'S1', 'F1', 'F2', 'F3', 'F4', 'F5', 'MC1', 'MC2', 'MC3', 'PI1', 'PI2', 'PI3', 'SI1', 'SI2', 'SI3', 'IB1', 'EA1', 'EA2', 'EA3']

# srednia pytan MC, PI, SI, EA
    
df_num['SI1'] = df_num['SI1'].replace([1, 2, 3, 4, 5], [-5, -4, -3, -2, -1])
df_num['SI2'] = df_num['SI2'].replace([1, 2, 3, 4, 5], [-5, -4, -3, -2, -1])
df_num['SI3'] = df_num['SI3'].replace([1, 2, 3, 4, 5], [-5, -4, -3, -2, -1])

for var in ['MC', 'PI', 'EA', 'SI']:
    mean_values = df_num[[f'{var}1', f'{var}2', f'{var}3']].mean(axis=1)
    var_last_index = df_num.columns.get_loc(f'{var}3')
    df_num.insert(var_last_index + 1, var, mean_values)

df_num = df_num.append(df_num.mean(), ignore_index=True)
    
# Parameters:
# each agents': PI, SI, EA, MC? should MC be per agent or different MC for 3 types of extrenal factors

df2 = df_num[['PI', 'SI']]
df2 = df2.dropna()
df2['status'] = df2[['SI', 'PI']].sum(axis=1).round()


status_counts = df2['status'].value_counts()

percentage = ((status_counts / status_counts.sum()) * 100).round(1)
status_df = pd.DataFrame({'count': status_counts, 'percentage': percentage})

red_count = df['S1'].value_counts()
percentage_red = ((red_count / red_count.sum()) * 100).round(1)