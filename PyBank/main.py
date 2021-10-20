import os
import csv

csv_path = os.path.join('resources','budget_data.csv')

with open(csv_path,'r') as budget_csv:

    budget_reader = csv.reader(budget_csv, delimiter = ',')
    header = next(budget_reader)

    total = 0
    count = 0
    greatest_increase = 0
    greatest_decrease = 0

    for row in budget_reader:
        num = int(row[1])
        
        if num > 0:
            if num > greatest_increase:
                greatest_increase = num
        elif num<0:
            if num < greatest_decrease:
                greatest_decrease = num

        total += int(row[1])
        count +=1


    print("Finiancial Analysis\n" 
          + "------------------------------\n"
          + "Total Month: " + str(count) + "\n" 
          + "Total: $"+ str(total) + "\n"
          + "Greaatest Increase: " + "($" + str(greatest_increase) +")"+ "\n"
          + "Greatest Decrease: " + "($" + str(greatest_decrease)+ ")" )

        
       