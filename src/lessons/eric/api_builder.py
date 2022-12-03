import os
import hashlib
from collections import OrderedDict
import requests
from environs import Env


env = Env()
env.read_env()


class EnterraAPI:
    def __init__(self, sign, allParams):
        self.sign = sign
        self.allParams = allParams
        self.BASE_URL = "https://web.roundercasino.com/"
        self.CLIENT_ID = env("CLIENT_ID")

    @classmethod
    def build(cls):
        CLIENT_ID = env("CLIENT_ID")
        CASINO_SECRET = env("CASINO_SECRET")

        def sort_od(od):
            res = OrderedDict()
            for k, v in sorted(od.items()):
                if isinstance(v, dict):
                    res[k] = sort_od(v)
                else:
                    res[k] = v
            return res

        def implode_recursive(arr):
            str_p = ""

            if isinstance(arr, dict):
                values = arr.values()
            else:
                values = arr

            for val in values:
                if isinstance(val, (list, tuple, dict)):
                    str_p = str_p + str(implode_recursive(val)) + separator
                else:
                    str_p = str_p + str(val) + separator

            return str_p[0 : len(str_p) - len(separator)]

        # Step 1. Get the required data
        allParams = {
            "clientId": "kYs1LA95C",
            "dateFrom": "2022-11-13 00:00:00",
            "dateTo": "2022-11-19 23:59:59",
            #'per-page': 100,
            #'page': 10,
            # 'amount': 100,
            # 'playerId': 74094,
            # 'locale': 'ru',
            # 'recursive': {
            #     'x': 3,
            #     'b': 2,
            #     'a': 1,
            #     'z': 4
            # },
            # 'recursiveArray': [3, 2, 1, 4]
        }  # Query parameters

        secret = "owTV8QU2SD54Skae1pYYQH1Obl2Xxf"  # Your secret key
        separator = ""

        # Step 2. Delete the parameter 'clientId' from the array with query parameters
        exceptedParams = ("clientId",)
        params = {}
        for (key, value) in allParams.items():
            if key not in exceptedParams:
                params[key] = value
        print("params2", params)
        # Step 3. Sort the parameters
        params = sort_od(params)
        print(f"{params=}")
        # Step 4. Concatenate the parameters into a string
        strParams = implode_recursive(params)

        # Step 5. Add a secret key to the string
        strParams = strParams + secret
        print(f"{strParams=}")
        # Step 6. Generate a signature using the SHA256 algorithm
        m = hashlib.sha256()
        m.update(str(strParams).encode("utf-8"))
        sign = m.hexdigest()
        print(sign)

        return cls(sign, allParams)

    @classmethod
    def login_user(cls):
        pass

    def get_rake(self):
        headers = {
            "Accept": "application/vnd.api+json",
            "sign": self.sign,
        }
        params = {
            "clientId": self.CLIENT_ID,
            "dateFrom": self.allParams["dateFrom"],
            "dateTo": self.allParams["dateTo"],
            "per-page": 20,
            "page": 100,
        }
        rake_url = self.BASE_URL + "api/web/v2/app/users/rake"
        return requests.get(rake_url, params=params, headers=headers)


current_week_rakeback = EnterraAPI.build()
rake_this_week = current_week_rakeback.get_rake()
print(rake_this_week.json())
