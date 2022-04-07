from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(clas, report):
        oldest_date = min(
            [product["data_de_fabricacao"] for product in report])

        expiration_date = min(
            [product["data_de_validade"] for product in report
                if datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
                >= datetime.today()])

        company = max(
            Counter(product["nome_da_empresa"] for product in report))

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com maior quantidade de produtos estocados: {company}\n"
        )
