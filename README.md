# python-challenge
This project is to use Python to read Excel CSV files. Loop through each row and summarize the data. Then print out the console output to a text file.
### Steps:
1. Import libraries needed to read CSV files and write out the console output
```python
import os
import csv
import sys
```
2. Open the Excel files and loop through each row
```python
csv_path = os.path.join('resources','budget_data.csv')
sys.stdout = open('Analysis/PyBank.txt','w')

with open(csv_path,'r') as budget_csv:

    budget_reader = csv.reader(budget_csv, delimiter = ',')
    header = next(budget_reader)
    
    for row in budget_reader:
```
3. Analyze the data and write out the console output to an exist text file
```python
sys.stdout = open('Analysis/PyBank.txt','w')
sys.stdout.close()
```
4. _[Final Results](https://github.com/ludanzhan/python-challenge/blob/main/Analysis/PyBank.txt)_

