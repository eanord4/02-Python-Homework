# Eric Nordstrom
# November 18, 2019
# second homework assignment for UT Data Analysis & Visualization boot camp
# Python 3.6.4


python_challenge_path = 'C:/users/eanor.LORDSTROM/Dropbox/Documents/Education/Data Analysis & Viz Boot Camp/Homework/02-Python'  # path on my computer; replace with your path
import csv, sys
sys.path.insert(1, python_challenge_path)  # for next import: path on my computer; allows running from any directory
sys.path.insert(2, '..')  # for next import: up one level if currently in PyBank folder; allows running on any computer if in this folder
import print_and_write as paw
import datetime as dt


"""DATA"""

budget_data_path = 'C:/users/eanor.LORDSTROM/Dropbox/Documents/Education/Data Analysis & Viz Boot Camp/UT-MCB-DATA-PT-11-2019-U-C/Homework/02-Python/Instructions/PyBank/Resources/budget_data.csv'  # path on my computer; replace with your path

month_indices = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
}

month_abbreviations = {item[1]: item[0] for item in month_indices.items()}  # flips keys and values of "month_indices" dict


"""FUNCTIONS"""

def date(month_str):
    '''returns datetime.date object from the month and year based on an input string of format "Jan-2000"'''

    entry = month_str.split('-')
    return dt.date(int(entry[1]), month_indices[entry[0]], 1)  # first day of the month

def next_month(date_object):
    '''add 1 month to the input datetime.date object'''

    if date_object.month == 12:
        return dt.date(date_object.year + 1, 1, date_object.day)
    
    return dt.date(date_object.year, date_object.month + 1, date_object.day)

def record_missing(first_date, last_date):
    '''place all months between first_date and last_date (exclusive) in "missing_months"'''

    global missing_months
    this_date = next_month(first_date)

    while this_date < last_date:
        missing_months.add(this_date)
        this_date = next_month(this_date)

def months_difference(first_date, last_date):
    '''the number of months between the first_date and last_date provided'''

    return last_date.month - first_date.month + 12 * (last_date.year - first_date.year)


"""RUN"""

if __name__ == '__main__':

    print()
    timestamp = dt.datetime.now()  # save timestamp in case script to be run multiple times


    # read and record info

    with open(budget_data_path, 'r') as in_file:

        budget_data = csv.reader(in_file)
        header = next(budget_data)
        first_row = next(budget_data)
        
        # months: looks like the months go one-by-one (each row is exactly one month later than the previous), but we can keep track if any are missing.
        missing_months = set()
        start_date = end_date = date(first_row[0])

        # profit/losses: keep track of sum, max, min; assume at end that the divisor for the average is the number of months in the dataset
        net_profit = 0
        max_profit = min_profit = float(first_row[1])
        max_profit_month = min_profit_month = start_date

        for row in budget_data:

            ## UPDATE MONTHS ##

            new_date = date(row[0])
            diff = months_difference(end_date, new_date)

            if diff > 0:
                record_missing(end_date, new_date)
                end_date = new_date
            
            elif diff < 0:
                if new_date in missing_months:
                    missing_months.remove(new_date)
                elif new_date < start_date:
                    record_missing(new_date, start_date)
                    start_date = new_date
            

            ## UPDATE PROFIT INFO ##

            new_profit = float(row[1])
            net_profit += new_profit

            if new_profit > max_profit:
                max_profit = new_profit
                max_profit_month = new_date
            elif new_profit < min_profit:
                min_profit = new_profit
                min_profit_month = new_date
    

    # write and print

    with open('output_file.txt', 'a') as out_file:
        
        paw.write_like_print(out_file, timestamp)
        paw.write_like_print(out_file)
    

        ## MONTHS REPORT ##

        paw.print_and_write(out_file, '~~~ DATASET OVERVIEW ~~~')  # gets its own section because it was not previously known whether any months would be missing between the first and the last
        paw.print_and_write(out_file, 'First month:', month_abbreviations[start_date.month], start_date.year)
        paw.print_and_write(out_file, 'Last month:', month_abbreviations[end_date.month], end_date.year)
        paw.print_and_write(out_file, 'Missing months:', len(missing_months))

        for item in sorted(missing_months):
            paw.print_and_write(out_file, '\t' + month_abbreviations[item.month], item.year)
        
        total_months = months_difference(start_date, end_date) - len(missing_months) + 1
        paw.print_and_write(out_file, 'Total number of months:', total_months)


        ## PROFIT REPORT ##

        paw.print_and_write(out_file)
        paw.print_and_write(out_file, '~~~ FINANCIAL ANALYSIS ~~~')
        paw.print_and_write(out_file, 'Net profit:', net_profit)
        paw.print_and_write(out_file, 'Average monthly profit:', round(net_profit / total_months, 2))
        display_max_profit_month = ' '.join((month_abbreviations[max_profit_month.month], str(max_profit_month.year)))
        display_min_profit_month = ' '.join((month_abbreviations[min_profit_month.month], str(min_profit_month.year)))
        paw.print_and_write(out_file, f'Maximum monthly profit: {round(max_profit, 2)} ({display_max_profit_month})')
        paw.print_and_write(out_file, f'Minimum monthly profit: {round(min_profit, 2)} ({display_min_profit_month})')


        paw.write_like_print(out_file)
        paw.write_like_print(out_file)
