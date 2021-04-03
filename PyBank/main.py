'Import Modules for working with .csv file'
import os
import csv
import statistics

'Create file path for budget_data.csv file'
budget_data_file_path = os.path.join('Resources', 'budget_data.csv')

'Write output file path'
output_path = os.path.join("Analysis", "budget_data_append.csv")

'Write output summary file path'
text_path = os.path.join("Analysis", "summary.txt")

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
    for x in range(1,len(profit_or_loss)):
        monthly_change = profit_or_loss[x] - profit_or_loss[x-1]
        profit_change.append(monthly_change)
    
    profit_change.insert(0, 0)

    total_months = len(month)
    net_profit = sum(profit_or_loss)
    avg_profit_change = statistics.mean(profit_change)
    max_profit = max(profit_change)
    max_loss = min(profit_change)

    'Re-zip lists, including new profit change list, into tuple'
    roster = zip(month, profit_or_loss, profit_change)

'Open output file and create writer'
with open(output_path, "w") as newcsvfile:
    """newcsvwriter = csv.writer(newcsvfile, delimiter=",")
    
    newcsvwriter.writerow = (['Month', 'Profit/Loss', 'Profit Change'])
    newcsvwriter.writerows(roster)

    for row in newcsvwriter:
        if row[2] == max_profit:
            max_profit_month = row[0]
        elif row[2] == max_loss:
            max_loss_month = row[0]

    text_path = os.path.join("Analysis", "results.txt")

    text = open(text_path, "w")
"""

with open(text_path, "w") as text:
    
    output = (
    "Financial Analysis\n"
    "--------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_profit}\n"
    f"Average Change: ${avg_profit_change}"
    )
    """f"Greatest Increase in Profits: {max_profit_month} (${max_profit})"
    f"Greatest Decrease in Profits: {max_loss_month} (${max_loss})"
    """
    
    text.write(output)