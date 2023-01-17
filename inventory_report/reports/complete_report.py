from inventory_report.reports.simple_report import SimpleReport


class CompleteReport():

    @classmethod
    def generate(cls, products):
        simple_report = SimpleReport.generate(products)
        company = []
        total = 0
        complete = []

        for product in products:
            company.append(product["nome_da_empresa"])
            total = company.count(product["nome_da_empresa"])
            companies = product["nome_da_empresa"]

            complete.append(f"- {companies}: {total}\n")

        # print(f"🔥🔥🔥{complete}")
        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{str(complete)}"
        )


products = [
  {
    "id": 1,
    "nome_do_produto": "MESA",
    "nome_da_empresa": "Forces of Nature",
    "data_de_fabricacao": "2022-05-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48",
    "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
  },
  {
    "id": 2,
    "nome_do_produto": "MEaaSA",
    "nome_da_empresa": "Nature",
    "data_de_fabricacao": "2022-05-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48",
    "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
  },
    {
    "id": 3,
    "nome_do_produto": "MEaaSA",
    "nome_da_empresa": "of Nature",
    "data_de_fabricacao": "2022-05-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48",
    "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
  },
    {
    "id": 4,
    "nome_do_produto": "MEaaSA",
    "nome_da_empresa": "PFita",
    "data_de_fabricacao": "2022-05-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48",
    "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
  }
]

print(CompleteReport.generate(products))
