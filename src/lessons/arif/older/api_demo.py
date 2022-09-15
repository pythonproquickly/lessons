import requests
from requests.exceptions import HTTPError

try:
    """response = requests.get(
        'https://geo.brunswickcountync.gov/arcgis/rest/services/Layers'
        '/TaxParcels/FeatureServer/0/query?where=1%3D1&outFields=*&outSR'
        '=4326&f=json')"""

    response = requests.get(
        'https://geo.brunswickcountync.gov/arcgis/rest/services/Layers'
        '/TaxParcels/FeatureServer/0/query?where=DeedAcreage+%3E+%27100%27'
        'and 1%3D1&outFields=*'
        '&outSR'
        '=4326&f=json')

    # "where=DeedAcreage+%3E+%27100%27"
    response.raise_for_status()
    parcels = response.json()

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')


print(parcels)
exit(0)
# "DeedAcreage": "65.000 AC", also LT

"""for parcel_item in parcels['features']:
    try:
        x = parcel_item['attributes']['DeedAcreage'].split(' ')
    except:
        print(parcel_item['attributes'])"""

parcels = [parcel_item['attributes'] for parcel_item in parcels['features'] if
           parcel_item['attributes'] is not None and float(
               parcel_item['attributes']['DeedAcreage'].split(' ')[0]) > 50]

for parcel in parcels:
    print(parcel)
print(len(parcels))
