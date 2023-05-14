import pandas as pd

dict_data = {'이름': ['서준', '우현', '인아'],
            '수학': [90,80,70,], '영어': [98,89,95],
            '음악': [85,95,100], '체육': [100,90,90]}

df_data = pd.DataFrame(dict_data)

print(df_data)

print(type(df_data))
print()

math1 = df_data['수학']
print(math1)
print(type(math1))
print()

eng1 = df_data.영어
print(eng1)
print(type(eng1))
print()

mus_gym = df_data[['음악', '체육']]
print(mus_gym)
print(type(mus_gym))