import json
from pathlib import Path

# json reader
class Json:

    def __init__(self):
        if not Path('output_data').exists():
            Path('output_data').mkdir()

    def read(self, content):
        with open(content) as json_file:
            data = json.load(json_file, indent=4)
            return data
    
    def write(self, data, filename):
        with open(filename, 'r') as outfile:
            json.dumps(outfile, indent=4)
