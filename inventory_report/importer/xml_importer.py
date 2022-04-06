import xml.etree.ElementTree as ET


class report_XML:
    def import_data(path):
        tree = ET.parse('country_data.xml')
        root = tree.getroot()
        product_itens = []
        for child in root:
            item = {}
            for element in child:
                # print(element.tag, 'text=', element.text)
                item[element.tag] = element.text
            product_itens.append(item)
        return product_itens

# Referência e Documentação:
# https://trybecourse.slack.com/archives/C013105FU2C/p1617305558357400
# https://docs.python.org/3/library/xml.etree.elementtree.html
