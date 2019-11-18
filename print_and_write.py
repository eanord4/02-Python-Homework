# Eric Nordstrom
# November 18, 2019
# for second homework submission - UT Data Analysis and Visualization boot camp
# general functions related to printing and writing to files
# Python 3.6.4


def write_like_print(out_file, *args, end='\n', sep=' '):
    '''write_like_print(out_file, *args, end='\n', sep=' ') --> append to the output file as the print() function would print to the console'''

    out_file.write(sep.join(str(arg) for arg in args) + end)

def print_and_write(out_file, *args, end='\n', sep=' '):
    '''print_and_write(out_file, *args, end='\n', sep=' ') --> print and append to output file'''

    print(*args, end=end, sep=sep)
    write_like_print(out_file, *args, end=end, sep=sep)