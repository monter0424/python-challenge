import os
import csv

##STEP ONE: Determine values 
csvpath = os.path.join('election_data.csv')

voters = 0
candidate = ""
candidate_vote = {}


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        candidate = str(row[2])
        voters = voters + 1
        if candidate == str('Khan'):
            candidate_one = 'Khan'
        elif candidate == str('Li'):
            candidate_two = 'Li'
        elif candidate == str('Correy'):
            candidate_three = 'Correy'
        else:
            candidate == str("O'Tooley")
            candidate_four = "O'Tooley"
        
        candidate = row[2]
        if candidate in candidate_vote:
            candidate_vote[candidate] = candidate_vote[candidate] + 1
        else:
            candidate_vote[candidate] = 1

print('Election Results')
print('---------------------------')
print(f'Total Votes: {voters}')
print('---------------------------')
print(f'{candidate_one}:')
print(f'{candidate_two}:')
print(f'{candidate_three}:')
print(f'{candidate_four}:')

##STEP TWO: Output into new txt file
output_file = os.path.join('Poll Analysis.txt')

with open(output_file, "w") as text_file:
    print("""
    Election Results
    ---------------------------
    Total Votes: 3521001
    ---------------------------
    Khan:
    Li:
    Correy:
    O'Tooley:""")