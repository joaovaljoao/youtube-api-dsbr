from csv_parser import YoutubeCSV
from api_methods import YoutubeApi
import json


df = YoutubeCSV('Youtube', 'input_data/redes_sociais.csv', sep=';')

channel_url = df.channel_url()


api = YoutubeApi()
channel = channel_url[2]


channel_content = api.get_channel_content(channel)
# write channel content
with open('output_data/channel_content.json', 'w') as outfile:
    json.dump(channel_content, outfile, indent=4)

channel_id = channel_content['items'][0]['id']

# get search content
search_content = api.get_videos_search(channel_id)

# write search content
with open('output_data/search_content.json', 'w') as outfile:
    json.dump(search_content, outfile, indent=4)

# read json
with open('output_data/search_content.json', 'r') as infile:
    data = json.load(infile)

# get video content
video_content = [api.get_videos(item['id']['videoId']) for item in data['items'] if item['id']['kind'] == 'youtube#video']

# write video content
with open('output_data/video_content.json', 'w') as outfile:
    json.dump(video_content, outfile, indent=4)