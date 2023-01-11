from datetime import datetime


class SimpleReport():
    @classmethod
    def generate(cls, products):
        companies = []
        earliest_date = []
        closest_date = []
        company_with_more_products = ""

        for product in products:
            earliest_date.append(product["data_de_fabricacao"])

            if product["data_de_validade"] >= str(datetime.now().date()):
                closest_date.append(product["data_de_validade"])

            companies.append(product["nome_da_empresa"])

            companies.count(product["nome_da_empresa"])

            company_with_more_products = max(
                companies,
                key=companies.count
            )

        return (
            f"Data de fabricação mais antiga: {min(earliest_date)}\n"
            f"Data de validade mais próxima: {min(closest_date)}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )
