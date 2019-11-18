# Eric Nordstrom
# November 18, 2019
# Second homework assignment for UT Data Analysis & Visualization boot camp
# Python 3.6.4


import csv
import datetime as dt


"""DATA"""

election_data_path = '..\\..\\..\\UT-MCB-DATA-PT-11-2019-U-C/Homework/02-Python/Instructions/PyPoll/Resources\\election_data.csv'.replace('/','\\')  # path on my computer; replace with your path

if __name__ == '__main__':
    
    vote_counts = {}  # candidate: number of votes


    # read and record info

    with open(election_data_path, 'r') as in_file:

        election_data = csv.reader(in_file)
        header = next(election_data)