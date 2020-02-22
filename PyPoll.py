# The data we need to retrieve
# 1. The total number of votes casted.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

import csv
import os

'''file_to_upload=os.path.join("Resources", "election_results.csv")'''

'''file_to_load='Resources/election_results.csv'
election_data=open(file_to_load, 'r')
#To do: Perform analysis

election_data.close()'''

'''with open(file_to_upload)as election_data:
    #To do: Perform analysis

    print(election_data)'''

'''file_to_save=os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Arapahoe, ")
    txt_file.write("Denver, ")
    txt_file.write("Jefferson")
    txt_file.write("Arapahoe, Denver, Jefferson")
    txt_file.write("Counties in the election\n-------------------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")'''


file_to_load=os.path.join("Resources", "election_results.csv")
file_to_save=os.path.join("analysis", "election_analysis")

total_votes=0
candidate_options=[]
candidate_votes={}

winning_candidate=""
winning_count=0
winning_percentage=0

with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    headers=next(file_reader)
    '''print(headers)'''

    for row in file_reader:
        total_votes+=1
        candidate_name=row[2]
        if(candidate_name not in candidate_options):
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1
        #print(row)
    
with open(file_to_save, "w") as txt_file:

    total_vote_summary= (f"Election Results\n"
    f"------------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"------------------------------\n")

    print(total_vote_summary, end="")

    txt_file.write(total_vote_summary)

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results_summary = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n") 
        print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n") 
        txt_file.write(candidate_results_summary)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage= vote_percentage
            winning_candidate=candidate


#print(total_votes)
#print(candidate_options)
#print(candidate_votes)
    winning_candidate_summary= (
        f"------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning vote count: {winning_count:,}\n"
        f"Winning percentage: {winning_percentage:.1f}%\n"
        f"------------------------------\n"
    )
    txt_file.write(winning_candidate_summary)
    print(winning_candidate_summary)