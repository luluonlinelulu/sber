# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 13:44:41 2024

@author: 11088909
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 08:55:24 2024

@author: 11088909
"""


# использую имеющийся файл df_nashdomrf.pkl
import pickle as pkl
import pandas as pd
import sqlite3


with open("df_nashdomrf.pkl", "rb") as f:
    object = pkl.load(f)
df = pd.DataFrame(object)

conn = sqlite3.connect('sql base')
df.to_sql('products', conn, if_exists='replace', index = False)

conn.commit() 
conn.close()

# Сохраняем в эксель-файл
df.to_excel('база данных по объектам.xlsx', index=False)

# Сохраняем в csv файл
df.to_csv('база данных по объектам.csv', index=False)

