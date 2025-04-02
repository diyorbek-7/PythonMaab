import pandas as pd
import sqlite3



#part1
#task1
# df_customer = pd.read_sql('select * from customers',sqlite3.connect(r'C:\Users\shoki\PycharmProjects\PythonProject\lesson-16\chinook.db'))
# print(df_customer.head(10))

#task2
# df_iris=pd.read_json(r'C:\Users\shoki\PycharmProjects\PythonProject\lesson-16\homework\iris.json')
# print(df_iris.shape)
# column_names = list(df_iris.columns)
# print(column_names)

#task3
# df_titanic = pd.read_excel(r'C:\Users\shoki\PycharmProjects\PythonProject\lesson-16\homework\titanic.xlsx')
# print(df_titanic.head(5))


# ----------- #4
# flights = pd.read_parquet(r'C:\Users\shoki\PycharmProjects\PythonProject\lesson-16\fights_files')
# print(flights.info)

#5
# df = pd.read_csv(r'C:\Users\shoki\PycharmProjects\PythonProject\lesson-16\homework\movie.csv')
# print(df.sample(10))

#part2
#task1
# df=pd.read_json(r'C:\Users\shoki\PycharmProjects\PythonProject\lesson-16\homework\iris.json')
# df.rename(columns = lambda x:x.lower() if x in ['sepalLength', 'sepalWidth'] else x, inplace=True)
# print(df.columns)

#task2
# df = pd.read_excel(r'C:\Users\shoki\PycharmProjects\PythonProject\lesson-16\homework\titanic.xlsx')
# filtered_rows = df[df['Age']>30]
# genderCounts = filtered_rows['Sex'].value_counts()
# print(genderCounts)

#----task3


#task4
# df = pd.read_csv(r'C:\Users\shoki\PycharmProjects\PythonProject\lesson-16\homework\movie.csv')
# filtered = df[df['duration']>120]
# sort_ed = filtered.sort_values(by = 'director_facebook_likes',ascending = False)
# print(sort_ed)


#part3
df_iris=pd.read_json(r'C:\Users\shoki\PycharmProjects\PythonProject\lesson-16\homework\iris.json')
df_titanic = pd.read_excel(r'C:\Users\shoki\PycharmProjects\PythonProject\lesson-16\homework\titanic.xlsx')
df_movie = pd.read_csv(r'C:\Users\shoki\PycharmProjects\PythonProject\lesson-16\homework\movie.csv')

#1
# numerical_df = df_iris.select_dypes(include='numeric')
# mean = numerical_df.mean()
# median = numerical_df.median()
# std = numerical_df.std()

#2
# print(df_titanic['Age'].min())
# print(df_titanic['Age'].max())
# print(df_titanic['Age'].sum())

#3
top_director = df_movie.groupby('director_name')['director_facebook_likes'].sum().idxmax()
print("Director with the highest total Facebook likes:", top_director)

longest_movies = df_movie[['movie_title', 'director_name', 'duration']].nlargest(5, 'duration')
print("\n5 Longest Movies and Their Directors:\n", longest_movies)








