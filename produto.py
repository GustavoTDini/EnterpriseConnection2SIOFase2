class produto:
    def __init__(self, valor_venda, valor_compra):
        self.valor_venda = valor_venda
        self.valor_compra = valor_compra

    def valor_de_venda(self):
        return self.valor_venda

    def valor_de_compra(self):
        return self.valor_compra

    def lucro(self):
        return self.valor_venda - self.valor_compra
