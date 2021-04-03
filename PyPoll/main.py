'Import Modules for working with .csv file'
import os
import csv
import pandas as pd

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
        
    'Pull a list of unique candidates'
    candidates_set = set(candidates)
    unique_candidates = list(candidates_set)
    print(unique_candidates)

    khan_count = 0
    li_count = 0
    correy_count = 0
    otooley_count = 0

    for row in csvreader:
        if row[2] == candidates_set[0]:
            khan_count = khan_count 