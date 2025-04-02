# import numpy as np
# array = np.array([22,25,24,28,30,27,26])
# print(np.mean(array))
# print(np.median(array))
# print(np.std(array))
# print(np.max(array))
# print(np.min(array))
from turtledemo.paint import switchupdown


# students = ['a','b','c','d','e','f']
# score = (70,20,30,40,50,60)
# passed_students = []
# count = 0
# for i , j in zip(students,score):
#     if j >= 50 :
#         passed_students.append(i)
#         count+=1
# print(passed_students)


# Step 1: Import the required library
import pandas as pd

# Step 2: Read the JSON file into a Pandas DataFrame
df = pd.read_json('sales_data.json')

# Step 3: Extract the 'sales' data and convert it into a DataFrame
# The 'sales' column contains a list of dictionaries, so we directly use it to create a DataFrame
sales_df = pd.DataFrame(df['sales'].tolist())

# Step 4: Calculate the revenue for each product (price * quantity)
sales_df['revenue'] = sales_df['price'] * sales_df['quantity']

# Step 5: Compute the total revenue by summing the 'revenue' column
total_revenue = sales_df['revenue'].sum()

# Step 6: Print the total revenue in the expected format
print(f"TOTAL REVENUE: ${total_revenue}")
