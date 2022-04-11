class produto:
    def __init__(self, valor_venda, custo_compra):
        self.valor_venda = valor_venda
        self.custo_compra = custo_compra

    def valor_de_venda(self):
        return self.valor_venda

    def valor_de_compra(self):
        return self.custo_compra

    def lucro(self):
        return self.valor_venda - self.custo_compra
