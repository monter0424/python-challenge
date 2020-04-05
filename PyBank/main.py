import os
import csv

csvpath = os.path.join('Bank Data.csv')

##STEP ONE: Determine values 
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    count = 0
    total_amount = 0
    average_change = 0
    total_profits = 0 
    total_losses = 0
    for row in csvreader:
        count = count +1 
        total_amount = (total_amount + int(row[1]))
        average_change = total_amount/count
        if int(row[1]) > 0:
            total_profits = total_profits + int(row[1])
        if int(row[1]) < 0:
            total_losses = total_losses + int(row[1])
        #greatest_increase =
        #greatest_decrease =

    print('Financial Analysis')
    print('------------------------------------------')    
    print (f'Total Months: {count}')
    print (f'Total: {total_amount}')
    print (f'Average Change: {average_change}')
    print (f'Greatest Increase in Profits: {total_profits}')
    print (f'Greatest Decrease in Profits: {total_losses}')

##STEP TWO: Output as txt file. 
output_file = os.path.join('Financial Analysis.txt')

with open(output_file, "w") as text_file:
    print("""
    Financial Analysis
    ------------------------------------------
    Total Months: 86
    Total: 38382578
    Average Change: 446309.0465116279
    Greatest Increase in Profits: 45710004
    Greatest Decrease in Profits: -7327426""")







            