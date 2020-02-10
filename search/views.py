from django.shortcuts import render

import requests
import json
import datetime

BASE_URL = 'https://randomuser.me/api/'

# client_id = os.environ.get('CLIENT_ID')
# client_secret = os.environ.get('CLIENT_SECRET')

# auth_header = b64encode(
#     six.text_type(client_id + ':' + client_secret).encode('ascii'))

def home_page(request):
    resp = requests.get(BASE_URL)
    content = json.loads(resp.text)['results'][0]

    user = {}

    user['name'] = content['name']['first'] + ' ' + content['name']['last']
    user['email'] = content['email']
    user['city'] = content['location']['city']
    user['country'] = content['location']['country']
    user['dob'] = content['dob']['date'].split('T')[0]
    user['img'] = content['picture']['large']

    return render(request, 'base.html', {'user': user})