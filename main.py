import os
from funcoes_auxiliares import *

# Definição de valores iniciais
valor_venda = float(50)
custo_compra = float(30)
estoque_minimo = 1000
custo_compra_anual = [30, 25, 35, 43, 32, 32, 32, 34, 45, 30, 33, 35]
vendas_anual = [225, 300, 333, 352, 145, 842, 144, 752, 520, 222, 127, 333]
meses_ano = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julio", "Agosto", "Setembro", "Outubro",
             "Novembro", "Dezembro"]

# Perguntamos ao usuário se ele que criar os valores ou utilizar o padrão
selecao = input_duas_respostas("Deseja Cadastrar novos valores? S - sim, N - não ", "s", "n")
print("\n")

# Caso o usuário selecione S - abrirá as opções de colocar novos valores
if selecao == "s":
    valor_venda = input_somente_numeros("Digite o valor de venda do produto: ")
    estoque_minimo = input_somente_numeros("Digite o valor de estoque mínimo: ")
    custo_compra = input_somente_numeros("Digite o valor do custo inicial: ")
    for i in range(0, len(meses_ano)):
        custo_compra_anual[i] = input_somente_numeros("Digite o custo do produto de {}: ".format(meses_ano[i]))
        vendas_anual[i] = input_somente_numeros("Digite as vendas de {}: ".format(meses_ano[i]))
    print("\n")

# criação do dicionário tipo JSon com a consolidação dos valores
valor_x_vendas = criar_dicionario_json(valor_venda, custo_compra_anual, vendas_anual, meses_ano)
print(valor_x_vendas)

# Abrimos um novo estoque com o valor de máximo considerado no exemplo
estoque_ano = Estoque(estoque_minimo)

# preenchemos o estoque com o estoque inicial com o custo do produto inicial
estoque_ano.re_estocar(valor_venda, custo_compra)

# Calculamos o custo do estoque inicial
custo_inicial = estoque_ano.custo_estoque()

dados_anual = calcular_valores_anual(valor_x_vendas, estoque_ano)
somar_valores(dados_anual)

while selecao != "p" or selecao != "s":
    selecao = input("Deseja Printar ou Salvar o relatório em um arquivo? P - printar, S - salvar ")
    print("\n")
    if selecao == "p":
        relatorio_anual(dados_anual[0], dados_anual[1], dados_anual[2], dados_anual[3], dados_anual[4],
                        custo_inicial, meses_ano, None)
        print(otimizar_estoque(estoque_minimo, vendas_anual, valor_venda, custo_compra, valor_x_vendas))
    elif selecao == "s":
        pasta = input("Digite a pasta aonde o arquivo será salvo: ")
        if not os.path.isdir("c:/{}".format(pasta)):
            os.mkdir("c:/{}".format(pasta))
        arquivo = input("Digite nome do arquivo que será salvo: ")
        abrir_arquivo = open("c:/{}/{}.txt".format(pasta, arquivo), "a")
        relatorio_anual(dados_anual[0], dados_anual[1], dados_anual[2], dados_anual[3], dados_anual[4],
                        custo_inicial, meses_ano, abrir_arquivo)
        abrir_arquivo.write(otimizar_estoque(estoque_minimo, vendas_anual, valor_venda, custo_compra, valor_x_vendas))
        abrir_arquivo.close()
    break
