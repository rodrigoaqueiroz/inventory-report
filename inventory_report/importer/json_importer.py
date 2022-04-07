import json


class report_JSON:
    def import_data(path):
        with open(path) as file:
            data = file.read()
            item = json.loads(data)
        return item
