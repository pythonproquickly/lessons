# Kendell Visser
# Dr. Siebrase
# COMP 3006 - Python Software Development
# HW Assignment Week 6

'''
Step 1: AutoMPG class:
In autompg.py implement a class that represents these attributes that are available for each
record in the data set:
• make – String. Automobile manufacturer. First token in the “car name” field of the data
set.
• model – String. Automobile model. All the other tokens in the “car name” field of the
data set except the first.
• year – Integer. Automobile year of manufacturer. This is the four-digit year that
corresponds to the “model year” field of the data set.
• mpg – Floag. Miles per gallon. This is a floating point value that corresponds to the
“mpg” field of the data set.
This class should implement the following methods:
• __init__ – Constructor that takes four parameters after self and initializes the attributes
described above.
• __repr__ and __str__ – Returns the string representation of the object. One of these can
call the other one.
• __eq__ – Implements equality comparison between two AutoMPG objects. Should use
all four attributes and should only work between AutoMPG objects.
• __lt__ – Implements less-than comparison between two AutoMPG objects. Should use
all four attributes in the order described above (e.g., if the “make” is the same, then the
model should be used).
• __hash__ – Implement an appropriate hash function for these objects.
In test_autompg.py implement a test class and test cases that test all of the functionality above
'''
class AutoMPG:
    # By default, this class is INITIALLY HASHABLE!
        # instance attributes
        # Create the __init__ constructor that takes the four parameters after
        # self and initializes the attributes described above.
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
        #print(__str__(self))
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
                return False
            #    NotImplemented

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
                return self.make < anotherObject.make and self.model < anotherObject.model and self.year < anotherObject.year and self.mpg < anotherObject.mpg
            #else:
                #NotImplemented

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
HW Assignment 6 Step 2: AutoMPGData class
In autompg.py define the AutoMPGData class. This class represents the entire AutoMPG data
set. It has a single attribute data that is a list of AutoMPG objects. One issue with the Auto
MPG data set is that in the data file, most of the fields are separated by spaces, but the separator
before the “car name” field is a TAB character. This makes it difficult to parse with Python’s csv
module, so there is a method described below (_clean_data) that takes care of this and saves the
“cleaned” data file in auto-mpg.clean.txt.
This class should implement these methods:
• __init__ – Constructor that takes no arguments. It should call the _load_data method
described below.
• __iter__ – Method to make the class iterable. It should return an iterator over the data
list.
• _load_data – Method that will load the cleaned data file (auto-mpg.clean.txt) and
instantiate AutoMPG objects and add them to the data attribute. See below for more
details about a useful technique for parsing the data. This method should call
_clean_data if the clean data file does not exist. (Hint: Use os.path.exists to check this.)
• _clean_data – Method that will read the original data file line by line (autompg.data.txt) and use the expandtabs method available on str objects to convert the
TAB character to spaces. Each line should be written to the “cleaned” file autompg.clean.txt.
Parsing Notes
The main goal of the _load_data method is to read in the data file and instantiate objects of type
AutoMPG using a few of the fields that are available. Here are some notes about how to
accomplish this:
• Use the csv module to parse each line with space delimiters and ignore multiple
sequential delimiters.
• This will give you a list of nine elements that correspond to the columns in the data file.
• Use collections.namedtuple to define a class called Record that has nine attributes that
correspond to the nine data fields in the same order as in the file.
• Using tuple packing/unpacking, assign the list returned by the csv module for a row to
create a Record object.
• Use the attributes of the Record object to pass the appropriate values to the constructor
for AutoMPG.
• You will need to use str.split and str.join to pick out the make and model values from
the data since they are contained within “” in the data file, so will be returned by the csv
module as a single string value.
Implement a test class and test cases in test_autompg.py to ensure the functionality above.

'''

import csv, collections, os
#from Kendell_Visser_HW_Assessment6_PART1.py import *
class AutoMPGData:
    # We need to create this empty list as an instance attribute and then call the loadData method for the init method.
    data = []
    # Note that the __init__ function is not taking any arguments. self is
    # not an attribute, but simplay a "default object".
    # __init__ is Constructor that takes no arguments. It should call the _load_data method
    # described below.
    def __init__(self):
        self._load_data()

    # Method to make the class iterable. It should return an iterator over the data
    # list, so we need to call list(self.data).
    def __iter__(self):
        return iter(list(self.data))

    #  Method that will load the cleaned data file (auto-mpg.clean.txt) and
    # instantiate AutoMPG objects and add them to the data attribute. See below for more
    # details about a useful technique for parsing the data. This method should call
    # _clean_data if the clean data file does not exist. (Hint: Use os.path.exists to check this.)
    def _load_data(self):
        cleanRecord = Record.record
        # Using the os.path.exists() function and setting it = to False, we are
        # seeing if _clean_data file DOOES NOT EXIST.  If not, this method will
        # perform.
        if os.path.exists("auto-mpg.clean.txt") == False:
            # calling the clean_data function if this text of data is NOT found
            # in the working directory.
            self._clean_data()
            with open ("auto-mpg.clean.txt") as cleanFile:
                AutoReader = csv.reader(cleanFile, delimiter= " ", skipinitialspace=True)
                for row in AutoReader:
                    carRecord = cleanRecord(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    splitName = carRecord.carName.split()
                    makeName = splitName[1:]
                    AutoMPGData.data.append([splitName[0], " ".join(makeName), "19"+str(carRecord.modelYear), carRecord.mpg])
                cleanFile.close()
        else:
            # Notice the code for the else statement is very similar to that of
            # the if statement above for the "auto-mpg.clean.txt" file, since we
            # want the data to be cleaned and executed correctly, whether the
            # desired file called is or is not in the working directory.

            # Note since the "auto-mpg.clean.txt" file DOES exist in the
            # working directory, the following will execute, and thus will
            # display a _clean_data of the whole AutoMPGData function printing
            # the whole text file within the function.
            with open("auto-mpg.clean.txt") as cleanFile:
                AutoReader = csv.reader(cleanFile, delimiter= " ", skipinitialspace=True)
                for row in AutoReader:
                    # This will give you a list of nine elements that correspond
                    # to the columns in the data file.
                    carRecord = cleanRecord(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    splitName = carRecord.carName.split()
                    makeName = splitName[1:]
                    # Note the 19 in string below is added in front of the car
                    # year as denoted by carRecord.modelYear since these are
                    # vehicles from the 1900s.
                    AutoMPGData.data.append([splitName[0], " ".join(makeName), "19"+str(carRecord.modelYear), carRecord.mpg])
                cleanFile.close()
# _clean_data is a Method that will read the original data file line by line
# (autompg.data.txt) and use the expandtabs method available on str objects
# to convert the TAB character to spaces. Each line should be written to the
# “cleaned” file autompg.clean.txt.
'''
The main goal of the _load_data method is to read in the data file and instantiate objects of type
AutoMPG using a few of the fields that are available. Here are some notes about how to
accomplish this:
• Use the csv module to parse each line with space delimiters and ignore multiple
sequential delimiters.
• This will give you a list of nine elements that correspond to the columns in the data file.
'''
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
                writeFile.write(str.expandtabs(autoData[l],3))
            writeFile.close()
        readFile.close() # remembering to close our file and the newly written file closed also.

'''
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


class Record:
    # Note in the namedtuple below, we can only have 2 inputs but the 9
    # attributes as the 2nd input can be separated by spaces because of our
    # expandtabs function above changing our delimiter to SPACES; the first
    # input is calling record which is similar to the "self" attributes defined
    # above, here we are calling this record since we define the class as record.
    record = collections.namedtuple("record", "mpg cylinders displacement horsepower weight acceleration modelYear origin carName")


def main():
    # Call in the data file as an object.
    object = AutoMPGData()
    for a in range(len(object.data)):
        print("AutoMPGData({})".format(object.data[a]))

#main()
# This program when runs it outputs the AutoMPGData in the namedtuple as a list
# for each entry, in a similar format to the following:
# AutoMPGData(['Make', 'Model', 'VehicleYear', 'mpg'])
# The first line of output is:
# AutoMPGData(['chevrolet', 'chevelle malibu', '1970', '18.0'])

#print("\n") # In the output, makes the output seem cleaner with a space between
# the output for Part 2 and Part 3.
'''
HW Assignment 6 - Step 3: main (program).
In autompg.py implement a main function that instantiates an AutoMPGData object and then
uses the iterator protocol (e.g., for a in AutoMPGData():) to loop across the object, printing
each AutoMPG object. For example, the output should look like this:
> python3 autompg.py
AutoMPG('chevrolet','chevelle malibu',1970,18.0)
AutoMPG('buick','skylark 320',1970,15.0)
AutoMPG('plymouth','satellite',1970,18.0)
AutoMPG('amc','rebel sst',1970,16.0)
AutoMPG('ford','torino',1970,17.0)


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
def main():
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
    autoMpgList.append(autoCar5)
# This can be appended 398 more times if we wanted to but in the output that is
# given in the question, it only has the first 5 entries.  Note that in Step 2,
# the autoMpgList is looped with the iterator across all of the values in the
# output of AutoMPGData.
    #Loop the autoMpgList using the in iterator and print the details of the auto
    for auto in autoMpgList:
        print(auto)

# Using the __name__ magic method module to call the main program and actually
# run the AutoMPG function in Python.
if __name__ == '__main__':
    main()
