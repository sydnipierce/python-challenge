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
    profit_change = []

    'Read header row, put cursor on next data line'
    header = next(csvreader)

    'Loop through data rows and create lists from columns'
    for row in csvreader:
        month.append(row[0])
        profit_or_loss.append(int(row[1]))
        
    'Calculate the change in profit between each month and create a list'
    for range(1, 87) in profit_or_loss:
        monthly_change = next(profit_or_loss) - profit_or_loss
        profit_change.append(monthly_change)

    'Make profit change list align with end month rather than beginning month'
    profit_change.insert(0, 0)
    profit_change.pop(86)

    total_months = len(month)
    net_profit = sum(profit_or_loss)
    avg_profit_change = mean(profit_change)
    max_profit = max(profit_change)
    max_loss = min(profit_change)

    'Re-zip lists, including new profit change list, into tuple'
    roster = zip(month, profit_or_loss, profit_change)

    'Write output file path'
    output_path = os.path.join("Analysis", "budget_data_append.csv")

    'Open output file and create writer'
    with open(output_path, 'w', newline='') as newcsvfile:
        newcsvwriter = csv.writer(newcsvfile, delimiter=",")
        newcsvwriter.writerow = (['Month', 'Profit/Loss', 'Profit Change'])
        newcsvwriter.writerows(roster)

    for row in newcsvwriter:
        if profit == max_profit:
            max_profit_month = 

    print(total_months)
    print(net_profit)
    print(profit_change)