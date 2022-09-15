import hashlib
from collections import OrderedDict


# clientId kYs1LA95C
# secret owTV8QU2SD54Skae1pYYQH1Obl2Xxf

def sort_od(od):
    res = OrderedDict()
    for k, v in sorted(od.items()):
        if isinstance(v, dict):
            res[k] = sort_od(v)
        else:
            res[k] = v
    return res

def implode_recursive(arr):
    str_p = ''

    if isinstance(arr, dict):
        values = arr.values()
    else:
        values = arr

    for val in values:
        if isinstance(val, (list, tuple, dict)):
            str_p = str_p + str(implode_recursive(val)) + separator
        else:
            str_p = str_p + str(val) + separator

    return str_p[0:len(str_p) - len(separator)]

# Step 1. Get the required data
allParams = {
    'moneyType': 82,
    'amount': 100,
    'playerId': 74094,
    'locale': 'ru',
    'recursive': {
        'x': 3,
        'b': 2,
        'a': 1,
        'z': 4
    },
    'recursiveArray': [3, 2, 1, 4]
} # Query parameters

secret = 'owTV8QU2SD54Skae1pYYQH1Obl2Xxf' # Your secret key
separator = ''

# Step 2. Delete the parameter 'clientId' from the array with query parameters
exceptedParams = (
    'kYs1LA95C',
)
params = {}
for (key, value) in allParams.items():
    if key not in exceptedParams:
        params[key] = value

# Step 3. Sort the parameters
params = sort_od(params)

# Step 4. Concatenate the parameters into a string
strParams = implode_recursive(params)

# Step 5. Add a secret key to the string
strParams = strParams + secret

# Step 6. Generate a signature using the SHA256 algorithm
m = hashlib.sha256()
m.update(str(strParams).encode('utf-8'))
sign = m.hexdigest()

print(sign)