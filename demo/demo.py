import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
def add_column(df):
        df['D'] = 20
        return df
df = df.pipe(add_column)
print(df)