import pandas as pd
import sqlite3
import numpy as np

# Read data into a DataFrame, as described in the lesson. 
# The SQL statement should retrieve the line_item_id, quantity, product_id, product_name, and price 
# from a JOIN of the line_items table and the product table. Hint: 
# Your ON statement would be ON line_items.product_id = products.product_id.
# Print the first 5 lines of the resulting DataFrame. Run the program to make sure this much works.

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """SELECT li.line_item_id, li.quantity, p.product_id, p.product_name, p.price FROM line_items li JOIN products p ON li.product_id = p.product_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    print(df.head())

df['total'] = df['quantity'] * df['price']
print(df.head())

# Add groupby() code to group by the product_id. Use an agg() method that specifies 
# 'count' for the line_item_id column, 
# 'sum' for the total column, and 
# 'first' for the 'product_name'. 
# Print out the first 5 lines of the resulting DataFrame. Run the program to see if it is correct so far.
result_df = df.groupby("product_id").agg({
    'line_item_id': 'count',
    'total': 'sum',
    'product_name': 'first'
}).reset_index()

print(result_df.head())

# Sort the DataFrame by the product_name column

result_df = result_df.sort_values('product_name')

# Add code to write this DataFrame to a file order_summary.csv, which should be written in the assignment7 directory. 
# Verify that this file is correct.

result_df.to_csv('../assignment7/order_summary.csv', index=False)
