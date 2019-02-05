# PEGI rating CSV generator
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

    def dumper(cwid):
        url = 'https://api.codeswholesale.com/v2/products/{}/description'.format(cwid)
        r = requests.get(url, headers=headers)
        dump = r.text
        dump_json = json.loads(dump)
        try:
            pegi = dump_json['pegirating']
            print(f'{cwid},"{pegi}"')
        except:
            print(f'{cwid},"No data for this product"')

    # generowanie listy ID
    def listgenerator():
        f = open('id.txt', 'r')
        for line in f:
            yield line.rstrip('\n')
        f.close()

    for games in listgenerator():
        dumper(games)


if __name__ == '__main__': main()
