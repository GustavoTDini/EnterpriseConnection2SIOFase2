from estoque import estoque
from produto import produto

valor_venda = float(50)
custo_compra = float(30)
custo_compra_anual = [30, 25, 35, 43, 32, 32, 32, 34, 45, 30, 33, 35]
vendas_anual = [225, 300, 333, 352, 145, 842, 144, 752, 520, 222, 127, 333]
meses_ano = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julio", "Agosto", "Setembro", "Outubro",
             "Novembro", "Dezembro"]
valor_x_vendas = {
    1: {
        "custo_compra": custo_compra_anual[0],
        "valor_venda": valor_venda,
        "vendas": vendas_anual[0]
    },
    2: {
        "custo_compra": custo_compra_anual[1],
        "valor_venda": valor_venda,
        "vendas": vendas_anual[1]
    },
    3: {
        "custo_compra": custo_compra_anual[2],
        "valor_venda": valor_venda,
        "vendas": vendas_anual[2]
    },
    4: {
        "custo_compra": custo_compra_anual[3],
        "valor_venda": valor_venda,
        "vendas": vendas_anual[3]
    },
    5: {
        "custo_compra": custo_compra_anual[4],
        "valor_venda": valor_venda,
        "vendas": vendas_anual[4]
    },
    6: {
        "custo_compra": custo_compra_anual[5],
        "valor_venda": valor_venda,
        "vendas": vendas_anual[5]
    },
    7: {
        "custo_compra": custo_compra_anual[6],
        "valor_venda": valor_venda,
        "vendas": vendas_anual[6]
    },
    8: {
        "custo_compra": custo_compra_anual[7],
        "valor_venda": valor_venda,
        "vendas": vendas_anual[7]
    },
    9: {
        "custo_compra": custo_compra_anual[8],
        "valor_venda": valor_venda,
        "vendas": vendas_anual[8]
    },
    10: {
        "custo_compra": custo_compra_anual[9],
        "valor_venda": valor_venda,
        "vendas": vendas_anual[9]
    },
    11: {
        "custo_compra": custo_compra_anual[10],
        "valor_venda": valor_venda,
        "vendas": vendas_anual[10]
    },
    12: {
        "custo_compra": custo_compra_anual[11],
        "valor_venda": valor_venda,
        "vendas": vendas_anual[11]
    },
}

def verificacao_anual():
    lucro_mensal_por_produto = []
    lucro_mensal = []
    valor_de_vendas_mensal = []
    custo_de_restocagem_mensal = []
    for i in range(1, 13):
        lucro = 0
        vendas = 0
        custo_estoque = 0
        for p in range(valor_x_vendas[i]["vendas"]):
            vendas += valor_x_vendas[i]["valor_venda"]
            lucro += estoque_ano.venda()
        custo_estoque = float(estoque_ano.restocar(valor_x_vendas[i]["valor_venda"], valor_x_vendas[i]["custo_compra"]))
        lucro_mensal_por_produto.append(lucro)
        valor_de_vendas_mensal.append(vendas)
        custo_de_restocagem_mensal.append(custo_estoque)
        lucro_mensal.append(vendas - custo_estoque)
    return [lucro_mensal, lucro_mensal_por_produto, valor_de_vendas_mensal, custo_de_restocagem_mensal]

def relatorio_anual(lucro_mensal, lucro_mensal_por_produto, valor_de_vendas_mensal, custo_de_restocagem_mensal, custo_inicial):
    lucro_anual = - custo_inicial
    for i, valor in enumerate(lucro_mensal):
        print("O lucro de {} foi {}".format(meses_ano[i], valor))
        lucro_anual += valor
    print("O lucro anual considerando as venda e os custos de reestocagem mensais é de cada produto vendido é {}".format(lucro_anual))
    print("\n")

    lucro_anual_por_produto = -custo_inicial
    for i, valor in enumerate(lucro_mensal_por_produto):
        print("O lucro por produto de {} foi {}".format(meses_ano[i], valor))
        lucro_anual_por_produto += valor
    print("O lucro anual considerando o custo de cada produto vendido é {}".format(lucro_anual_por_produto))
    print("\n")

    vendas_total = -custo_inicial
    for i, valor in enumerate(valor_de_vendas_mensal):
        print("A receita de vendas de {} foi de {}".format(meses_ano[i], valor))
        vendas_total += valor
    print("O receita de vendas do ano todo foi de {}".format(vendas_total))
    print("\n")

    print(custo_de_restocagem_mensal)
    custo_estoque_total = custo_inicial
    for i, valor in enumerate(custo_de_restocagem_mensal):
        print("O custo de estocagem de {} foi de {}".format(meses_ano[i], valor))
        custo_estoque_total += valor
    print("O custo com o estoque durante todo o ano foi de {}".format(custo_estoque_total))

estoque_ano = estoque(1000)

estoque_ano.restocar(valor_venda, custo_compra)

custo_inicial = estoque_ano.custo_estoque()

dados_anual = verificacao_anual()

relatorio_anual(dados_anual[0], dados_anual[1], dados_anual[2], dados_anual[3], custo_inicial)
