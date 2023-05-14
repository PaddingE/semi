import pandas as pd

dict_data = {'수학': [90,80,70,], '영어': [98,89,95],
             '음악': [85,95,100], '체육': [100,90,90]}

df_data = pd.DataFrame(dict_data, index = ['서준', '우현', '인아'])

print(df_data)
print()

label1 = df_data.loc['서준']
position1 = df_data.iloc[0]

print(label1)
print()

print(position1)
print()

label2 = df_data.loc[['서준', '우현']]
position2 = df_data.iloc[[0,1]]

print(label2)
print()

print(position2)
print()

label3 = df_data.loc['서준':'우현']
position3 = df_data.iloc[0:1]

print(label3)
print()

print(position3)
print()