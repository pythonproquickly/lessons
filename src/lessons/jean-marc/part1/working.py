# In a file called working.py, implement a function called convert that expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

# Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

# Either before or after you implement convert in working.py, additionally implement, in a file called test_working.py, three or more functions that collectively test your implementation of convert thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

# pytest test_working.py

# Hints
# Recall that the re module comes with quite a few functions, per docs.python.org/3/library/re.html, including search.
# Recall that regular expressions support quite a few special characters, per docs.python.org/3/library/re.html#regular-expression-syntax.
# Because backslashes in regular expressions could be mistaken for escape sequences (like \n), best to use Python’s raw string notation for regular expression patterns, else pytest will warn with DeprecationWarning: invalid escape sequence. Just as format strings are prefixed with f, so are raw strings prefixed with r. For instance, instead of "harvard\.edu", use r"harvard\.edu".
# Note that re.search, if passed a pattern with “capturing groups” (i.e., parentheses), returns a “s object,” per docs.python.org/3/library/re.html#s-objects, wherein ses are 1-indexed, which you can access individually with group, per docs.python.org/3/library/re.html#re.s.group, or collectively with groups, per docs.python.org/3/library/re.html#re.s.groups.
# Note that you can format an int with leading zeroes with code like
# print(f"{n:02}")
# wherein, if n is a single digit, it will be prefixed with one 0, per docs.python.org/3/library/string.html#format-string-syntax.


import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        fr_hr, to_hr = s.split(" to ")
        con_dic = {"12AM":"00","1AM":"01","2AM":"02","3AM":"03","4AM":"04","5AM":"05","6AM":"06","7AM":"07","8AM":"08","9AM":"09","10AM":"10","11PM":"11","12PM":"12","1PM":"13","2PM":"14","3PM":"15","4PM":"16","5PM":"17","6PM":"18","7PM":"19","8PM":"20","9PM":"21","10PM":"22","11PM":"23","12AM":"00"}

        if ":" in fr_hr:
            match = re.search("^(1[0-2]|[1-9]):([0-5][0-9]) ([AP][M])$", fr_hr)
            # print(match)
            new_fr_hr = con_dic[(match.group(1)+match.group(3))]
            # print(fr_hr)
            # print(new_fr_hr)
            con_fr_hr = new_fr_hr + ":" + match.group(2)
            # print(con_fr_hr)
        else:
            match = re.search("^(1[0-2]|[1-9]) ([AP][M])$", fr_hr)
            new_fr_hr = con_dic[(match.group(1)+match.group(2))]
            # print(fr_hr)
            # print(new_fr_hr)
            con_fr_hr = new_fr_hr + ":00"
            # print(con_fr_hr)

        if ":" in to_hr:
            match = re.search("^(1[0-2]|[1-9]):([0-5][0-9]) ([AP][M])$", to_hr)
            # print(match)
            new_to_hr = con_dic[(match.group(1)+match.group(3))]
            # print(to_hr)
            # print(new_to_hr)
            con_to_hr = new_to_hr + ":" + match.group(2)
            # print(con_to_hr)
        else:
            match = re.search("^(1[0-2]|[1-9]) ([AP][M])$", to_hr)
            new_to_hr = con_dic[(match.group(1)+match.group(2))]
            # print(to_hr)
            # print(new_to_hr)
            con_to_hr = new_to_hr + ":00"
            # print(con_to_hr)
        return (con_fr_hr + " to " + con_to_hr)
    except:
        raise ValueError
        # sys.exit(1)

if __name__ == "__main__":
    main()


# SOLUTION FOR XX:YY AM/PM not only XX AM/PM
# match = re.search("^(1[0-2]|[1-9]):[0-5][0-9]|60) ([AP][M]) to (1[0-2]|[1-9]):([0-5][0-9]|60) ([AP][M])$", s)

# # print(match)
# # print(match.group(0))
# # # hr
# # print(match.group(1))
# # #  min
# # print(match.group(2))
# # # AM PM
# # print(match.group(3))
# # # hr
# # print(match.group(4))
# # #  min
# # print(match.group(5))
# # # AM PM
# # print(match.group(6))

# con_dic = {"12AM":"00","1AM":"01","2AM":"02","3AM":"03","4AM":"04","5AM":"05","6AM":"06","7AM":"07","8AM":"08","9AM":"09","10AM":"10","11PM":"11","12PM":"12","1PM":"13","2PM":"14","3PM":"15","4PM":"16","5PM":"17","6PM":"18","7PM":"19","8PM":"20","9PM":"21","10PM":"22","11PM":"23","12AM":"00"}

# # print(match.group(1)+match.group(3))
# # print(match.group(4)+match.group(6))
# # print(con_dic[(match.group(1)+match.group(3))])
# # print(con_dic[(match.group(4)+match.group(6))])

# print( con_dic[(match.group(1)+match.group(3))] + ":" + match.group(2) + " to " + con_dic[(match.group(4)+match.group(6))] + ":" + match.group(5))
