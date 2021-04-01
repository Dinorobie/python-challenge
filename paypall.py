import os
import csv
csvpath = os.path.join("..", "PYTHON-CHALLENGE", "election_data.csv")
total_votes=[]
dict={}
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
# Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
# Read each row of data after the header
    for row in csvreader:
        total_votes.append(row[0])
        candidate= row[2]
        votes=1 
        if candidate not in dict:
            dict[candidate]  = votes
        else:
            dict[candidate]=dict[candidate]+1


winner= max(dict, key= dict.get)
      
#Print Result
print(f'total votes:{len(total_votes)}')
#loop
for candidate in dict:
    print(f'{candidate}: {round((dict[candidate]/(len(total_votes))*100),2)}% ({dict[candidate]})')
print(f'winner: {winner}')

#Creat File
output_path = os.path.join("analysis", "election_results.txt")
with open(output_path, 'w') as text2:
    text2.write(f' Elecction Results\n')
    text2.write(f' --------------------\n')
    text2.write(f'total votes:{len(total_votes)}\n')
    text2.write(f' --------------------\n')
    for candidate in dict:
        text2.write(f'{candidate}: {round((dict[candidate]/(len(total_votes))*100),2)}% ({dict[candidate]})\n')
    text2.write(f' --------------------\n')
    text2.write(f'winner: {winner}\n')
    text2.write(f' --------------------\n')