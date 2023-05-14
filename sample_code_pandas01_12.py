import pandas as pd

dict_data = {'이름': ['서준', '우현', '인아'],
            '수학': [90,80,70,], '영어': [98,89,95],
            '음악': [85,95,100], '체육': [100,90,90]}

df_data = pd.DataFrame(dict_data)
print(df_data)
print()

df_data['국어'] = 80

print(df_data)