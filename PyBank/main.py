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
    profit = 0
    loss = 0
    change = 0

    for row in budget_reader:
        num = int(row[1])

        if num > 0:
            if num > greatest_increase:
                greatest_increase = num
                profit += num
        elif num<0:
            if num < greatest_decrease:
                greatest_decrease = num
                loss += num

        if int(row[1]) == greatest_increase:
            increase = str(row[0])
        elif int(row[1]) == greatest_decrease:
            decrease = str(row[0])
        
        total += int(row[1])
        count +=1
        change = (profit + loss)/count


    print("Finiancial Analysis\n" 
          + "------------------------------\n"
          + "Total Month: " + str(count) + "\n" 
          + "Total: $"+ str(total) + "\n"
          + "Average Change: $" + str(change) + "\n"
          + "Greaatest Increase: " + increase+ " ($" + str(greatest_increase) +")"+ "\n"
          + "Greatest Decrease: " +decrease+ " ($" + str(greatest_decrease)+ ")" )
      

        
       