# import modules
import os
import csv

# define path of the file to read, file_path
file_path = os.path.join("Resources", "election_data.csv")

# define variables
votes_count = []
total_votes = 0
candidates_list = []

khan_votes = 0
khan_percent = 0
correy_votes = 0
correy_percent = 0
li_votes = 0
li_percent = 0
otooley_votes = 0
otooley_percent = 0


# open the cvs file and csv.reader to get a handle on the file and skip header row
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    if csv.Sniffer().has_header:
        next(csvreader) 
    
# for loop csvreader (all data rows, excluding header)
    for row in csvreader:
# calculate total number of votes in dataset, total_votes
        votes_count.append(row[0])
        total_votes += 1
        
# calculate number of candidates and calculate total number of votes for each
        candidates_list.append(row[2])
        if row[2] == "Khan":
            khan_votes += 1
            khan_percent = round(khan_votes / total_votes *100)
        elif row[2] == "Correy":
            correy_votes += 1
            correy_percent = round(correy_votes / total_votes *100)
        elif row[2] == "Li":
            li_votes += 1
            li_percent = round(li_votes / total_votes *100)
        elif row[2] == "O'Tooley":
            otooley_votes += 1
            otooley_percent = round(otooley_votes / total_votes *100)

# find winner
candidates_votes_each = ([khan_votes, correy_votes, li_votes, otooley_votes])
candidates_names = ["Khan", "Correy", "Li", "O'Tooley"]
candidates_sort = dict(zip(candidates_names, candidates_votes_each))
key = max(candidates_sort, key=candidates_sort.get)

          

# Print
print("Election Results")
print("---------------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------------")
print(f"Khan: {(khan_percent)}% ({khan_votes})")
print(f"Correy: {(correy_percent)}% ({correy_votes})")
print(f"Li: {(li_percent)}% ({li_votes})")
print(f"O'Tooley: {(otooley_percent)}% ({otooley_votes})")
print("---------------------------------")
print(f"Winner: {key}")


# write to output file with the results
output_path = os.path.join("Analysis", "results.txt")
with open(output_path, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["-------------------------------------------"])
    csvwriter.writerow([f"Khan: {(khan_percent)}% ({khan_votes})"])
    csvwriter.writerow([f"Correy: {(correy_percent)}% ({correy_votes})"])
    csvwriter.writerow([f"Li: {(li_percent)}% ({li_votes})"])
    csvwriter.writerow([f"O'Tooley: {(otooley_percent)}% ({otooley_votes})"])
    csvwriter.writerow(["-------------------------------------------"])
    csvwriter.writerow([f"Winner: {key}"])
