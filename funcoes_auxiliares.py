from estoque import Estoque


# função para aceitar apenas 2 repostas para um input
def input_duas_respostas(pergunta, resposta_a, resposta_b):
    while True:
        resposta = input(pergunta)
        if resposta == resposta_a or resposta == resposta_b:
            return resposta


# função para aceitar apenas números para um input
def input_somente_numeros(pergunta):
    resposta = "o"
    while not type(resposta) == int:
        resposta = input(pergunta)
        try:
            resposta = int(resposta)
        except ValueError:
            print("Não é um número")
    return resposta


# função que faz a soma de valores de uma lista
def somar_valores(listas):
    nova_lista = [0] * len(listas)
    for i, lista in enumerate(listas):
        if type(lista) == list:
            for j in lista:
                nova_lista[i] += j
    return nova_lista


# função para printar ou escrever em um arquivo
def print_save(texto, arquivo):
    if arquivo is not None:
        arquivo.write(texto)
        arquivo.write("\n")
    else:
        print(texto)


# função que cria o dicionário Json com os dados de vendas
def criar_dicionario_json(valor_venda, custo_compra_list, vendas_list, meses):
    dicionario = {}
    for i, mes in enumerate(meses):
        dicionario[i + 1] = {
            "custo_compra": custo_compra_list[0],
            "valor_venda": valor_venda,
            "vendas": vendas_list[0],
            "mes": mes
        }
    return dicionario


# Função para verificar e retornar os diversos valores a serem estudados
def calcular_valores_anual(valor_x_vendas, estoque):
    # Listas que vão ser preenchidas com os dados coletados
    lucro_mensal_por_produto = []
    lucro_mensal = []
    valor_de_vendas_mensal = []
    custo_de_re_estocagem_mensal = []
    custo_estoque_final = 0
    # Iteração para verificar casa mês do ano baseado em nosso dicionário
    for i in range(1, 13):
        lucro = 0
        vendas = 0
        # Iteração fazer as vendas, considerando o quanto foi vendido em cada mês
        for p in range(valor_x_vendas[i]["vendas"]):
            vendas += valor_x_vendas[i]["valor_venda"]
            # Utilizando a função do Estoque, retira o produto mais antigo e soma o seu valor ao lucro por produto
            lucro += estoque.venda()
        # Utilizando a função do Estoque calculamos o custo mensal de estoque e o completamos até o valor definido
        custo_estoque = float(
            estoque.re_estocar(valor_x_vendas[i]["valor_venda"], valor_x_vendas[i]["custo_compra"]))
        lucro_mensal_por_produto.append(lucro)
        valor_de_vendas_mensal.append(vendas)
        custo_de_re_estocagem_mensal.append(custo_estoque)
        lucro_mensal.append(vendas - custo_estoque)
        custo_estoque_final = estoque.custo_estoque()
    return [lucro_mensal, lucro_mensal_por_produto, valor_de_vendas_mensal, custo_de_re_estocagem_mensal,
            custo_estoque_final]


def otimizar_estoque(estoque_atual, vendas_anual, valor_venda, custo_compra, valor_x_vendas):
    # definimos o minimo de estoque necessário considerando as vendas do ano
    estoque = 0
    maior_lucro = 0
    estoque_otimizado = 0
    # Verificamos o maior valor de vendas mensais, baseado no último ano
    for value in vendas_anual:
        if value > estoque:
            estoque = value
    for estoque_teste in range(estoque, estoque_atual + 1):
        estoque_teste_ano = Estoque(estoque_teste)
        estoque_teste_ano.re_estocar(valor_venda, custo_compra)
        custo_teste_inicial = estoque_teste_ano.custo_estoque()
        valores_teste = calcular_valores_anual(valor_x_vendas, estoque_teste_ano)
        valores_calculados = somar_valores(valores_teste)
        lucro_teste = valores_calculados[1] - custo_teste_inicial
        if lucro_teste > maior_lucro:
            maior_lucro = lucro_teste
            estoque_otimizado = estoque_teste
    return "O melhor estoque para se manter é {}, que dará um lucro de {}".format(estoque_otimizado, maior_lucro)


# Função que recebe os valores da verificação e os coleta em dados legíveis
def relatorio_anual(lucro_mensal, lucro_mensal_por_produto, valor_de_vendas_mensal, custo_de_re_estocagem_mensal,
                    custo_final_do_estoque, custo_inicial_do_estoque, meses_ano, arquivo):
    # Considerando o lucro pelas vendas temos que retirar o custo de estoque inicial
    lucro_anual = - custo_inicial_do_estoque
    for i, valor in enumerate(lucro_mensal):
        print_save("O lucro de {} foi {}".format(meses_ano[i], valor), arquivo)
        lucro_anual += valor
    print_save("O lucro anual considerando as venda e os custos de re-estocagem mensais é de {}".format(lucro_anual),
               arquivo)
    print_save("\n", arquivo)

    # Considerando o lucro por lucro individual de cada produto, temos que retirar o custo do estoque final
    lucro_anual_por_produto = -custo_final_do_estoque
    for i, valor in enumerate(lucro_mensal_por_produto):
        print_save("O lucro por produto de {} foi {}".format(meses_ano[i], valor), arquivo)
        lucro_anual_por_produto += valor
    print_save("O lucro anual considerando o custo de cada produto vendido é de {}".format(lucro_anual_por_produto),
               arquivo)
    print_save("\n", arquivo)

    vendas_total = -custo_inicial_do_estoque
    for i, valor in enumerate(valor_de_vendas_mensal):
        print_save("A receita de vendas de {} foi de {}".format(meses_ano[i], valor), arquivo)
        vendas_total += valor
    print_save("O receita de vendas do ano todo foi de {}".format(vendas_total), arquivo)
    print_save("\n", arquivo)

    custo_estoque_total = custo_inicial_do_estoque
    for i, valor in enumerate(custo_de_re_estocagem_mensal):
        print_save("O custo de estocagem de {} foi de {}".format(meses_ano[i], valor), arquivo)
        custo_estoque_total += valor
    print_save("O custo com o estoque durante todo o ano foi de {}".format(custo_estoque_total), arquivo)
    print_save("\n", arquivo)
