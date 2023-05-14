import pandas as pd

dict_data = {'수학': [90,80,70,], '영어': [98,89,95],
             '음악': [85,95,100], '체육': [100,90,90]}

df_data = pd.DataFrame(dict_data, index = ['서준', '우현', '인아'])

print(df_data)
print()

df_data2 = df_data.copy()
df_data3 = df_data.copy()

df_data2.drop('수학', axis = 1, inplace= True)
df_data3.drop(['영어', '음악'], axis = 1, inplace= True)

print(df_data2)
print()

print(df_data3)
print()