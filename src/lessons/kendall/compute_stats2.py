# Kendell Visser
# COMP 3006 - Python Software Development 2
# Dr. Ben Siebrase
# DUE: 2 April, 2022 at 11:59 PM
# HW Assessment 1
'''
In this part of the assignment, you will implement a Python script that reads data from standard
input, computes some basic statistics over the values that are read in, and writes those
statistics to standard output. This program will be implemented in a file called
compute_stats.py.
This program will assume that the data is read in a stream of numbers, one per line. The data
coming in will have already been sorted numerically in ascending order (i.e., what you did in
Part 1). There might be “missing-data” values (read the data file documentation) that must be
ignored when computing the statistics.
The statistics that must be computed are
1) Average value
2) Minimum value
3) Maximum value
4) Median value
Before your program terminates, it should print the computed values formatted similar to the
following:
min: -17.9, max: 17.1, average: 2.54148, median: 1.65

'''


import statistics
import sys
import csv
# ENSURE THE FOLLOWING BASH COMMAND LINES ARE RUN IN WSL AND IN SAME WORKING
# DIRECTORY BEFORE PROCEEDING:
'''
IMPORTANT NOTES FROM THE DATA FILE DOCUMENTATION FOR CUT COMMAND IN PART 1.a:
9    T_DAILY_AVG  [7 chars]  cols 63 -- 69
          Average air temperature, in degrees C. See Note F.

F.  The daily values reported in this dataset are calculated using
            multiple independent measurements for temperature and precipitation.
            USCRN/USRCRN stations have multiple co-located temperature sensors
            that make 10-second independent measurements which are used to
            produce max/min/avg temperature values at 5-minute intervals. The
            precipitation gauge is equipped with multiple load cell sensors to
            provide independent measurements of depth change at 5-minute
            intervals.


Step 1.a: Extract the column of data for Field 9, T_DAILY_AVG using
the command line cut:
Bash Command Line is: cut -b 63-69 Data.txt > T_DAILY_AVG.txt

Step 1.b: Sort the column of data. The sorted data should be
saved in a file named T_DAILY_AVG_sorted.txt
Bash Command Line is: sort -g  T_DAILY_AVG.txt > T_DAILY_AVG_sorted.txt

Step 1.c: Do it in a pipeline.  As shown in lecture, commands can be combined in
a pipeline without saving the intermediate data into files, so we could do all
of the above in one shot so that the numerically sorted, ascending data is piped
directly to a Python program something like this:
Bash Command Line is: cut -b 63-69 Data.txt | sort -g | python3 compute_stats.py

# STEP 1.C IS THE CALL LINE INTO BASH TO RUN THIS PROGRAM without further action
of 1.a and 1.b.

'''

def compute_stats(values):
	if len(values) == 0:
		return None
	o_min = values[0]
	# Since the list is already Sorted in ascending order and the null values have
	# been ignored, thus our first value will be the minimum value.  Do note that
	# the first value is at position 0, and thus we call an index of [0] instead
	# of [1].
	o_max = values[-1]
	# Similar to the minimum, we know that the last number is the maximum value
	# because our values are already sorted in ascending order, and note that the
	# shortcut to call the last value is the index position value of [-1].
	o_avg = sum(values) / len(values)
	# Find the average of the StreamNumbers list will be taking the sum of all of
	# them and dividing by how many numbers there are in the list; the len length
	# function will give us the total number of values in the list and we can divide
	# this number by the sum to calculate the average value.
	middleNumber = len(values) // 2
	# Find the middle element in the list.  This will be the Outputted median if the
	# number of elements in the list is odd; notice the mod 2 division denoted by //
	o_median = (values[middleNumber] + values[~middleNumber]) / 2
	# In the event that there is an EVEN number of elements in the given list, this
	# function will take the sum of the middle 2 numbers, and divide by 2 to find
	# the center of these values, also known as our median value as desired.

	# Print the results
	# print('min: %g, max: %g, average: %g, median: %g' % (
	# Minimum_T_DAILY_AVG, Maximum_T_DAILY_AVG, Average_T_DAILY_AVG,
	# Median_T_DAILY_AVG))

	return o_min, o_max, o_avg, o_median

def main(column, filename):
	column -= 1
	# Read in the data that was cut and sorted into the T_DAILY_AVG_sorted.txt file
	# in part 1.
	file = open(filename, 'r')
	reader = sorted(list(csv.reader(file, delimiter=' ', skipinitialspace=True)))
	T_DAILY_AVG_text_sorted = file.read()
	#print(T_DAILY_AVG_text_sorted)
	# StreamNumbers = list() # Creating an empty list for the values being read to be
	# able to be structured into a List.

	'''
	AN IMPORTANT NOTE FROM THE DATA FILE DOCUMENTATION IS:
		 C.  Missing data are indicated by the lowest possible integer for a
				given column format, such as -9999.0 for 7-character fields with
				one decimal place or -99.000 for 7-character fields with three
				decimal places.
	THEREFORE IN THE T_DAILY_AVG_text_sorted, THE INITIAL VALUE OF -9999.0 SHOULD
	BE IGNORED!
	'''
	# While the StreamNumbers list is Empty:
	StreamNumbers = list()
	# Run a while loop throughout the data until there is an End of File (EOF), in
	# other words, an infinite loop.
	for item in reader:
		Values_to_Input = item[column]
		if Values_to_Input == '-9999.0' or Values_to_Input == '-99.000':	# skip the missing values
			continue
		# From Note C in the Documentation File above, We want to skip the
		# values of -9999.0, which is the head, first value in the read in data
		# text file, T_DAILY_AVG_text_sorted
		# By converting our inputted values to a float, we are changing the text
		# file from a string format to a more integer format, where decimal values
		# are included.
		StreamNumbers.append(float(Values_to_Input))
		# By using the append command, we are able to put our newly converted float
		# values into the empty list that was created and named StreamNumbers.
	Minimum_T_DAILY_AVG, Maximum_T_DAILY_AVG, Average_T_DAILY_AVG, Median_T_DAILY_AVG = compute_stats(StreamNumbers)

	print("The minimum value is: ", Minimum_T_DAILY_AVG)
	print("The maximum value is: ", Maximum_T_DAILY_AVG)
	print("The average value is: ", Average_T_DAILY_AVG)
	print("The median value is: ", Median_T_DAILY_AVG)

	'''
	The outputting results for the given data set using the following bash command:
	cut -b 63-69 Data.txt | sort -g | python3 compute_stats.py
	
	RESULTS:
	The minimum value is:  -17.9
	The maximum value is:  17.1
	The average value is:  2.5414835164835154
	The median value is:  1.65
	
	'''

if __name__ =="__main__":
	if len(sys.argv) < 2:
		print("Must specify a column number and filename")
		exit()
	column = int(sys.argv[1])
	filename = sys.argv[2]
	main(column, filename)
