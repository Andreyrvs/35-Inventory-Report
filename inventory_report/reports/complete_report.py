from inventory_report.reports.simple_report import SimpleReport


class CompleteReport():

    @classmethod
    def generate(cls, products):
        simple_report = SimpleReport.generate(products)
        formatted = ""
        companies = {}

        for product in products:
            if product["nome_da_empresa"] not in companies:
                companies[product["nome_da_empresa"]] = 1
            else:
                companies[product["nome_da_empresa"]] += 1

        for key in companies:
            formatted += f"- {key}: {companies[key]}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{formatted}"
        )
