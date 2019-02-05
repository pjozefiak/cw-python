import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session


class CwConnection:
    def __init__(self, client_id, client_secret, endpoint):
        self.client_id = client_id
        self.client_secret = client_secret
        self.endpoint = endpoint

    def authclient(self):
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        token = dict(oauth.fetch_token(token_url='{}/oauth/token'.format(self.endpoint), client_id=self.client_id,
                                       client_secret=self.client_secret))
        headers = {'accept': 'application/json', 'Authorization': 'Bearer {}'.format(token['access_token'])}
        return headers, self.endpoint

    def getEndpoint(self):
        return self.endpoint

    def send(self, prod):
        url = 'https://api.codeswholesale.com/v2/products/{}/description'.format(prod)
        r = requests.get(url, headers=self.authclient())
        return r.text