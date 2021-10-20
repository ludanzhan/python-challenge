import os
import csv
# import sys

csv_path = os.path.join('resources','election_data.csv')
# sys.stdout = open('Analysis/PyPoll.txt','w')
with open(csv_path,'r') as election_csv:
    election_reader = csv.reader(election_csv, delimiter = ',')
    header = next(election_reader)

    count = 0
    khan = 0
    correy = 0
    li = 0
    otooley = 0

    for row in election_reader:
        if str(row[2]) == "Khan":
            khan += 1
        elif str(row[2]) == "Correy":
            correy += 1
            
        elif str(row[2]) == "Li":
            li += 1
        elif str(row[2]) == "O'Tooley":
            otooley += 1

        count += 1

        percent_khan = float(khan / count)*100
        percent_coreey = float(correy / count)*100
        percent_otooley = float(otooley / count)*100
        percent_li = float(li / count)*100

    print("Election Results\n" 
          + "---------------------------\n"
          + "Total Votes: " + str(count) + "\n"
          + "---------------------------\n"
          + "Khan: " + str(percent_khan) + "% (" + str(khan) + ")\n"
          + "Coreey: " + str(percent_coreey) + "% (" + str(correy) + ")\n"
          + "Li: " + str(percent_li) + "% (" + str(li) + ")\n"
          + "O'Tooley: " + str(percent_otooley) + "% (" + str(otooley) + ")\n"
          + "-----------------------------\n")