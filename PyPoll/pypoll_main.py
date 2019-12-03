import os, csv
with open(os.path.join("election_data.csv"), "r") as file:
	csv_reader = csv.reader(file, delimiter=',')
	data = list(csv_reader)

# The total number of votes cast
total_votes = len(data) - 1
print("Total Votes: " + str(total_votes))

# A complete list of candidates who received votes
candidate = []
for x in range(1,len(data)):
    candidate.append(data[x][2])

candidate_list = []
for x in candidate:
    if x not in candidate_list:
        candidate_list.append(x)
        
# The percentage of votes each candidate won 
# The total number of votes each candidate won
# The winner of the election based on popular vote  
for x in candidate_list:
    print(x + ": " 
    + str(round(candidate.count(x) / total_votes * 100)) 
    + "%" + " (" + str(candidate.count(x)) + ")")

    
winner = []

for x in candidate_list:
    if candidate.count(x) > candidate.count(winner):
        winner = x
print("Winner: " + winner)