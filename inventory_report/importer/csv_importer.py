from inventory_report.importer.importer import Importer
import csv


class report_CSV(Importer):
    def import_data(path):
        product_itens = []
        ext = path.split(".")[-1]
        if ext =="csv":
            with open(path) as file:
                data = csv.DictReader(file, delimiter=',', quotechar='"')
                for item in data:
                    product_itens.append(item)
                return product_itens
        else:
            raise ValueError("Arquivo inválido")    
