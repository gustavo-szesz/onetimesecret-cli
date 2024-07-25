import requests
from requests.auth import HTTPBasicAuth

URL = "https://onetimesecret.com"

class OneTimeSecretCli(object):
    def __init__(self, user, key, url=URL):
        self.key = key
        self.url = url
        self.user = user

    def create_link(self, secret, ttl=259200, passphrase=None):
        data = {"secret": secret, "ttl": ttl}
        if passphrase:
            data["passphrase"] = passphrase
        response = requests.post(
            "{}/api/v1/share".format(self.url),
            data=data,
            auth=HTTPBasicAuth(self.user, self.key),
        )
        response_data = response.json()
        return "{}/secret/{}".format(self.url, response_data["secret_key"])

    def retrieve_secret(self, secret_key, passphrase=None):
        data = {"secret_key": secret_key}
        if passphrase:
            data["passphrase"] = passphrase
        response = requests.post(
            "{}/api/v1/secret/{}".format(self.url, secret_key),
            data=data,
            auth=HTTPBasicAuth(self.user, self.key),
        )
        if response.status_code == 200:
            return response.json().get("value")
        elif response.status_code == 404:
            print("Error: Secret not found. Please check the secret key.")
            return None
        else:
            print(f"Error: {response.status_code} - {response.reason}")
            response.raise_for_status()

