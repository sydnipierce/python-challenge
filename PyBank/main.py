'Import Modules'
import os
import csv
import statistics

'Create file path for budget_data.csv file'
budget_data_file_path = os.path.join('Resources', 'budget_data.csv')

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
    
    'Insert a value for the first month of the profit change list to force alignment of changes with correct month'
    profit_change.insert(0, 0)

    'Calculate core statistics for analysis'
    total_months = len(month)
    net_profit = sum(profit_or_loss)
    max_profit = max(profit_change)
    max_loss = min(profit_change)

    'Check that max/min values are correct'
    'print(max_profit)'
    'print(max_loss)'

    'Find index number for max and min profits to locate corresponding months in months list.'
    max_month_index = profit_change.index(max_profit)
    min_month_index = profit_change.index(max_loss)

    'Locate corresponding months in months list'
    max_profit_month = month[max_month_index]
    max_loss_month = month[min_month_index]

    'Remove forced zero value in profit change list to generate correct average value'
    profit_change.pop(0)
    avg_profit_change = statistics.mean(profit_change)

'Write output to summary txt file'
with open(text_path, "w") as text:
    
    output = (
    "Financial Analysis\n"
    "--------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_profit}\n"
    f"Average Change: ${avg_profit_change}\n"
    f"Greatest Increase in Profits: {max_profit_month} (${max_profit})\n"
    f"Greatest Decrease in Profits: {max_loss_month} (${max_loss})"
    )
    
    text.write(output)

'Print summary results to terminal'
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${avg_profit_change}")
print(f"Greatest Increase in Profits: {max_profit_month} (${max_profit})")
print(f"Greatest Decrease in Profits: {max_loss_month} (${max_loss})")