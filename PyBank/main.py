import csv
import datetime as dt


"""DATA"""

budget_data_path = "..\\..\\..\\UT-MCB-DATA-PT-11-2019-U-C\\Homework\\02-Python\\Instructions\\PyBank\\Resources\\budget_data.csv"  # replace with your path to the budget_data.csv file

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

def write_like_print(*args, end='\n', sep=' '):
    '''write_like_print(*args, end='\n', sep=' ') --> append to the output file as the print() function would print to the console'''

    global out_file
    out_file.write(sep.join(str(arg) for arg in args) + end)

def print_and_write(*args, end='\n', sep=' '):
    '''print_and_write(*args, end='\n', sep=' ') --> print and append to output file'''

    global out_file
    print(*args, end=end, sep=sep)
    write_like_print(*args, end=end, sep=sep)


"""RUN"""

if __name__ == '__main__':

    print()
    now = dt.datetime.now()

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

        for line in budget_data:

            ## UPDATE MONTHS ##

            new_date = date(line[0])
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

            new_profit = float(line[1])
            net_profit += new_profit

            if new_profit > max_profit:
                max_profit = new_profit
                max_profit_month = new_date
            elif new_profit < min_profit:
                min_profit = new_profit
                min_profit_month = new_date
    

    with open('output_file.txt', 'a') as out_file:

        write_like_print(now)
        write_like_print()
    

        ## MONTHS REPORT ##

        print_and_write('~~~ DATASET OVERVIEW ~~~')  # gets its own section because it was not previously known whether any months would be missing between the first and the last
        print_and_write('First month:', month_abbreviations[start_date.month], start_date.year)
        print_and_write('Last month:', month_abbreviations[end_date.month], end_date.year)
        print_and_write('Missing months:', len(missing_months))

        for item in sorted(missing_months):
            print_and_write('\t' + month_abbreviations[item.month], item.year)
        
        total_months = months_difference(start_date, end_date) - len(missing_months) + 1
        print_and_write('Total number of months:', total_months)


        ## PROFIT REPORT ##

        print_and_write()
        print_and_write('~~~ FINANCIAL ANALYSIS ~~~')
        print_and_write('Net profit:', net_profit)
        print_and_write('Average monthly profit:', round(net_profit / total_months, 2))
        print_and_write('Maximum monthly profit:', month_abbreviations[max_profit_month.month] + str(max_profit_month.year), round(max_profit, 2), sep='\t')
        print_and_write('Minimum monthly profit:', month_abbreviations[min_profit_month.month] + str(min_profit_month.year), round(min_profit, 2), sep='\t')


        write_like_print()
        write_like_print()
