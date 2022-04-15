import pandas as pd

class YoutubeCSV:
    def __init__(self, column, filename, sep=',', encoding='utf-8'):
        self.column = column
        self.filename = filename
        self.data = pd.read_csv(self.filename, sep=sep, encoding=encoding)

    def channel_key(self):
        data = self.data[f'{self.column}'].to_list()
        return data

