class SimpleReport:
    def __init__(self, products):
        self.products = products
        print(products)

    def generate(self, products):

        return (
            f"Data de fabricação mais antiga: {products.data_de_fabricacao}"
            f"Data de validade mais próxima: {products.data_de_validade}"
            f"Empresa com mais produtos: {products.nome_da_empresa}"
        )
