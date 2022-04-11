# Classe que contem as informações de um produto
class Produto:
    # Definição do produto, considera o valor para vendas e custo de compras
    def __init__(self, valor_venda, custo_compra):
        self.valor_venda = valor_venda
        self.custo_compra = custo_compra

    # Função que retorna o valor de venda do produto
    def valor_de_venda(self):
        return self.valor_venda

    # Função que retorna o custo de compra do produto
    def valor_de_compra(self):
        return self.custo_compra

    # Função que retorna o lucro do produto, por quanto ele foi vendido menos quanto custou
    def lucro(self):
        return self.valor_venda - self.custo_compra
