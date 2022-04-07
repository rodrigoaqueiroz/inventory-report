from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        ext = path.split(".")[-1]
        if ext == "json":
            with open(path) as file:
                data = file.read()
                item = json.loads(data)
                return item
        else:
            raise ValueError("Arquivo inválido")
