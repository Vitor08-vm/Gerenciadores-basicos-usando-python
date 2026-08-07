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

