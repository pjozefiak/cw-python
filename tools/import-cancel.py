# Tool for cancelling stucked import for CodesWholesale Plugins

import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import json


def main():
    client_id = ''
    client_secret = ''

    endpoint = 'https://api.codeswholesale.com'

    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    token = dict(oauth.fetch_token(token_url='{}/oauth/token'.format(endpoint), client_id=client_id,
                                           client_secret=client_secret))

    headers = {'accept': 'application/json', 'Authorization': 'Bearer {}'.format(token['access_token'])}

    def getaccount():
        uri = 'https://api.codeswholesale.com/v2/accounts/current'
        r = requests.get(uri, headers=headers)
        account = json.loads(r.text)
        return account

    def getimports():
        uri = 'https://api.codeswholesale.com/v2/imports'
        r = requests.get(uri, headers=headers)
        imports_json = json.loads(r.text)
        return imports_json['items']

    def getimportstocancel(imports):
        imports_to_cancel = []
        for imp in imports:
            if imp['importStatus'] == 'AWAITING' or imp['importStatus'] == 'IN_PROGRESS':
                imports_to_cancel.append(imp)
            else:
                continue
            return imports_to_cancel

    account = getaccount()
    print('Account: {} - {}'.format(account['fullName'], account['email']))
    print('---')
    if not getimportstocancel(getimports()):
        print('No imports to cancel')
    else:
        for stuck_import in getimportstocancel(getimports()):
            url = 'https://api.codeswholesale.com/v2/imports/{}'.format(stuck_import['importId'])
            requests.patch(url, headers=headers)
            print('{} - cancelled'.format(stuck_import['importId']))

    print('---')
    print('All stucked imports has been cancelled')


if __name__ == '__main__':
    main()
