from inventory_report.importer.xml_importer import report_XML


class Inventory:
    def import_data(path, report=""):
        products = []
        ext = path.split(".")[-1]
        if ext == "xml":
            products = report_XML.xml_data(path)
        if report == "simples":
            # aguardar req01
        elif report == "completo":
            # aguardar req02
        # return aguardar resultado dos ifs

