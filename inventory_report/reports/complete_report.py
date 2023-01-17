from inventory_report.reports.simple_report import SimpleReport


class CompleteReport():

    @classmethod
    def generate(cls, products):
        physicians_qtd = 0
        newton_qtd = 0
        forces = 0
        simple_report = SimpleReport.generate(products)

        for product in products:
            if product["nome_da_empresa"] == simple_report:
                physicians_qtd += 1
            if product["nome_da_empresa"] == "Newton Laboratories, Inc.":
                newton_qtd += 1
            if product["nome_da_empresa"] == "Forces of Nature":
                forces += 1

        # print(f"🔥{physicians_qtd}💵{newton_qtd}⏰{forces}")
        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"- Physicians Total Care, Inc.: {physicians_qtd}\n"
            f"- Newton Laboratories, Inc.: {newton_qtd}\n"
            f"- Forces of Nature: {forces}"
        )
