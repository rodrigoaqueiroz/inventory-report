from inventory_report.importer.xml_importer import report_XML
from inventory_report.importer.json_importer import report_JSON
from inventory_report.importer.csv_importer import report_CSV
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def import_data(path, report=""):
        products = []
        ext = path.split(".")[-1]
        if ext == "xml":
            products = report_XML.import_data(path)
        if ext == "json":
            products = report_JSON.import_data(path)
        if ext == "csv":
            products = report_CSV.import_data(path)
        if report == "simples":
            report = SimpleReport.generate(products)
        elif report == "completo":
            report = CompleteReport.generate(products)
        return report
