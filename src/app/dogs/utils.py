"""extract picture from API"""

import requests


async def get_picture():
    url = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(url)

    if response.status_code == 200:
        picture = response.json()['message']
    else:
        picture = f' HTTP status: {response.status_code}'

    return picture

