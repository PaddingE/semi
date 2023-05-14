import pandas as pd

tup_data = ('영인', '2010-05-01', '여', True)
list_index = ['이름', '생년월일', '성별', '학생여부']
sr_data = pd.Series(tup_data, index= list_index)

print(sr_data)

print(sr_data[0])
print(sr_data['이름'])
print()

print(sr_data[[1,2]])
print(sr_data[['생년월일', '성별']])
print()

print(sr_data[1 : 3])
print(sr_data['생년월일': '성별'])