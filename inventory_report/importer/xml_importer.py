import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class report_XML(Importer):
    def import_data(path):
        tree = ET.parse(path)
        root = tree.getroot()
        product_itens = []
        ext = path.split(".")[-1]
        if ext == "xml":
            for child in root:
                item = {}
                for element in child:
                    item[element.tag] = element.text
                product_itens.append(item)
            return product_itens
        else:
            raise ValueError("Arquivo inválido")

# Referência e Documentação:
# https://trybecourse.slack.com/archives/C013105FU2C/p1617305558357400
# https://docs.python.org/3/library/xml.etree.elementtree.html
