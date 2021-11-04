import requests

print("Saving Image...")
api = 'https://benbot.app/api/v1/status'
api = requests.get(api)
version = api.json()['currentFortniteVersionNumber']
url = 'https://media.fortniteapi.io/images/map.png?showPOI=true'
r = requests.get(url, allow_redirects=True)

open(f'{version}0 - map.png', 'wb').write(r.content)
print("Success! you may now exit this program.")