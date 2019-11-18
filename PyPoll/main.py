# Eric Nordstrom
# November 18, 2019
# Second homework assignment for UT Data Analysis & Visualization boot camp
# Python 3.6.4


python_challenge_path = '..'  # assuming currently in python-challenge/PyPoll
import csv, sys
sys.path.insert(1, python_challenge_path)
import print_and_write as paw
import datetime as dt


"""DATA"""

election_data_path = '..\\..\\..\\UT-MCB-DATA-PT-11-2019-U-C/Homework/02-Python/Instructions/PyPoll/Resources\\election_data.csv'.replace('/','\\')  # path on my computer; replace with your path


"""RUN"""

if __name__ == '__main__':
    
    vote_counts = {}  # candidate: number of votes


    # read and record info

    with open(election_data_path, 'r') as in_file:

        election_data = csv.reader(in_file)
        header = next(election_data)

        for row in election_data:
