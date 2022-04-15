from requests import get as GET

class YoutubeApi:

    def __init__(self):
        self.api_key = json.load(open('creds/credentials.json'))['api_key']
        self.url = 'https://www.googleapis.com/youtube/v3/'
        self.headers = {'Accept': 'application/json'}
    
    def get_channel_id(self, channel_name:str) -> str:
        params = {
            'part': 'snippet',
            'forUsername': channel_name,
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
    
    def get_content(self, channel_key:str) -> dict:

        for item in youtube_url:
            key = item.split("/")[-1]
            if item.split("/")[-2] != 'channel':
                channel_id = self.get_channel_id(key)
                return self.get_videos(channel_id)
            else:
                return self.get_videos(key)

