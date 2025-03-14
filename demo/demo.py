# import pandas as pd
# df = pd.read_csv(r'C:\Users\shoki\PyCharmProjects\PythonProject\demo\email.csv')
# print(df.head(3))
import pandas as pd

data = [
    ['A','B',21],
    ['C','D',22],
    ['F','S',54]
     ]
columns = ['Name','Fname','Age']
df = pd.DataFrame(data = data, columns=columns)
print(df)