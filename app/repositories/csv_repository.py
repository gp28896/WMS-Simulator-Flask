import json


class JSONRepository:


    def __init__(self, file_path: str):

        self.file_path = file_path


    def read(self):

        try:
            with open(self.file_path, "r") as f:
                return json.load(f)

        except:
            return []


    def write(self, data):

        with open(self.file_path, "w") as f:
            json.dump(data, f, indent = 2)


    def append(self, item):

        data = self.read()
        data.append(item)
        self.write(data)