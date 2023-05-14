import pandas as pd

dict_data = {'a': 1, 'b' : 2, 'c': 3}

sr_data = pd.Series(dict_data)

print(type(sr_data))
print()
print(sr_data)