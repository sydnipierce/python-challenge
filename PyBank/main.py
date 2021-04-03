'Import Modules for working with .csv file'
import os
import csv

'Create file path for budget_data.csv file'
budget_data_file_path = os.path.join('Resources', 'budget_data.csv')

'While the budget_data.csv file is open, do the following:'
with open(budget_data_file_path) as budget_csvfile:

    'Create variable for the read .csv using delimiter comma'
    csvreader = csv.reader(budget_csvfile, delimiter=',')

    'Check that reading .csv file worked'
    'for row in csvreader:'
    'print(row)'
    
    'Create empty lists to collect .csv column data'
    month = []
    profit_or_loss = []

    'Find the number of records in the table'
    header = next(csvreader)
    total_months = 0
    for row in csvreader:
        total_months = total_months + 1
        month.append(row[0])
        profit_or_loss.append(row[1])

    net_profit = sum(profit_or_loss)

    print(total_months)

