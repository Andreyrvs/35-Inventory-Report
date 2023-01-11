from abc import ABC, abstractmethod


class SimpleReport(ABC):
    def __init__(self, products):
        self.products = products

    @abstractmethod
    def generate(products):

        data_fab = "Data de fabricação mais antiga:"
        data_val = "Data de validade mais próxima:"
        empresa = "Empresa com mais produtos:"

        string_with_data = ""
        for product in products:
            string_with_data = f"""{data_fab} {product.get("data_de_fabricacao")}\n{data_val} {product.get("data_de_validade")}\n{empresa} {product.get("nome_da_empresa")}\n"
            """

        return string_with_data


# products = [
#      {
#        "id": 1,
#        "nome_do_produto": "CADEIRA",
#        "nome_da_empresa": "Forces of Nature",
#        "data_de_fabricacao": "2022-04-04",
#        "data_de_validade": "2023-02-09",
#        "numero_de_serie": "FR48",
#        "instrucoes_de_armazenamento": "Conservar em local fresco"
#      }
#    ]

# print(SimpleReport.generate(products))
