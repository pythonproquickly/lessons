# Import dictionary from text file
# We have handled this for you
import numpy as np

def import_dict():
    dictionary = np.load('dictionary.npy', allow_pickle='TRUE').item()
    return dictionary

# 1. Use this function to create a new version of the imported dictionary
# - Your new dictionary should have three keys and values for each county
# - The keys should be descriptive (instead of 'beds' you could use '# of Hospital Beds' for example)
# - The value for housing data should be divided by 100. That way when we create the bar chart
#   the housing prices won't distort the other values.
def dictionary_cleaner(old_dict):
    new_dict = {}
    for county, county_data in old_dict.items():
        new_dict[county.title()] = {}
    housing = "House Price"
    beds = "# of Hospital Beds"
    cases = "# of Cases"

    for county, county_data in old_dict.items():
        county = county.title()
        if county_data.get('housing', None) is None:
            old_housing = 0
        else:
            old_housing = county_data['housing']
        if county_data.get('cases', None) is None:
            old_cases = 0
        else:
            old_cases = county_data['cases']
        if county_data.get('beds', None) is None:
            old_beds = 0
        else:
            old_beds = county_data['beds']
        new_dict[county] = {housing: old_housing, cases: old_cases, beds: old_beds}

    return new_dict


# This runs if the file is executed and doesn't if the file is imported
# This is where you can test the output of your functions.
if __name__ == '__main__':
    imported_dict = import_dict()
    print("Imported Dictionary: ", imported_dict)
    cleaned_dict = dictionary_cleaner(imported_dict)
    print(cleaned_dict)

