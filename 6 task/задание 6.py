
#Задача 1 Загрузка DataFrame

import pandas as pd 
 
# assign data of lists. 
data = {'Показатель': ['pH ', 'Цветность ', 'Жёсткость ', 'Аммиак и аммоний-ион (по азоту) ', 'Нитриты (по NO2) ',
   'Нитраты (по NO3) ', 'Фосфаты (P) ', 'Хлориды (Cl) ', 'Сульфаты (SO4) ', 'Железо (включая хлорное железо) по Fe ', 
   'Нефть ', 'Общая минерализация (сухой остаток) ', 'Окисляемость перманганатная '], 'Значение': [8.4, 0, 9.199999999999999, 0.42, 0.017, 24, 0.36, 200, 189.5, 0.019, 0.55, 590, 2], 
        'Min': [6, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  'Max': [9, 30, 10, 1.5, 3.3, 45, 3.5, 350, 500, 0.3, 0.3, 1000, 0.5] } 
 
# Create DataFrame 
df = pd.DataFrame(data) 
 
# Print the output. 

df.loc[(df["Значение"] <= df["Max"]) & (df["Значение"] >= df["Min"]), "Вывод"] = "В пределах нормы"
df.loc[(df["Значение"] < df["Min"]) | (df["Значение"] > df["Max"]), "Вывод"] = "Не соответствует норме"

display(df)
df.to_excel('Выводы.xlsx', index=False)


#Задача 2 Апельсины яблоки

# вытаскиваем первый фрукт

B1 = ["orange"]*5 + ['apple']*4
# задаем число экспериментов
n = 100000
# формируем выборку
A = pd.DataFrame({"A":list(map(lambda a: random.choice(B1), range(n)
                              ))
                 })
# считаем статистику выпадения апельсина
P_orange1 = len(A[A.A=='orange'])/A.shape[0]
P_orange1

# вытаскиваем второй фрукт
B2 = ["orange"]*4 + ['apple']*4
# задаем число экспериментов
n = 100000
# формируем выборку
A = pd.DataFrame({"A":list(map(lambda a: random.choice(B2), range(n)
                              ))
                 })
# считаем статистику выпадения апельсина
P_orange2 = len(A[A.A=='orange'])/A.shape[0]

# вытаскиваем третий фрукт
B3 = ["orange"]*3 + ['apple']*4
# задаем число экспериментов
n = 100000
# формируем выборку
A = pd.DataFrame({"A":list(map(lambda a: random.choice(B3), range(n)
                              ))
                 })

# считаем статистику выпадения апельсина
P_orange3 = len(A[A.A=='orange'])/A.shape[0]
# считаем вероятность, что все три фрукта апельсины
P_orange=P_orange1*P_orange2*P_orange3
P_orange

#Задача 3 Мастер

# проверяем первую деталь

B1 = ["standart"]*7 + ['nestandart']*3
# задаем число экспериментов
n = 100000
# формируем выборку
A = pd.DataFrame({"A":list(map(lambda a: random.choice(B1), range(n)
                              ))
                 })
# считаем статистику выпадения нестандартной детали
P_nestandart1 = len(A[A.A=='nestandart'])/A.shape[0]


# проверяем вторую деталь
B2 =  ["standart"]*7 + ['nestandart']*2
# задаем число экспериментов
n = 100000
# формируем выборку
A = pd.DataFrame({"A":list(map(lambda a: random.choice(B2), range(n)
                              ))
                 })
# считаем статистику выпадений черных шаров
P_standart2 = len(A[A.A=='standart'])/A.shape[0]


# считаем вероятность, что на этом проверка закончена
P_2=P_nestandart1*P_standart2
P_2



























