from abc import ABC, abstractmethod
from datetime import datetime


class SimpleReport(ABC):
    def __init__(self, products):
        self.products = products

    @abstractmethod
    def generate(products):
        data_de_fabricacao = ""
        data_de_validade = ""
        empresa = ""
        old_date = []

        for product in products:
            empresa = product.get("nome_da_empresa")

            old_date.append(product["data_de_fabricacao"])

            if product["data_de_validade"] < str(datetime.now().date):
                data_de_validade = product.get("data_de_validade")


        print(f"🔥🔥🔥🔥🔥🔥{old_date}")

        return (
            f"Data de fabricação mais antiga: {min(old_date)}\n"
            f"Data de validade mais próxima: {data_de_validade}\n"
            f"Empresa com mais produtos: {empresa}"
        )
