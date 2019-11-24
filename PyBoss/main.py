# Eric Nordstrom
# November 22, 2019
# Second homework assignment for UT Data Analysis & Visualization boot camp - optional additional content
# Python 3.6.4


import csv


"""DATA"""

old_data_path = 'C:/users/eanor.LORDSTROM/Dropbox/Documents/Education/Data Analysis & Viz Boot Camp/UT-MCB-DATA-PT-11-2019-U-C/Homework/02-Python/ExtraContent/Instructions/PyBoss/employee_data.csv'  # path on my computer; replace with your path
new_data_path = 'converted_employee_data.csv'

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}  # source: https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5


"""FUNCTIONS"""

def new_row(row):
    '''new_row(row) --> convert the row to the new format'''

    emp_ID = row[0]

    first_name, last_name = row[1].split()

    year, month, day = row[2].split('-')
    new_DOB = '/'.join((month, day, year))

    last_4_SSN = row[3].split('-')[-1]
    new_SSN = '***-**-' + last_4_SSN

    state_abbrev = us_state_abbrev[row[4]]

    return emp_ID, first_name, last_name, new_DOB, new_SSN, state_abbrev

def convert_employee_data(in_file_path, out_file_path):
    '''convert_employee_data(in_file_path, out_file_path) --> convert the data to the new format'''
    
    print('Converting...')

    try:
        with open(in_file_path, 'r') as in_file, open(out_file_path, 'a') as out_file:

            old_data = csv.reader(in_file)
            new_data = csv.writer(out_file)

            old_header = next(old_data)
            new_header = ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']
            new_data.writerow(new_header)

            for row in old_data:
                new_data.writerow(new_row(row))
            
        print('Successfully converted data.')

    except ValueError:
        print('Got ValueError. Original row:')  # catch row at which error occurred
        print(row)


"""RUN"""

if __name__ == '__main__':
    convert_employee_data(old_data_path, new_data_path)