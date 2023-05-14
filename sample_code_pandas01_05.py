import pandas as pd

df_data = pd.DataFrame([[15,'남', '덕영중'],[17,'여','수리중']],
                       index= ['준서','예은'],
                       columns= ['나이','성별','학교'])

print(df_data)
print()

print(df_data.index)
print()

print(df_data.columns)
print()

df_data.index = ['학생1','학생2']
df_data.columns = ['연령', '남여', '소속']

print(df_data)
print()

print(df_data.index)
print()

print(df_data.columns)
print()