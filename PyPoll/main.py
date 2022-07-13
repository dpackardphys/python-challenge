import os
import csv

#Read in election data from csv file, skip header
csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #Define some initial variables
    num_votes = 0
    vote_dict = dict()
    
    #Loop through election data
    for row in csvreader:
        num_votes += 1
        
        #Googled "python remove duplicates from list" (because I was originally parsing the csv file into a list, not a dict),
        #found "not in" method here, which returns True if the given element is not in the given list (here, list of dictionary keys):
        #https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
        if row[2] not in vote_dict: 
            vote_dict[row[2]]= 0
        vote_dict[row[2]] += 1

#Start creating text file to store results
output_path = os.path.join('Analysis','results.txt')
with open(output_path, 'w') as output_file:
    print("Election Results")
    output_file.write("Election Results:\n")
    print("-------------------------")
    output_file.write("-------------------------\n")


    print(f"The total number of votes cast was {num_votes}")
    output_file.write(f"The total number of votes cast was {num_votes}\n")
    print("-------------------------")
    output_file.write("-------------------------\n")

    #Define variable to keep track of greatest vote total per candidate
    greatest_votes = 0

    #Loop through dictionary of candidates/votes
    for candidate in vote_dict:
        print(f"{candidate}: {round(100*vote_dict[candidate]/num_votes,3)}% ({vote_dict[candidate]})")
        output_file.write(f"{candidate}: {round(100*vote_dict[candidate]/num_votes,3)}% ({vote_dict[candidate]})\n")
        if vote_dict[candidate] > greatest_votes:
            greatest_votes = vote_dict[candidate]
            winner = candidate
    
    print("-------------------------")
    output_file.write("-------------------------\n")
    print(f'Winner: {winner}')
    output_file.write(f'Winner: {winner}')#Chicken dinner!

