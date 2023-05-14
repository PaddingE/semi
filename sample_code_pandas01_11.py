import pandas as pd

dict_data = {'이름': ['서준', '우현', '인아'],
            '수학': [90,80,70,], '영어': [98,89,95],
            '음악': [85,95,100], '체육': [100,90,90]}

df_data = pd.DataFrame(dict_data)
df_data.set_index('이름', inplace= True)
print(df_data)

n_element1 = df_data.loc['서준', '음악']
print(n_element1)

n_element2 = df_data.iloc[0,2]
print(n_element2)

n_element3 = df_data.loc['서준',['음악','체육']]
print(n_element3)

n_element4 = df_data.iloc[0,[2,3]]
print(n_element4)

n_element5 = df_data.loc['서준','영어':'체육']
print(n_element5)

n_element6 = df_data.iloc[0, 1:]
print(n_element6)