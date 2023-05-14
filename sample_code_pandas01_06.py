import pandas as pd

df_data = pd.DataFrame([[15,'남', '덕영중'],[17,'여','수리중']],
                       index= ['준서','예은'],
                       columns= ['나이','성별','학교'])

print(df_data)
print()

df_data.rename(columns= {'나이': '연령', '성별': '남여', '학교': '소속'}, inplace= True)
df_data.rename(index= {'준서' : '학생1', '예은' : '학생2'}, inplace= True)

print(df_data)