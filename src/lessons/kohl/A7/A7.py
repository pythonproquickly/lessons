import pandas as pd
import requests

from TableViewer import *

# Initial code written by Derya Akbaba, University of Utah.
# Author of final code:

######################################
# Data Retrieval & Data Printing
######################################

# You will be using three datasets for this project from opendata.utah.gov.
# We will show you how to import one dataset using an API and you will be
# responsible for the other two.

# Here, we are importing COVID case numbers from the following url
# https://opendata.utah.gov/Health/Utah-COVID-Cases-by-County-Map/y4r8-7n5m
covid = "https://opendata.utah.gov/resource/y4r8-7n5m.json"
covid_api_response = requests.get(covid)

covid_data = covid_api_response.json()

# You can use the view_table function to see the first 5 rows
# of the data that you just loaded.

print("Preview of downloaded COVID data:")
print(view_table(covid_data), "\n")

# This is where you will start loading your data.
# We have provided the name of the dataset and the URl to find the API
# endpoint.

# Data retrieval Step 1.
# Utah Hospital Characteristics
# https://opendata.utah.gov/Health/Utah-Hospital-Characteristics/ierb-h3t5
# Store the data from this data set in a variable called hospital_data.

hospital = "https://opendata.utah.gov/resource/ierb-h3t5.json"
hospital_api_response = requests.get(hospital)

hospital_data = hospital_api_response.json()

# Data retrieval Step 2.
# Average Home Price By County In Utah 1996-2015
# https://opendata.utah.gov/Social-Services/Average-Home-Price-By-County-In
# -Utah-1996-2015/sma7-tpu2
# Store the data from this data set in a variable called housing_data.

housing = "https://opendata.utah.gov/resource/sma7-tpu2.json"
housing_api_response = requests.get(housing)

housing_data = housing_api_response.json()

######################################
# Dictionary Creation
# Make a dictionary using county name as the key.
# From the hospital dataset you will want to add all of the
# total_licensed_beds in a county.
# From the COVID dataset you will want to add active cases.
# From the Housing dataset you will want the difference between the housing
# prices (2015 - 1996).
# Your data structure will look like this:
# {'county1': {'beds': [1], 'cases': [2], 'housing': [3]}, 'county2': {
# 'beds': [1], 'cases': [2], 'housing': [3]}}
######################################

# For every entry in each of our 3 datasets you add the data to complete_dict.
# The county will serve as the key.
# Remember real-world data is not always complete, so you will need to check
# if the
# data you are looking for exists.

complete_dict = {}
# Here is an example of how we add entries to the complete_dict from the
# COVID dataset.
for item in covid_data:
    cases = item['confirmed']
    county = item['county'].upper()
    if county in complete_dict:
        complete_dict[county]['cases'] = int(cases)
    else:
        complete_dict[county] = {'cases': int(cases)}

# Next you will add the total number of licenced beds per county.
# Notice that some counties have more than one hospital, so they
# will report more than one bed number. You will have to add them
# up so that you are only reporting one number for each county.
# We are expecting to see integer values.

for item in hospital_data:
    if 'county' in item:
        county = item['county'].upper()
    else:
        continue
    if 'total_licensed_beds' in item:
        beds = float(item['total_licensed_beds'])
    else:
        beds = 0
    if county not in complete_dict:
        complete_dict[county] = {}
    if 'beds' in complete_dict[county]:
        complete_dict[county]['beds'] += beds
    else:
        complete_dict[county]['beds'] = beds

# Finally you will find how much the housing prices have changed in each
# county.
# You can get this number by finding the difference between the average home
# price
# in April 1996 and the average home price in April 2015.
# The values should mostly be positive since home prices have increased
# since 1996.
# We are expecting to see float values.

for item in housing_data:
    if 'regionname' in item:
        county = item['regionname'].upper()
    else:
        continue
    if '_2015_04' in item and '_1996_04' in item:
        price_change = float(item['_2015_04']) - float(item['_1996_04'])
    else:
        price_change = 0
    if county not in complete_dict:
        complete_dict[county] = {}
    complete_dict[county]['housing'] = price_change

# You can print the dictionary to see all your data in one place.
print("Nested Dictionary:")
print(complete_dict)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

in_pandas = pd.DataFrame.from_dict(complete_dict)
print(in_pandas)
