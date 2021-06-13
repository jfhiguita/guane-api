import urllib3
import json

http = urllib3.PoolManager()


def send_f():
    with open('./app/guane.txt') as f:
        file_data = f.read()
    try:
        url = 'https://gttb.guane.dev/api/files'
        res = http.request(
            'POST',
            url,
            fields = {
                'file': ('./app/guane.txt', file_data, 'text/plain'),
            } 
        )

        response_data = json.loads(res.data.decode('utf-8'))

    except Exception:
        raise ValueError(f'Url may be wrong. url: {url}')

    return response_data['filename']
