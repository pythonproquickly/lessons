import unittest
import autompgFINALDRAFT

# Test case for Part 2 the class AutoMPGData and class Record:
class TestAutoMPGData(unittest.TestCase):
    def test_autompgData_create(self):
        # initializes the class for __init__.
        autompg = autompgFINALDRAFT.AutoMPG(make = 'ford', model = 'toyota', year = '1975', mpg = '20.0')
        self.assertEqual(autompg.make, 'ford')
        self.assertEqual(autompg.model, 'toyota')
        self.assertEqual(autompg.year, '1975')
        self.assertEqual(autompg.mpg, '20.0')
        # However, in the AutoMPGData __init__ , we are just using _load_data.

    def test_iter_autompgData(self):
        autompg = autompgFINALDRAFT.AutoMPG(make = 'ford', model = 'toyota', year = '1975', mpg = '20.0')
        self.assertEqual(list(autompg),autompg.data)

        # The loadData function opens the data in a readable text file.
    def test_LoadData_autompgData(self):
        autompgDataFile = open("auto-mpgData.txt", "r")
# print(autompgDataFile.read())
    def test_cleanData_autompgData(self):
        # NEWautompgDataFile = open("auto-mpg.clean.txt", "w")
        NEWautompgDataFile = open("auto-mpg.clean.txt", "r")

# This is important in what we use to implement the above functionality and confirm that these tests are running successfully.
if __name__ == '__main__':
    unittest.main()

'''
You do not need to unittest the Record class
# Test case for class Record:
import collections
class TestRecord(unittest.TestCase):
#record = collections.namedtuple("record", "mpg cylinders displacement horsepower weight acceleration modelYear origin carName")
    def test_record(Record):
        autompg = autompgFINALDRAFT.AutoMPG(make = 'ford', model = 'toyota', year = '1975', mpg = '20.0')
        self.assertEqual(autompg, namedtuple("record", "mpg cylinders displacement horsepower weight acceleration modelYear origin carName"))

# This is important in what we use to implement the above functionality and confirm that these tests are running successfully.
if __name__ == '__main__':
    unittest.main()
'''
