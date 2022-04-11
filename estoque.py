from produto import produto


class estoque:
    def __init__(self, estoque_total):
        self.estoque = []
        self.estoque_total = estoque_total

    def estocar(self, produto):
        self.estoque.append(produto)

    def pegar_produto(self, index):
        return self.estoque[index]

    def venda(self):
        lucro = produto.lucro(self.estoque[0])
        self.estoque.pop(0)
        return lucro

    def quantidade_estoque(self):
        return len(self.estoque)

    def restocar(self, custo_atual, valor_venda):
        quantidade_a_comprar = 0
        if self.quantidade_estoque() < self.estoque_total:
            quantidade_a_comprar = self.estoque_total - self.quantidade_estoque()
        for i in range(quantidade_a_comprar):
            self.estocar(produto(valor_venda, custo_atual))

    def custo_estoque(self):
        valor_estoque = 0
        for produto in self.estoque:
            valor_estoque += produto.valor_de_compra()
        return valor_estoque
