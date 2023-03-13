import csv

file_to_load = "PyPoll/Resources/election_data.csv"
total_vote = 0
vote = 0
name = 0
candidates = []
candidate_total_votes = {}
percent = 0
percent_candidate_vote = {}
new_max = 0


with open(file_to_load,'r') as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    header =next(csvreader)

    for row in csvreader:
        total_vote += 1
        current_candidates = (row[2])
        if current_candidates not in candidates:
            candidates.append(current_candidates)
            candidate_total_votes[current_candidates] = 0
        candidate_total_votes[current_candidates] += 1
    for candidate_name in candidate_total_votes:
        vote = candidate_total_votes.get(candidate_name)
        print(candidate_name)
        print(float(vote)/float(total_vote)*100)
    #print(candidate_total_votes)
    for candidate, candidate_votes in candidate_total_votes.items():
        #print(candidate)
        #print(candidate_votes)
        max_votes = candidate_votes
        if max_votes >= new_max:
            new_max = max_votes
            winning_candidate = candidate
    print(f"the winner is:{winning_candidate}")
    


print(f"Total Votes: {total_vote}")
print(f"The candidate name is: {candidates}")
print(f"Total Votes is {candidate_total_votes}")






