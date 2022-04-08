'''
Step 2: Unit Testing
Create a new program, test_compute_stats2.py, that contains the unit tests for the
compute_stats function described above. This code should use the unittest module as
described in lecture, import the compute_stats2 module, and make calls to the
compute_stats2.compute_stats function to test it. The core functionality should be tested with
a list containing an even number of elements and an odd number. Corner cases such as an
empty list (should return None for all the values) and a list with a single element should also be
tested.
'''
#import __main__
import unittest
import comp_week2_stats_original
# from comp_week2_stats_original import main
#from comp_week2_stats_original import *
import compute_stats2
import sys
import csv
#print(sys.argv)
#print(sys.exc_info())
#import compute_stats as compute_stats2
#coreList =[]
#compute_stats2.compute_stats from compute_stats2
#if __name__ == '__main__':
#    values = [1,3,5,7,9,11,13,15,17,19, 21] # Assume we have these values
#return()


class Test_compute_stats2(unittest.TestCase):
    def test_compute_stats2(self):
        self.assertEqual(compute_stats2.compute_stats([1,2,3,4,5,6,7,8,9,10]), (1, 10, 5.5, 5.5)) # Even
        self.assertEqual(compute_stats2.compute_stats([1,2,3,4,5,6,7,8,9]), (1, 9, 5.0, 5.0)) # Odd
        self.assertEqual(compute_stats2.compute_stats([]), None) # Empty list
        self.assertEqual(compute_stats2.compute_stats([2]), None) # One element

if __name__ == '__main__':
    unittest.main()

'''
Step 3: More Flexible Input Processing
To make this program more flexible and easy to use, it should be changed to accept the whole
data file (not just a single column), and the data should not need to be sorted.
Change compute_stats2.py so that it takes a single command line argument that is an integer
specifying which whitespace separated column it should process. For the user, column numbers
start at 1.
Since the program is going to be processing the whole file rather than just a single column of
numbers, we will use the csv module to parse it. Read the csv.reader documentation to figure
out how to specify spaces as the delimiter in the file and how to skip over multiple delimiters in
a row (if you don’t do this, each individual space will be considered a delimiter, which is not
going to work well).
Finally, change your program so that it does not require the input values to be sorted already
(i.e., it should sort the values itself before passing to the compute_stats function).
After making these improvements, the script could be called as such:
python3 compute_stats2.py 9 < Data.txt
'''

#import pandas as pd
#read_file = pd.read_csv (r'mnt/c/Users/Owner/Documents/University of Denver - MS Data Science Coursework/COMP 3006 - Python Software Development 2/Weekly HW Assignments/HW Assignment 2/new_data.txt')
#read_file.to_csv (r'mnt/c/Users/Owner/Documents/University of Denver - MS Data Science Coursework/COMP 3006 - Python Software Development 2/Weekly HW Assignments/HW Assignment 2/new_data.csv', index=None)
# DO NOT USE PANDAS!:
# import csv (see top of file for this import)

read_file = read_csv (r'c/Users/Owner/Documents/University of Denver - MS Data Science Coursework/COMP 3006 - Python Software Development 2/Weekly HW Assignments/HW Assignment 2/new_data.txt')
read_file.to_csv (r'c/Users/Owner/Documents/University of Denver - MS Data Science Coursework/COMP 3006 - Python Software Development 2/Weekly HW Assignments/HW Assignment 2/new_data.csv', index=None)


with open('Data.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('Data.csv', 'w') as out_file:
        writer = csv.writer(out_file)
#        writer.writerow(('title', 'intro'))
        writer.writerows(lines)


'''
Step 4: Optional File Name
Change compute_stats2.py so that it takes an optional second command-line argument that
specifies a file to use instead of reading from standard input. The existing functionality should
work, but after this change the program can take a file name and read from that. E.g.:
python3 compute_stats2.py 9 Data.txt
'''
