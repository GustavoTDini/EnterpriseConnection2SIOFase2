from estoque import Estoque

# Definição de valores iniciais
valor_venda = float(50)
custo_compra = float(30)
estoque_minimo = 1000
custo_compra_anual = [30, 25, 35, 43, 32, 32, 32, 34, 45, 30, 33, 35]
vendas_anual = [225, 300, 333, 352, 145, 842, 144, 752, 520, 222, 127, 333]
meses_ano = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julio", "Agosto", "Setembro", "Outubro",
             "Novembro", "Dezembro"]

# Dicionario tipo JSon com a consolidação dos valores
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


# Função para verificar e retornar os diversos valores a serem estudados
def calcular_valores_anual():
    # Listas que vão ser preenchidas com os dados coletados
    lucro_mensal_por_produto = []
    lucro_mensal = []
    valor_de_vendas_mensal = []
    custo_de_re_estocagem_mensal = []
    # Iteração para verificar casa mês do ano baseado em nosso dicionário
    for i in range(1, 13):
        lucro = 0
        vendas = 0
        # Iteração fazer as vendas, considerando o quanto foi vendido em cada mês
        for p in range(valor_x_vendas[i]["vendas"]):
            vendas += valor_x_vendas[i]["valor_venda"]
            # Utilizando a função do Estoque, retira o produto mais antigo e soma o seu valor ao lucro por produto
            lucro += estoque_ano.venda()
        # Utilizando a função do Estoque calculamos o custo mensal de estoque e o completamos até o valor definido
        custo_estoque = float(
            estoque_ano.re_estocar(valor_x_vendas[i]["valor_venda"], valor_x_vendas[i]["custo_compra"]))
        lucro_mensal_por_produto.append(lucro)
        valor_de_vendas_mensal.append(vendas)
        custo_de_re_estocagem_mensal.append(custo_estoque)
        lucro_mensal.append(vendas - custo_estoque)
        custo_estoque_final = estoque_ano.custo_estoque()
    return [lucro_mensal, lucro_mensal_por_produto, valor_de_vendas_mensal, custo_de_re_estocagem_mensal, custo_estoque_final]


def somar_valores(listas):
    nova_lista = [0] * len(listas)
    for i, lista in enumerate(listas):
        if type(lista) == list:
            for j in lista:
                nova_lista[i] += j
    return nova_lista


# Função que recebe os valores da verificação e os coleta em dados legíveis
def relatorio_anual(lucro_mensal, lucro_mensal_por_produto, valor_de_vendas_mensal, custo_de_re_estocagem_mensal,
                    custo_final_do_estoque, custo_inicial_do_estoque):
    lucro_anual = - custo_inicial_do_estoque
    for i, valor in enumerate(lucro_mensal):
        print("O lucro de {} foi {}".format(meses_ano[i], valor))
        lucro_anual += valor
    print("O lucro anual considerando as venda e os custos de re-estocagem mensais é de {}".format(lucro_anual))
    print("\n")

    lucro_anual_por_produto = -custo_final_do_estoque
    for i, valor in enumerate(lucro_mensal_por_produto):
        print("O lucro por produto de {} foi {}".format(meses_ano[i], valor))
        lucro_anual_por_produto += valor
    print("O lucro anual considerando o custo de cada produto vendido é de {}".format(lucro_anual_por_produto))
    print("\n")

    vendas_total = -custo_inicial_do_estoque
    for i, valor in enumerate(valor_de_vendas_mensal):
        print("A receita de vendas de {} foi de {}".format(meses_ano[i], valor))
        vendas_total += valor
    print("O receita de vendas do ano todo foi de {}".format(vendas_total))
    print("\n")

    custo_estoque_total = custo_inicial_do_estoque
    for i, valor in enumerate(custo_de_re_estocagem_mensal):
        print("O custo de estocagem de {} foi de {}".format(meses_ano[i], valor))
        custo_estoque_total += valor
    print("O custo com o estoque durante todo o ano foi de {}".format(custo_estoque_total))


def otimizar_estoque(estoque_atual):
    # definimos o minimo de estoque necessário considerando as vendas do ano
    estoque = 0
    maior_lucro = 0
    estoque_otimizado = 0
    # Verificamos o maior valor de vendas mensais, baseado no último ano
    for value in vendas_anual:
        if value > estoque:
            estoque = value
    for estoque_teste in range(estoque, estoque_atual+1):
        estoque_teste_ano = Estoque(estoque_teste)
        estoque_teste_ano.re_estocar(valor_venda, custo_compra)
        custo_teste_inicial = estoque_teste_ano.custo_estoque()
        valores_teste = calcular_valores_anual()
        valores_calculados = somar_valores(valores_teste)
        lucro_teste = valores_calculados[1] - custo_teste_inicial
        if lucro_teste > maior_lucro:
            maior_lucro = lucro_teste
            estoque_otimizado = estoque_teste
    print("O melhor estoque para se manter é {}, que dará um lucro de {}".format(estoque_otimizado, maior_lucro))

# Abrimos um novo estoque com o valor de máximo considerado no exemplo
estoque_ano = Estoque(estoque_minimo)

# preenchemos o estoque com o estoque inicial com o custo do produto inicial
estoque_ano.re_estocar(valor_venda, custo_compra)

# Calculamos o custo do estoque inicial
custo_inicial = estoque_ano.custo_estoque()

dados_anual = calcular_valores_anual()
somar_valores(dados_anual)

relatorio_anual(dados_anual[0], dados_anual[1], dados_anual[2], dados_anual[3], dados_anual[4], custo_inicial)

otimizar_estoque(estoque_minimo)
