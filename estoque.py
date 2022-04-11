from produto import Produto


# Classe para o controle do nosso estoque, baseado em uma fila
class Estoque:
    # Definição do estoque e indicando quanto será o estoque a ser mantido
    def __init__(self, estoque_total):
        self.estoque = []
        self.estoque_total = estoque_total

    # função para colocar um novo produto no estoque
    def estocar(self, novo_produto):
        self.estoque.append(novo_produto)

    # função para selecionar um produto do estoque
    def pegar_produto(self, index):
        return self.estoque[index]

    # função que realiza uma venda, retira o produto mais antigo do estoque e calcula seu lucro,
    # considerando o custo deste
    def venda(self):
        lucro = 0
        if not self.sem_estoque():
            lucro = self.estoque[0].lucro()
            self.estoque.pop(0)
        return lucro

    # função que verifica se o estoque está vazio
    def sem_estoque(self):
        return not self.estoque

    # função que retorna a quantidade de produtos no estoque
    def quantidade_estoque(self):
        return len(self.estoque)

    # função que re-estoca até o total definido considerando o valor de compra do mês, retorna o custo desta compra
    def re_estocar(self, valor_venda, custo_compra):
        quantidade_a_comprar = 0
        if self.quantidade_estoque() < self.estoque_total:
            quantidade_a_comprar = self.estoque_total - self.quantidade_estoque()
        for i in range(quantidade_a_comprar):
            self.estocar(Produto(valor_venda, custo_compra))
        return custo_compra * quantidade_a_comprar

    # função para determinar o custo total do atual estoque, considerando os diversos valores de compra
    def custo_estoque(self):
        valor_estoque = 0
        for produto_estocado in self.estoque:
            valor_estoque += produto_estocado.valor_de_compra()
        return valor_estoque
