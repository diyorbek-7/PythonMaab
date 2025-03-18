import sqlite3
import pandas as pd

#merging nad joining
#1
# con = sqlite3.connect('chinook.db')
# cursor = con.cursor()
# query = '''
# SELECT customers.CustomerId, customers.FirstName, customers.LastName, COUNT(invoices.InvoiceId) AS TotalInvoices
# FROM customers
# INNER JOIN invoices ON customers.CustomerId = invoices.CustomerId
# GROUP BY customers.CustomerId
# ORDER BY TotalInvoices DESC;
# '''
# df = pd.read_sql_query(query,con)
# print(df)

#2
# df = pd.read_csv('movie.csv')
# df1 = df[['director_name','color']]
# df2 = df[['director_name','num_critic_for_reviews']]
# left_join_df = pd.merge(df1,df2,on='director_name',how = 'left')
# outer_join_df = pd.merge(df1,df2,on = 'director_name',how = 'outer')
# print(len(left_join_df))
# print(len(outer_join_df))

#grouping and aggregating
#1
# df = pd.read_excel('titanic.xlsx')
#
# grouped_df = df.groupby('Pclass').agg(
#     Average_age = ('Age','mean'),
#     Total = ('Fare','sum'),
#     passenger_count = ('Pclass','count')
# )
# print(grouped_df)

#2
# df = pd.read_csv('movie.csv')
#
# grouped_df = df.groupby(['color','director_name']).agg(
#     Total_Critic_Reviews = ('num_critic_for_reviews','sum'),
#     Average_Duration = ('duration','mean')
# ).reset_index()
# print(grouped_df)

#3---

#apply functions
#1
# df = pd.read_excel('titanic.xlsx')
# def classify(age):
#     return 'Adult' if age>18 else 'child'
# df['Age_Group']=df['Age'].apply(classify)
# print(df[['Age','Age_Group']])

#2
# df = pd.read_csv("employee.csv")
# def normalize(group):
#     return (group - group.min()) / (group.max() - group.min())
# df["Normalized_Salary"] = df.groupby("DEPARTMENT")["BASE_SALARY"].apply(normalize).reset_index(level=0, drop=True)
# print(df[["DEPARTMENT", "BASE_SALARY", "Normalized_Salary"]].head())


#3
# df = pd.read_csv('movie.csv')
# def classify(duration):
#     if duration<60:
#         return 'Short'
#     elif duration>60:
#         return 'Long'
#     else:
#         return 'Medium'
# df['Classify_duration']=df['duration'].apply(classify)
# print(df[['duration','Classify_duration']])

#using pipe
#1
# df = pd.read_excel('titanic.xlsx')
# def filter(df):
#     df = df[df['Survived']==1]
#     return df
# def filling(df):
#     df["Age"] = df["Age"].fillna(df["Age"].mean())
#     return df
# def create_fare_per_age(df):
#     df["Fare_Per_Age"] = df["Fare"] / df["Age"]
#     return df
# df = (df.pipe(filter)
#       .pipe(filling)
#       .pipe(create_fare_per_age))
