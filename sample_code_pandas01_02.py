import pandas as pd

list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr_data = pd.Series(list_data)

print(sr_data)

n_index = sr_data.index
str_value = sr_data.values

print(n_index)
print()
print(str_value)