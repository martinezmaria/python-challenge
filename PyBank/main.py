# import modules
import os
import csv

# define path of the file to read, file_path
file_path = os.path.join("Resources", "budget_data.csv")

# define variables
months_count = []
total_months = 0
total_rev = []
row_index_revenue_loss = 1
rev_change = []

# open the cvs file and csv.reader to get a handle on the file and skip header row
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    if csv.Sniffer().has_header:
        next(csvreader) 
    
# for loop csvreader (all data rows, excluding header)
    for row in csvreader:
# calculate total number of months in dataset, months_count
        total_months += 1
        months_count.append(row[0])
        
# calculate net total amount of "profit/loss" over entire period, total_rev
        total_rev.append(int(row[1]))

    for i in range(len(total_rev)-1):
# calculate revenue change 
        rev_change.append(total_rev[i+1]-total_rev[i])
        
#define and compare max, min revenue values        
max_increase_value = max(rev_change)
max_decrease_value = min(rev_change)

max_increase_month = rev_change.index(max(rev_change)) + 1
max_decrease_month = rev_change.index(min(rev_change)) - 1


# Print
print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {total_months}")
print(f"Total Net Revenue: $ {sum(total_rev)}")


# calculate average of changes in "profit/loss" over entire period
print(f"Average Change is: {round(sum(rev_change)/len(rev_change),2)}")


# find greatest increase in "profits" (date and amount), greatest_increase
print(f"Greatest Increase in Revenue: {months_count[max_increase_month]} (${(str(max_increase_value))})")


# find greatest decrease in "losses" (date and amount), greatest_decrease
print(f"Greatest Decrease in Revenue: {months_count[max_decrease_month]} (${(str(max_decrease_value))})")



# write to output file with the results
output_path = os.path.join("Analysis", "results.txt")
with open(output_path, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------------------------------"])
    csvwriter.writerow([f"Total Months: {total_months}"])
    csvwriter.writerow([f"Total Net Revenue: $ {sum(total_rev)}"])
    csvwriter.writerow([f"Average Change is: {round(sum(rev_change)/len(rev_change),2)}"])
    csvwriter.writerow([f"Greatest Increase in Revenue: {months_count[max_increase_month]} (${(str(max_increase_value))})"])
    csvwriter.writerow([f"Greatest Decrease in Revenue: {months_count[max_decrease_month]} (${(str(max_decrease_value))})"])