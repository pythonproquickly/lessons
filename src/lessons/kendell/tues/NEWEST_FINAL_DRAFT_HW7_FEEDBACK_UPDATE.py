# Kendell Visser
# Dr. Siebrase
# COMP 3006 - Python Software Development
# HW Assignment Week 7

'''
HW 7, Step 1: Configure logging module
In autompg2.py configure the logging module as shown in the lecture so that it logs at the
DEBUG level into file autompg2.log and to the console at level INFO. Go back through the
code in autompg2.py and add logging calls at appropriate places. As new code is written in this
assignment, add logging calls as you go.
'''
import collections
import logging
import os
import csv
from collections import namedtuple
import requests
import ssl
import argparse


# Creating the basic Configuration and writing the data using logging at the Debug level.
logging.basicConfig(filename='AutoMPGData.log',
                    level=logging.DEBUG, filemode='w')

logging.debug('very detailed information')
logging.info('tracing info')
logging.warning('something bad might happen')
logging.error('something bad happened')
logging.critical('something really bad happened')

logger = logging.getLogger(__name__)
# makes sure debug messages are at least being processed.
logger.setLevel(logging.DEBUG)

# we can assess the name attribute of the logger object
# notice it is the __name__ variable of the module.
print(logger.name)

# create a file handler and set severity level.
# Notice that our logger is at level INFO and our
# handler is at DEBUG.  The handler will log anything at or above DEBUG,
# but the logger won't pass DEBUG to the handler.
'''
fh = logging.FileHandler('auto-mpg.clean1', 'w')
fh.setLevel(logging.DEBUG)
'''

fh = logging.FileHandler('auto-mpgCleanData.txt', 'w')
fh.setLevel(logging.DEBUG)

# create formatter
# see documentation for formatting.
# formatting here represents log level, logger name, module and log message
formatter = logging.Formatter(
    '%(levelname)s :: %(name)s :: %(module)s :: %(message)s')

# add formatter to file handler
fh.setFormatter(formatter)

# add file handler to logger
logger.addHandler(fh)  # add the handler to the root logger

# stream handler for DEBUG:
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
# INFO goes to console.
sh.setFormatter(formatter)
logger.addHandler(sh)

# No DEBUG information goes to console.
# These are just print statements originally from the class notes that helps print results to ensure the code is running:
for i in range(10):
    if i % 2 == 1:
        logger.debug('odd number encountered: {}'.format(i))
        logger.info('odd number encountered: {}'.format(i))


'''
Step 1: AutoMPG class: (From HW 6 -- See HW 6 for instructions in this section) I removed this comment for cleaner code.
'''


class AutoMPG:
    def __init__(self, make, model, year, mpg):
        self.make = make
        self.model = model
        self.year = year
        self.mpg = mpg

    # Create the __str__ to return the string representation of the object.
    def __str__(self):
        return f'A vehicle: {self.make}, {self.model}, {self.year}, {self.mpg}'

    # Create the __repr__ constructor to return the string representation of
    # the object in an alternate way.
    # print(__str__(self))
    def __repr__(self):
        return f'Vehicle({self.make}, {self.model}, {self.year}, {self.mpg})'

    # Note that an alternate way to call the __repr__(self) is by calling
    # the str(self) in the return statement.

    # Create the __eq__ equality comparison which Implements equality
    # comparison between two AutoMPG objects. Should use all four attributes
    # and should only work between AutoMPG objects.

    def __eq__(self, anotherObject):
        if type(self) == type(anotherObject):
            # Noting equality via the example given in the asynchronous exercise videos:
            return self.make == anotherObject.make and self.model == anotherObject.model and self.year == anotherObject.year and self.mpg == anotherObject.mpg
        else:
            # important to return NotImplemented instead of false.  Much easier for the Python console to run.
            return NotImplemented

    def __lt__(self, anotherObject):
        if type(self) == type(anotherObject):
            # The lt module allows us to use operators such as:
            # ==, !=, <, >, <=, and >= on comparison operators.
            # We are going to use < in this return statement since the
            # following is given to us in this assignment.
            # Implements LESS-THAN comparison between two AutoMPG objects.
            # Should use all four attributes in the order described above
            # (e.g., if the “make” is the same, then the
            # model should be used).

            # We need to use all 4 attributes; however, also only work
            # between AutoMPG objects it is for this reason that we are
            # using < instead of the ==
            return (self.make, self.model, self.year, self.mpg) < (anotherObject.make, anotherObject.model, anotherObject.year, anotherObject.mpg)
        else:
            return NotImplemented

# To implement the hash method now, we must put all of our 4 attributes into
# the hash "function" and call each attribute to the self Object:
    def __hash__(self):
        return hash((self.make, self.model, self.year, self.mpg))
# The hash function is to Implement an appropriate hash function for these objects.
# In test_autompg.py implement a test class and test cases that test all of the
# functionality above.


#myfile = open("auto-mpgData.txt")


# Citation of Given Data used in this project:
# Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.
'''
HW Assignment 6 Step 2: AutoMPGData class (From HW 6 -- See HW 6 for instructions in this section) I removed this comment for cleaner code.
'''

#from Kendell_Visser_HW_Assessment6_PART1.py import *


class Record:
    # Note in the namedtuple below, we can only have 2 inputs but the 9
    # attributes as the 2nd input can be separated by spaces because of our
    # expandtabs function above changing our delimiter to SPACES; the first
    # input is calling record which is similar to the "self" attributes defined
    # above, here we are calling this record since we define the class as record.
    # list
    record = collections.namedtuple(
        "record", "mpg cylinders displacement horsepower weight acceleration modelYear origin carName")


class AutoMPGData:

    def __init__(self):
        self.data = []  # instance attribute in __init__ function
        self._load_data()

    def __iter__(self):
        return iter(list(self.data))

    def _load_data(self):
        cleanRecord = Record.record
        if os.path.exists("auto-mpg.clean.txt") == False:
            self._clean_data()
            with open("auto-mpg.clean.txt") as cleanFile:
                AutoReader = csv.reader(
                    cleanFile, delimiter=" ", skipinitialspace=True)
                for row in AutoReader:
                    carRecord = cleanRecord(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    splitName = carRecord.carName.split()
                    makeName = splitName[1:]
                    self.data.append([splitName[0], " ".join(
                        makeName), "19" + str(carRecord.modelYear), carRecord.mpg])
                cleanFile.close()
        else:
            with open("auto-mpg.clean.txt") as cleanFile:
                AutoReader = csv.reader(
                    cleanFile, delimiter=" ", skipinitialspace=True)
                for row in AutoReader:
                    carRecord = cleanRecord(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    splitName = carRecord.carName.split()
                    makeName = splitName[1:]
                    self.data.append([splitName[0], " ".join(
                        makeName), "19" + str(carRecord.modelYear), carRecord.mpg])
                cleanFile.close()

    def _clean_data(self):
        # Call IN THE DATA TEXT FILE, "auto-mpgData.txt" to access the WHOLE (cleaned Data Set).
        # This first open file reads the data.
        with open("auto-mpgData.txt") as readFile:
            autoData = readFile.readlines()
            # This second interior open file will write to this text file of data.
            with open("auto-mpg.clean.txt", "w") as writeFile:
                for l in range(len(autoData)):
                    # applying the expandtabs method here on the string objects
                    # within the auto-mpgData file to change the TABS indents to
                    # just spaces.  Makes splitting and calling into program much
                    # easier delimited just by spaces, rather than some by Tabs
                    # and others by spaces.

                    # Use the csv module to parse each line with space delimiters
                    # and ignore multiple sequential delimiters.
                    writeFile.write(str.expandtabs(autoData[l], 3))
                writeFile.close()
            # remembering to close our file and the newly written file closed also.
            readFile.close()

    '''
    HW 7, Step 2: Add sorting to AutoMPGData class
    Enhance the AutoMPGData class by adding the following methods:
    • sort_by_default – This method should use the list.sort method to sort the data list in
    place. By default, list.sort will use the sorting implied by the less-than operator already
    implemented on the AutoMPG class. After this method is run, the list will be sorted by
    make, model, year, and then mpg.
    • sort_by_year – This method will use list.sort to sort the list in place but will override the
    default sorting by specifying the key= keyword parameter to list.sort to ensure that
    sorting happens by year, make, model, mpg.
    • sort_by_mpg – This method will use list.sort to sort the list in place but will override the
    default sorting so that the order is determined by mpg, make, model, year.
    '''

    def sort_by_default(self):
        self.data.sort()
        # list.sort(reverse=False)
    # sort_by_default will take the list of the Data which is now an INSTANCE ATTRIBUTE, and sort it with list.sort

    def sort_by_year(self):
        # key takes a function with lambda function for the key.  return order of values sorted.
        # We are using tuple comparison
        self.data.sort(key=lambda x: (x.year, x.make, x. model, x.mpg))
        # so need to also include make and model attributes in our lambda key value
        # function for list sorted.
        # call out the specific sort for the keyword year since we are doing a sort_by_year.
        self.data.sort(key=self.data.year)
         # sort data attribute the instance attribute from the list, self.data
    # Here we are going to overwrite the sort_by_default function, however the key word value will now be sorted by year.

    def sort_by_mpg(self):
            # key takes a function with lambda function for the key.  return order of values sorted.
            # We are using tuple comparison
            self.data.sort(key=lambda y: (y.mpg, y.make, y. model, y.year))
            # so need to also include make and model attributes in our lambda key value
            # function for list sorted. NOTICE Here though that mpg is First since we are sorting by mpg.
            # call out the specific sort for the keyword mpg since we are doing a sort_by_mpg.
            self.data.sort(key=self.data.mpg)

    '''
    HW 7, Step 3: Add capability to download Internet data
    Enhance the AutoMPGData class by adding the _get_data method. Please follow these
    guidelines for this method:
    • _get_data will be called by the _load_data method if the original data file (autompg.data.txt) does not exist.
    • This method should use the requests module to download the original data file from the
    UCI Machine Learning Repository and save it in the local file auto-mpg.data.txt.
    Test this functionality by removing the local data file and executing autompg2.py. It should
    download the data and then work as before.
    '''

    def _get_data(self):
    # uses requests module from website (recall the data from the citation is at:
    # https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data)
    # called by __load_data__
        """Download the original autoMPG data set from the web.  This is the autoMPGData called into the loadData function from HW 6."""
        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
        timeout = 0.2

        try:
            r = requests.get(url, timeout=timeout)
            r.raise_for_status()
            with open('auto-mpg.data.txt', 'w') as file:
                file.write(r.text)
        except requests.exceptions.ConnectionError as error:
            print(str(error))
        except requests.exceptions.Timeout as error:
            print(str(error))


'''
HW 7, Step 4:

Enhance command-line parsing
In autompg2.py use the argparse module to implement enhanced command-line parsing for this
program. The program should support the usage shown below. The only “command” supported
is “print”, which will iterate over the elements of the AutoMPGData collection (as it is sorted)
and print each one. The options to the “sort order” are “year”, “mpg”, and “default”, and the
result of these options is to call the corresponding “sort_by_XXX” method on the
AutoMPGData object before the data are printed.
usage: autompg2.py [-h] [-s <sort order>] <command>
analyze Auto MPG data set
positional arguments:
 <command> command to execute
optional arguments:
 -h, --help show this help message and exit
 -s <sort order>, --sort <sort order>
'''

# creater parser using the argparse module:
AutoParser = argparse.ArgumentParser(description="This program allows the user to \
sort AutoMPG objects by year, mpg, default.")
# By adding the following arguments for help and sort are 2 commands addressed in the
# problem above. Note that the sort_by_XXX just refers to the respectively named
# sort functions created in Part TWO: sort_by_default, sort_by_mpg, and sort_by_year.
AutoParser.add_argument('command', metavar='<command>',\
                        # print(help(metavar))
                        # NOTE THE DEFAULT NAME FOR THE ARGUMENT IN USAGE METHODS
                        # FOR THE add_argument() METHOD IS metavar.
                        # This is declaring the help function, next the -s function,
                        # we can call similar functions by adding more of the
                        # AutoParser.add_argument() functionalities.
                        choices=['print', '-p'],\
                        help='Please type print then choose year, mpg or default')
                    # This line sets up what is displayed to the user when they
                    # are confused of the output command line prompt, and gives them guidance.
AutoParser.add_argument('-s', '--sort', dest='sort',\
                        # action here stores, saves and sorts the data.
                        action='store', metavar='<sort order>',\
                        # NOTE THE DEFAULT NAME FOR THE ARGUMENT IN USAGE METHODS FOR THE add_argument() METHOD IS metavar.

                        choices=['year', 'mpg', 'default'],\
                        help='<sort order> = year || mpg || default')
# NOTE: When the following command line prompt is run to call in a sort,
# python3 autompgNEWESTFINALDRAFT2.py -s dest='year'
# The output is:
'''
__main__
INFO :: __main__ :: autompgNEWESTFINALDRAFT2 :: odd number encountered: 1
INFO :: __main__ :: autompgNEWESTFINALDRAFT2 :: odd number encountered: 3
INFO :: __main__ :: autompgNEWESTFINALDRAFT2 :: odd number encountered: 5
INFO :: __main__ :: autompgNEWESTFINALDRAFT2 :: odd number encountered: 7
INFO :: __main__ :: autompgNEWESTFINALDRAFT2 :: odd number encountered: 9
usage: autompgNEWESTFINALDRAFT2.py [-h] [-s <sort order>] <command>
autompgNEWESTFINALDRAFT2.py: error: argument -s/--sort: invalid choice: 'dest=year' (choose from 'year', 'mpg', 'default')
'''
# Notice the error is stating to choose 'year', 'mpg', or 'default'.

# Therefore, we can call the sort functions defined in Part 2.
# Call them argParser to actually run:

# ok
args = AutoParser.parse_args()


data = AutoMPGData()  # Recall this is an instance attribute defined earlier.
# if optional arg sort by option
# RECALL SIMILAR TO DEFINING THESE defs with a key word lambda function in part 2,
# that we had to use .data.sort.  In part 2, it was self.data.sort, but now our
# data is being stored in args, and thus, we should try to use args.data.sort instead
# when calling in our if statements for the arg parsing. (See Below):
# no args

############
#############
if args.sort == 'year':
    data.sort_by_year()
if args.sort == 'mpg':
    data.sort_by_mpg()
if args.sort == 'default':
    data.sort_by_default()
for a in data:
    if a[0] == "chevroelt":
        a[0] = "chevrolet"
    elif a[0] == "chevy":
        a[0] = "chevrolet"
    elif a[0] == "maxda":
        a[0] = "mazda"
    elif a[0] == "mercedes-benz":
        a[0] = "mercedes"
    elif a[0] == "toyouta":
        a[0] = "toyota"
    elif a[0] == "vokswagen":
        a[0] = "volkswagen"
    elif a[0] == "vw":
        a[0] = "volkswagen"
    print(a)

# NOTE THAT WHEN THE CODE IS RUN IN THE COMMAND LINE WITH THE FOLLOWING COMMAND PROMPT SINCE THE AUTOMPGDATA IS NOW ARGPARSED:
# python3 autompgNEWESTFINALDRAFT2.py -h
'''
Output of the Above Command Line Prompt is:
__main__
INFO :: __main__ :: autompgNEWESTFINALDRAFT2 :: odd number encountered: 1
INFO :: __main__ :: autompgNEWESTFINALDRAFT2 :: odd number encountered: 3
INFO :: __main__ :: autompgNEWESTFINALDRAFT2 :: odd number encountered: 5
INFO :: __main__ :: autompgNEWESTFINALDRAFT2 :: odd number encountered: 7
INFO :: __main__ :: autompgNEWESTFINALDRAFT2 :: odd number encountered: 9
usage: autompgNEWESTFINALDRAFT2.py [-h] [-s <sort order>] <command>

This program allows the user to sort AutoMPG objects by year, mpg, default.

positional arguments:
  <command>             Please type print

optional arguments:
  -h, --help            show this help message and exit
  -s <sort order>, --sort <sort order>
                        <sort order> = year || mpg || default
'''
# Notice that the autompgNEWESTFINALDRAFT2 file is being called and ran through the
# practice for loop at the INFO level... this is what gets passed to the file, however,
# if we actually open our file, we will see this sample for loop being run over BOTH
# The DEBUG AND INFO severity Levels.
# Additionally, this command line with -h will call the help file and shows that we can also
# call the -s prompt, which will direct the user to sort in a certain order, and thus
# running the Python Prompts from Part TWO that were defined as sort_by_default,
# sort_by_year, and sort_by_mpg.

# IT IS ALSO IMPORTANT TO NOTE THAT IF THIS ARGPARSE SECTION ABOVE IS COMMENTED OUT, the PROGRAM will
# OUTPUT THE FOLLOWING WITH THE ORIGINAL STRING OUTPUT FROM HW 6 AS WELL! BUT, WE DO NOT WANT A LOT OF
# OUTPUT ALL THE TIME!:
'''
OUTPUT WITH THE ARGPARSED SECTION ABOVE IN PART 4 COMMENTED OUT:
__main__
INFO :: __main__ :: autompgNEWESTFINALDRAFT2 :: odd number encountered: 1
INFO :: __main__ :: autompgNEWESTFINALDRAFT2 :: odd number encountered: 3
INFO :: __main__ :: autompgNEWESTFINALDRAFT2 :: odd number encountered: 5
INFO :: __main__ :: autompgNEWESTFINALDRAFT2 :: odd number encountered: 7
INFO :: __main__ :: autompgNEWESTFINALDRAFT2 :: odd number encountered: 9
A vehicle: chevrolet, chevelle malibu, 1970, 18.0
A vehicle: buick, skylark 320, 1970, 15.0
A vehicle: plymouth, satellite, 1970, 18.0
A vehicle: amc, rebel sst, 1970, 16.0
A vehicle: ford, torino, 1970, 17.0

'''


'''
# Some HW 6 instructions for clarity of next section:
• Use collections.namedtuple (OPTIONAL) to define a class called Record that has nine attributes that
correspond to the nine data fields in the same order as in the file.
• Using tuple packing/unpacking, assign the list returned by the csv module for a row to
create a Record object.
• Use the attributes of the Record object to pass the appropriate values to the constructor
for AutoMPG.
• You will need to use str.split and str.join (OPTIONAL) to pick out the make and model values from
the data since they are contained within “” in the data file, so will be returned by the csv
module as a single string value.
'''

# namedtuple


def main():
    # Call in the data file as an object.
    object = AutoMPGData()
    for a in range(len(object.data)):
        print("AutoMPGData({})".format(object.data[a]))
        # using the logging function defined above to call a debug function on the autoMPGData variable, a (auto)
        logging.debug(a)
        # writes this logging debug code to a new file called autompg2.log in the working directory.
        logging.basicConfig(filename='autompg2.log',
                            level=logging.INFO, filemode='w')

# main()
# This program when runs it outputs the AutoMPGData in the namedtuple as a list
# for each entry, in a similar format to the following:
# AutoMPGData(['Make', 'Model', 'VehicleYear', 'mpg'])
# The first line of output is:
# AutoMPGData(['chevrolet', 'chevelle malibu', '1970', '18.0'])


# print("\n") # In the output, makes the output seem cleaner with a space between
# the output for Part 2 and Part 3.
'''
HW Assignment 6 - Step 3: main (program). (From HW 6 -- See HW 6 for instructions in this section) I removed this comment for cleaner code.
'''

# Declare the AutoMPG class - NOTE BY UN COMMENTING THIS SECTION OF LINES THE
# OUTPUT WILL BE SIMILAR TO THE ABOVE OUTPUT WITH "MAKE: MODEL: YEAR: MPG: " titles.
# However, will overwrite the previous declared AutoMPG class above, and change
# its f string. NOTE THAT IF YOU USE MY PART 3 PYTHON SCRIPT, it will be
# outputted with the strings used in AutoMPG1 class below.
"""
class AutoMPG1:
    # Constructor in Python - Used initialize the class attributes
    # Note that this __init__ module is being re assigned but is the same code
    # from Step 1.
    def __init__(self, make, model, year, mpg):
        # inits for our four attributes we are interested in to compare object
        # self to, respectively, make, model, year, and mileage (mpg).
        self.make = make
        self.model = model
        self.year = year
        self.mpg = mpg
    # The __str__ method prints the details of the AutoMPG objects
    def __str__(self):
        # Print the make, model, year and mileage with Headers as desired in the
        # given output above:
        return "Make: {}, Model: {}, Year: {}, mpg: {}".format(self.make, self.model, self.year, self.mpg)
"""


"""def main():
    # Create an empty list to store the different autos
    autoMpgList = []
    # Create an instance of the AutoMPG named autoCar1
    autoCar1 = AutoMPG('chevrolet', 'chevelle malibu', 1970, 18.0)
    # Create an instance of the AutoMPG named autoCar2
    autoCar2 = AutoMPG('buick', 'skylark 320', 1970, 15.0)
    # Create an instance of the AutoMPG named autoCar3
    autoCar3 = AutoMPG('plymouth', 'satellite', 1970, 18.0)
    # Create an instance of the AutoMPG named autoCar4
    autoCar4 = AutoMPG('amc', 'rebel sst', 1970, 16.0)
    # Create an instance of the AutoMPG named autoCar5
    autoCar5 = AutoMPG('ford', 'torino', 1970, 17.0)
    # Append each auto to the autoMpgList
    # Append autoCar1 to autoMpgList
    autoMpgList.append(autoCar1)
    # Append autoCar2 to autoMpgList
    autoMpgList.append(autoCar2)
    # Append autoCar3 to autoMpgList
    autoMpgList.append(autoCar3)
    # Append autoCar4 to autoMpgList
    autoMpgList.append(autoCar4)
    # Append autoCar5 to autoMpgList
    autoMpgList.append(autoCar5)"""
# This can be appended 398 more times if we wanted to but in the output that is
# given in the question, it only has the first 5 entries.  Note that in Step 2,
# the autoMpgList is looped with the iterator across all of the values in the
# output of AutoMPGData.
    # Loop the autoMpgList using the in iterator and print the details of the auto
"""for auto in autoMpgList:
    print(auto)"""
# use argparse for command line functions here including print

# Using the __name__ magic method module to call the main program and actually
# run the AutoMPG function in Python.


if __name__ == '__main__':
    main()

'''
if __name__ == '__logmain__':
    logmain()
'''
