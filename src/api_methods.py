from requests import get as GET
import json

class YoutubeApi:

    def __init__(self):
        self.api_key = json.load(open('creds/credentials.json'))['api_key']
        self.url = 'https://www.googleapis.com/youtube/v3/'
        self.headers = {'Accept': 'application/json'}
    
    def get_channel_id(self, channel_name:str) -> str:
        params = {
            'part': 'id',
            'forUsername': channel_name,
            'key': self.api_key
        }
        response = GET(self.url + 'channels', params=params)
        return response.json()

    def get_channel_info(self, channel_id:str) -> dict:
        params = {
            'part': 'snippet,contentDetails,statistics',
            'id': channel_id,
            'key': self.api_key
        }
        response = GET(self.url + 'channels', params=params, headers=self.headers)
        return response.json()

    def get_videos(self, channel_id:str) -> dict:
        params = {
            'part': 'snippet,contentDetails,statistics',
            'id': channel_id,
            'key': self.api_key
        }
        response = GET(self.url + 'videos', params=params, headers=self.headers)
        return response.json()
    
    def get_content(self, channel_url:str) -> dict:

        key = channel_url.split("/")[-1]
        if channel_url.split("/")[-2] == 'channel':
            return self.get_channel_info(key)
        elif channel_url.split("/")[-2] == 'user':
            channel_id = self.get_channel_id(key)['items'][0]['id']
            return self.get_channel_info(channel_id)
        else:
            return None