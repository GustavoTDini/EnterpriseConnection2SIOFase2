from estoque import estoque
from produto import produto


valor_venda = float(50)
valor_compra = float(30)
valor_compra_ano = [30, 25, 35, 43, 32, 32, 32, 34, 45, 30, 33, 35]
vendas_ano = [225, 300, 333, 352, 145, 842, 144, 752, 520, 222, 127, 333]
valor_x_vendas = {
    1: {
        "valor": valor_compra_ano[0],
        "vendas": vendas_ano[0]
    },
    2: {
        "valor": valor_compra_ano[1],
        "vendas": vendas_ano[1]
    },
    3: {
        "valor": valor_compra_ano[2],
        "vendas": vendas_ano[2]
    },
    4: {
        "valor": valor_compra_ano[3],
        "vendas": vendas_ano[3]
    },
    5: {
        "valor": valor_compra_ano[4],
        "vendas": vendas_ano[4]
    },
    6: {
        "valor": valor_compra_ano[5],
        "vendas": vendas_ano[5]
    },
    7: {
        "valor": valor_compra_ano[6],
        "vendas": vendas_ano[6]
    },
    8: {
        "valor": valor_compra_ano[7],
        "vendas": vendas_ano[7]
    },
    9: {
        "valor": valor_compra_ano[8],
        "vendas": vendas_ano[8]
    },
    10: {
        "valor": valor_compra_ano[9],
        "vendas": vendas_ano[9]
    },
    11: {
        "valor": valor_compra_ano[10],
        "vendas": vendas_ano[10]
    },
    12: {
        "valor": valor_compra_ano[11],
        "vendas": vendas_ano[11]
    },
}


estoque_ano = estoque(1000)

estoque_ano.restocar(valor_compra, valor_venda)
print(estoque_ano.quantidade_estoque())

custo_inicial = estoque_ano.custo_estoque()

print(custo_inicial)


lucro_mensal = []

# for i in range(1,12):
#     estoque atual = 0
#     for e in estoque_ano:
#         while e != 0:
#             estoque = estoque.index(e)
#     estoque