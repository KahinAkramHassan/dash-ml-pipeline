
import pandas as pd
import numpy as np


df_02_intermediate = pd.read_csv('../data/02_intermediate_cleaned_data.csv')
df_02_intermediate_mean = df_02_intermediate.groupby(['Year']).mean().reset_index()

year_all = [*['All'], *df_02_intermediate['Year'].unique()]
commodity_all = df_02_intermediate.filter(regex='kilo').columns
commodity_all_infl = df_02_intermediate.filter(regex='infl').columns

df_02_intermediate_grouped = df_02_intermediate.groupby('Year')

years_between = f'{df_02_intermediate["Year"].min()}-{df_02_intermediate["Year"].max()}'
price_rice_avg = f'{np.round(df_02_intermediate["Price_rice_kilo"].mean(),2)}'
price_beef_avg = f'{np.round(df_02_intermediate["Price_beef_kilo"].mean(),2)}'
price_coffee_avg = f'{np.round(df_02_intermediate["Price_coffee_kilo"].mean(),2)}'
