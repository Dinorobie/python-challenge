import os
import csv
csvpath = os.path.join("..", "PYTHON-CHALLENGE", "budget_data.csv")
total_months=[]
profits_losses=[]
change_profits_lose=[]

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
 # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
# Read each row of data after the header
    for row in csvreader:
        total_months.append(row[0])
        profits_losses.append(float(row[1]))
#loop
    for i in range(1, len(profits_losses)):
        change_profits_lose.append(profits_losses[i]-profits_losses[i-1])
        avarage_change=sum(change_profits_lose)/len(change_profits_lose)

    maxincrease=change_profits_lose.index(max(change_profits_lose))+1
    maxdeacreas=change_profits_lose.index(min(change_profits_lose))+1
#Amount of months in budget_data
print(f'total months:{len(total_months)}')
print(f'total: ${sum(profits_losses)}')
print(f'Avarage Change: ${round(avarage_change,2)}')
print(f'Greatest increase in profit:{total_months[maxincrease]} ${max(change_profits_lose)}')
print(f'Greatest decrease in profit:{total_months[maxdeacreas]} ${min(change_profits_lose)}')
#Creat File
output_path = os.path.join("analysis", "financials_analysis.txt")
with open(output_path, 'w') as text2:
    text2.write(f'Financial analysis\n')
    text2.write(f'total months:{len(total_months)}\n')
    text2.write(f'Avarage Change: ${round(avarage_change,2)}\n')
    text2.write(f'Greatest increase in profit:{total_months[maxincrease]} ${max(change_profits_lose)}\n')
    text2.write(f'Greatest decrease in profit:{total_months[maxdeacreas]} ${min(change_profits_lose)}\n')