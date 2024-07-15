

import pickle as pkl
import pandas as pd
import matplotlib.pyplot as plt
with open("df_nashdomrf.pkl", "rb") as f:
    
    object = pkl.load(f)
df = pd.DataFrame(object)

b=(pd.DataFrame({'count' : df.groupby( ["region"] ).size()}).reset_index())

df = pd.DataFrame(b, columns=['region', 'count'])


fig, ax = plt.subplots(figsize=(20,20))

bars = plt.barh(df['region'], df['count'])
y_labels=df['region']
ax.bar_label(bars)
plt.title('Кол-во объектов по регионам')
plt.xlabel('Кол-во объектов') #Подпись для оси х
plt.ylabel('Номер региона') #Подпись для оси y
plt.yticks(df['region'])
plt.show()


