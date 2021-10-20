import os
import csv

def print_percentages(budget_data):
    total = int(budget_data[1])
    print(f"Total: {str(total)}")



csv_path = os.path.join('resources','budget_data.csv')

with open(csv_path,'r') as budget_csv:
    budget_reader = csv.reader(budget_csv, delimiter = ',')
    header = next(budget_reader)

    for row in budget_reader:
        print_percentages(row)