"""Utils dogs module"""

# urllib libraries
import urllib3

#standard libraries
import json


#instance 
http = urllib3.PoolManager()


async def get_picture():
    """extract picture from API"""
    try:
        url = 'https://dog.ceo/api/breeds/image/random'
        response = http.request('GET', url)
        response_data = json.loads(response.data.decode('utf-8'))

    except Exception:
        raise ValueError(f'HTTP status: {response}')

    return response_data['message']


def send_f():
    """send file to server"""
    with open('app/guane.txt') as f:
        file_data = f.read()
    try:
        url = 'https://gttb.guane.dev/api/files'
        res = http.request(
            'POST',
            url,
            fields = {
                'file': ('app/guane.txt', file_data, 'text/plain'),
            } 
        )

        response_data = json.loads(res.data.decode('utf-8'))

    except Exception:
        raise ValueError(f'Url may be wrong. url: {url}')

    return response_data['filename']

