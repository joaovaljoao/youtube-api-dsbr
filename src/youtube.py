import requests
import json

def get_youtube_content(id):
    headers = {
        'Accept': 'application/json',
    }

    params  = { 'channelId': id,
                'key' : 'cole a key aqui', 
                'order': 'date',
                'maxResults': '348'}

    response = requests.get('https://youtube.googleapis.com/youtube/v3/search', headers=headers, params=params)
    return response

def json_writer(response):
    with open('youtube.json', 'w') as outfile:
        json.dump(response.json(), outfile, indent=4)


id = 'UCbT5RHZncV04-qp1jtm6Nsw'
response = get_youtube_content(id)
json_writer(response)