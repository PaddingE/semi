import pandas as pd

df_exer = pd.read_excel('./연습용.xlsx')

print(df_exer)

df_exer.drop('단위',axis= 1, inplace= True)

print(df_exer)

df_exer.drop('항목',axis= 1, inplace= True)
print(df_exer)
print()

print(df_exer.shape)
print(df_exer.dtypes)