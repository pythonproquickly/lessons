"""variables named to illustrtae how this works:
in practice they should be real domain names"""

import pandas as pd
import pprint as pp

list_of_dicts = [
    [
        {
            "id": 100,
            "name": "test",
            "state": "active",
            "boardId": 100,
            "goal": "",
            "startDate": "2023-01-30T07:58:57.186Z",
            "endDate": "2023-01-11T07:58:00.000Z",
        }
    ],
    [
        {
            "id": 123,
            "name": "test2",
            "state": "active",
            "boardId": 1233,
            "goal": "",
            "startDate": "2021-07-30T07:58:57.186Z",
            "endDate": "2021-07-13T07:58:00.000Z",
        }
    ],
]

# step one: transform the lists of list of dicts to
# dicts with a key, and a value that is the original dict
counter = 0
indexed_dict = {}
for alist in list_of_dicts:
    for adict in alist:
        counter += 1
        indexed_dict[counter] = adict

# compare to above
pp.pprint(indexed_dict)

# load a df, note orient param which turns it thru 90 degrees
df = pd.DataFrame.from_dict(indexed_dict, orient="index")

pp.pprint(df)
