# import pytest
from inventory_report.inventory.product import Product


def test_cria_produto():
    my_product = Product(
        2,
        'Batata',
        'Carre',
        '22-04-2022',
        '22-05-2022',
        '1232',
        'Guarda bem'
    )
    assert my_product.id == int(2)
    assert my_product.nome_do_produto == 'Batata'
    assert my_product.nome_da_empresa == 'Carre'
    assert my_product.data_de_fabricacao == '22-04-2022'
    assert my_product.data_de_validade == '22-05-2022'
    assert my_product.numero_de_serie == '1232'
    assert my_product.instrucoes_de_armazenamento == 'Guarda bem'
