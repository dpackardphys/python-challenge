import os
import csv

#Read in data from csv file, skip header
csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    num_months = 0
    net_profit = 0
    profits = list()
    profit_change = dict()
    max_change = 0
    min_change = 0

    #Read first month of data
    first_month = next(csvreader)
    num_months += 1
    net_profit = net_profit + int(first_month[1])
    profits.append(int(first_month[1]))
    #print(profits)
    j = 0

    #Loop over remaining months
    for row in csvreader:
        #Increment the number of months in the data
        num_months += 1
        
        #Add new profits/losses
        net_profit = net_profit + int(row[1])
        profits.append(int(row[1]))

        #Record monthly changes
        profit_change[row[0]] = (profits[j+1]-profits[j])
        j += 1

        #Record min and max changes
        if profit_change[row[0]] > max_change:
            max_change = profit_change[row[0]]
            max_month = row[0]
        elif profit_change[row[0]] < min_change:
            min_change = profit_change[row[0]]
            min_month = row[0]
      
        

    #Calculate average (sum of differences is difference of first 
    # and last elements)
    avg_change = (profits[num_months-1]-profits[0])/len(profit_change)

    #Open output text file
    output_path = os.path.join('Analysis','results.txt')
    with open(output_path, 'w') as output_file:
        print("Financial Analysis")
        output_file.write("Financial Analysis\n")
        print("----------------------------")
        output_file.write("----------------------------\n")
        print(f"Total Months: {num_months}")
        output_file.write(f"Total Months: {num_months}\n")
        print(f"Total Profit: ${net_profit}")
        output_file.write(f"Total Profit: ${net_profit}\n")
        print(f"Average Change: ${round(avg_change,2)}")
        output_file.write(f"Average Change: ${round(avg_change,2)}\n")
        print(f"Greatest Increase in Profits: {max_month} (${max_change})")
        output_file.write(f"Greatest Increase in Profits: {max_month} (${max_change})\n")
        print(f"Greast Decrease in Profits: {min_month} (${min_change})")
        output_file.write(f"Greast Decrease in Profits: {min_month} (${min_change})")
