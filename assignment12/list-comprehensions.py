import pandas as pd

df = pd.read_csv('../csv/employees.csv')

names_list = [f"{row["first_name"]} {row["last_name"]}" for _, row in df.iterrows()]
print(names_list)

names_e = [name for name in names_list if 'e' in name.lower()]
print(names_e)