import os
import csv

csv_path = os.path.join("..","resources","budget_data.csv")

with open(csv_path,'r') as budget_csv:
    budget_reader = csv.reader(budget_csv, delimiter = ',')
    print(budget_reader)