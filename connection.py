#Base connection function
import requests
import json
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session


def main():
    # data
    client_id = ''
    client_secret = ''
    endpoint = 'https://api.codeswholesale.com'

    # connection
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url='{}/oauth/token'.format(endpoint), client_id=client_id, client_secret=client_secret)
    finaltoken = dict(token)
    bearer = finaltoken['access_token']
    headers = {'accept': 'application/json', 'Authorization': 'Bearer {}'.format(bearer)}
