import json

import requests
from hashlib import sha256

from ApiCore.SignatureGen import SignatureGen


class ApiHelper:

    def __init__(self, url, sign_gen, client_id):
        self.__sign_generator = sign_gen
        self.req = requests
        self.url = url
        self.clientId = client_id

    def get(self, url, header, r_params):
        self.req.get(url=url, headers=header, params=r_params)

    def get_sign(self, params):
        return self.__sign_generator.get_signature(params)

    def login_user(self, login: str, password: str):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/vnd.api+json',
        }

        params = {
            'clientId': self.clientId,
        }
        data = {
            'login': login,
            'password': password,
        }

        if login is None:
            login_url = self.url + "api/web/v2/login?clientId={}".format(
                self.clientId)
        else:
            login_url = self.url + "api/web/v2/login?clientId={}".format(login)

        return self.req.post(login_url,
                             params=params,
                             headers=headers,
                             data=data)


if __name__ == '__main__':

    base_url = "https://web.roundercasino.com/api/web/"

    secret_key = None
    sign_for_accept = SignatureGen(sk=secret_key)

    AccepterTransaction = ApiHelper(base_url, sign_for_accept, "clientId")

    # need correct get
    json_answer = AccepterTransaction.get_transaction().json()
    transaction_num = 0
