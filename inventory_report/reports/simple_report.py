from datetime import datetime


class SimpleReport():
    @classmethod
    def generate(cls, products):
        company_with_more_products = []
        earliest_date = []
        closest_date = []

        miau = 0
        for product in products:
            earliest_date.append(product["data_de_fabricacao"])

            if product["data_de_validade"] >= str(datetime.now().date()):
                closest_date.append(product["data_de_validade"])

            company_with_more_products.append(product["nome_da_empresa"])

            company_with_more_products.count(product["nome_da_empresa"])

            miau = max(
                company_with_more_products,
                key=company_with_more_products.count
            )

        return (
            f"Data de fabricação mais antiga: {min(earliest_date)}\n"
            f"Data de validade mais próxima: {min(closest_date)}\n"
            f"Empresa com mais produtos: {miau}"
        )
