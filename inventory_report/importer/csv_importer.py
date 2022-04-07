import csv


class report_CSV:
    def import_data(path):
        product_itens = []
        with open(path) as file:
            data = csv.DictReader(file, delimiter=',', quotechar='"')
            for item in data:
                product_itens.append(item)
        return product_itens
