from django.shortcuts import render

import requests
import json

BASE_URL = 'https://randomuser.me/api/'

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