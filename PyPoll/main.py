# Eric Nordstrom
# November 18, 2019
# Second homework assignment for UT Data Analysis & Visualization boot camp
# Python 3.6.4


python_challenge_path = 'C:/users/eanor.LORDSTROM/Dropbox/Documents/Education/Data Analysis & Viz Boot Camp/Homework/02-Python'  # path on my computer; replace with your path
import csv, sys
sys.path.insert(1, python_challenge_path)  # for next import: path on my computer; allows running from any directory
sys.path.insert(2, '..')  # for next import: up one level if currently in PyPoll folder; allows running on any computer if in this folder
import print_and_write as paw
import datetime as dt


"""DATA"""

election_data_path = 'C:/users/eanor.LORDSTROM/Dropbox/Documents/Education/Data Analysis & Viz Boot Camp/UT-MCB-DATA-PT-11-2019-U-C/Homework/02-Python/Instructions/PyPoll/Resources/election_data.csv'  # path on my computer; replace with your path


"""RUN"""

if __name__ == '__main__':
    
    vote_counts = {}  # key = candidate name; value = number of votes
    timestamp = dt.datetime.now()
    print()

    # read and record info

    with open(election_data_path, 'r') as in_file:

        election_data = csv.reader(in_file)
        header = next(election_data)

        for row in election_data:
            
            candidate = row[2]
            
            if candidate in vote_counts:
                vote_counts[candidate] += 1
            else:
                vote_counts[candidate] = 1
    
    
    # report

    total_votes = sum(vote_counts.values())
    winner = max(vote_counts, key=lambda candidate: vote_counts[candidate])
    
    with open('output_file.txt', 'a') as out_file:
        
        paw.write_like_print(out_file, timestamp)
        paw.write_like_print(out_file)
    
        paw.print_and_write(out_file, '~~~ RESULTS ~~~')
        paw.print_and_write(out_file, 'Total votes:', total_votes)
        paw.print_and_write(out_file, 'Votes by candidate...')

        for candidate in vote_counts:
            percent = round(vote_counts[candidate] / total_votes * 100, 2)
            paw.print_and_write(out_file, f'\t{candidate}: {percent}% ({vote_counts[candidate]})')
        
        paw.print_and_write(out_file, 'Winner:', winner)
        paw.write_like_print(out_file)
        paw.write_like_print(out_file)
