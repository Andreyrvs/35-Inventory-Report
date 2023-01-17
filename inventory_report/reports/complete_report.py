from inventory_report.reports.simple_report import SimpleReport


class CompleteReport():

    @classmethod
    def generate(cls, products):
        simple_report = SimpleReport.generate(products)
        company = []
        total = 0
        formatted = ""

        for product in products:
            company.append(product["nome_da_empresa"])
            total = company.count(product["nome_da_empresa"])
            companies = product["nome_da_empresa"]

            formatted += f"- {companies}: {total}\n"

        print(f"🔥🔥🔥{formatted}")
        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{formatted}"
        )
