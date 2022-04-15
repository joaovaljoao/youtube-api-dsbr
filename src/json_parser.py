import json

# json reader
class Json:

    def __init__(self, file):
        self.file = file

    def read(self):
        with open(self.file) as json_file:
            data = json.load(json_file, indent=4)
            return data
    
    def write(self, data, mode='a'):
        with open(self.file, mode) as outfile:
            json.dump(data, outfile, indent=4)
