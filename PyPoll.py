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

with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    headers=next(file_reader)
    print(headers)

    '''for row in file_reader:
        print(row)'''

