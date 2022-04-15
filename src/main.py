from csv_parser import YoutubeCSV
from api_methods import YoutubeApi


df = YoutubeCSV('Youtube', 'input_data/redes_sociais.csv')

channel_key = df.channel_key()

# Baixar os dados de cada canal
for key in channel_key:
    YoutubeApi().get_content(key)