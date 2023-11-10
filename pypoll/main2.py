import os

file_name = "election_data.csv"
output_fname = "BudgetAnalysis.txt"
csvpath = os.path.join(os.getcwd(), "Resources", file_name)
outpath = os.path.join(os.path.curdir, output_fname)

# Read the Election_data.csv file
with open(csvpath, 'r') as file:
    lines = file.readlines()

# Extract header and data
header = lines[0].strip().split(',')
data_lines = [line.strip().split(',') for line in lines[1:]]

# Create a dictionary to store counts for each candidate
candidate_counts = {}
for line in data_lines:
    candidate = line[2]  
    if candidate in candidate_counts:
        candidate_counts[candidate] += 1
    else:
        candidate_counts[candidate] = 1

# Find the total votes
total_count = sum(candidate_counts.values())

# Calculate the percentage of votes each candidate received
percentage_data = {candidate: (count / total_count) * 100 for candidate, count in candidate_counts.items()}

# Find the winner
winner = max(percentage_data, key=percentage_data.get)

# Print and write results to a text file 
output_data = []
output_data.append("Election Results \n")
output_data.append("---------------------------------------- \n")
output_data.append(f"Total Votes: {total_count:.0f}\n")
output_data.append("---------------------------------------- \n")
# Append the results to the output_data list with specified length between fields
for candidate, count in candidate_counts.items():
    percentage = percentage_data[candidate]
    output_data.append("{:<25} {:<05.3f}% ({:})\n".format(candidate, percentage, count))

output_data.append("---------------------------------------- \n")
output_data.append(f"Winner: {winner}\n")
output_data.append("---------------------------------------- \n")

# Write the output data to a text file
with open(outpath, 'w') as output_file:
    output_file.writelines(output_data)

# Print the data 
for line in output_data:
    print(line)
