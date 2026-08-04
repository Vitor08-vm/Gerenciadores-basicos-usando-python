import os

class Produto:
    def __init__(self, id, nome, preco, quantidade):
        self.id = str(id)
        self.nome = str(nome)
        self.preco = float(preco)
        self.quantidade = int(quantidade)

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def salvar_estoque(self, arquivo):
        with open("estoque.txt", "w") as arquivo:
            for prod in self.produtos:
                arquivo.write(f"{prod.id};{prod.nome};{prod.preco};{prod.quantidade}\n")      
                        
    def carregar_estoque(self, arquivo):           
        with open("estoque.txt","r") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                id, nome, preco, quantidade = linha.split(";")
                linha = Produto(id, nome, preco, quantidade)
                self.produtos.append(linha)
        return self.produtos        

Material1 = Produto(id = "ID_0123", nome = "Martelo", preco = 5.00, quantidade = 100)
Material2 = Produto(id = "ID_0001", nome = "Chave de Fenda", preco = 10.00, quantidade = 50)
Material3 = Produto(id = "ID_0003", nome = "Serra", preco = 20.00, quantidade = 250)

estoque = Estoque()

estoque.adicionar_produto(Material1)
estoque.adicionar_produto(Material2)
estoque.adicionar_produto(Material3)

estoque.salvar_estoque("estoque.txt")
estoque2 = Estoque()
print(estoque2.carregar_estoque("estoque.txt"))
