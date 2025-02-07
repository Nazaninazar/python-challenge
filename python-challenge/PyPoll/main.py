# cd 
#cd PyPoll
#open main.py
#import file

#create file paths across operating systems
import os
import csv


#path to the csvfile
csvpath = os.path.join('Resources', 'election_data.csv')

#dictionary for candidate name and vote count.
poll = {}

#Sets variable
total_votes = 0

# open CSV file 
with open(csvpath,'r') as csvfile:
   csvread= csv.reader(csvfile)

#skips header line
next(csvread,None)

# from column 3, using each name only once.
#counts votes for each candidate
#keeps a total vote count by counting up 1

for row in csvread:
 total_votes+=1
 if row[2] in poll.keys():
  poll[row[2]]= poll[row[2]]+1
 else: 
  poll[row[2]]=1
  
#empty list for candidates and the vote associated to them
candidates = []
num_votes = []

#Candidates & number of vote 
for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)
    
# vote % list
vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 3))

# zips candidates, num_votes, vote_percent into tuples
clean_data = list(zip(candidates, num_votes, vote_percent))
# winner_list(even if a tie)
winner_list = []

for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

# winner_list a str with the first entry
winner = winner_list[0]

#only runs if there is a tie- separated by commas
if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

#prints to file
output_file = os.path.join('election_results.txt')

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in clean_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

#prints file to terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())  Out [2]:  Election Results 

   
    
  