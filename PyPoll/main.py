'Import Modules for working with .csv file'
import os
import csv
import pandas as pd

khan_count = 0
li_count = 0
correy_count = 0
otooley_count = 0

'Create file path for election_data.csv file'
election_data_file_path = os.path.join('Resources', 'election_data.csv')

'While the election_data.csv file is open, do the following:'
with open(election_data_file_path) as election_csvfile:

    'Create variable for the read .csv using delimiter comma'
    csvreader = csv.reader(election_csvfile, delimiter=',')

    'Check that reading .csv file worked'
    'for row in csvreader:'
    'print(row)'

    'Create empty lists to collect .csv column data'
    voters = []
    candidates = []

    'Read header row, put cursor on next data line'
    header = next(csvreader)

    'Loop through data rows and create lists from columns'
    for row in csvreader:
        voters.append(row[0])
        candidates.append(row[2])

        if row[2] == "Khan":
            khan_count = khan_count + 1
        elif row[2] == "Li":
            li_count += 1
        elif row[2] == "Correy":
            correy_count += 1
        elif candidate == "O'Tooley":
            otooley_count += 1

    for x in range(5):
        print(voters[x])
        print(candidates[x])
        
    'Pull a list of unique candidates'
    candidates_set = set(candidates)
    unique_candidates = list(candidates_set)
    print(unique_candidates)

    total_votes = len(voters)
    print(total_votes)

    khan_percent = khan_count / total_votes
    li_percent = li_count / total_votes
    correy_percent = correy_count / total_votes
    otooley_percent = otooley_count / total_votes

    print(khan_count)
    print(li_count)
    print(correy_count)
    print(otooley_count)

    if (khan_count > li_count) and (khan_count > correy_count) and (khan_count > otooley_count):
        winner = "Khan"
    elif (li_count > khan_count) and (li_count > correy_count) and (li_count > otooley_count):
        winner = "Li"
    elif (correy_count > khan_count) and (correy_count > li_count) and (correy_count > otooley_count):
        winner = "Correy"
    elif (otooley_count > khan_count) and (otooley_count > li_count) and (otooley_count > correy_count):
        winner = "O'Tooley"
    else:
        winner = "None"