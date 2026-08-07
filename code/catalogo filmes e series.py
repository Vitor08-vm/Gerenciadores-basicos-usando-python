import os

class Midia:
    def __init__(self, titulo, ano, genero):
        self.titulo = str(titulo)
        self.ano = str(ano)
        self.genero = str(genero)

class Filme(Midia):
    def __init__(self, titulo, ano, genero, duracao_minutos):
        super().__init__(titulo, ano, genero)
        self.duracao_minutos = duracao_minutos

class Serie(Midia):
    def __init__(self,titulo,ano,genero,temporadas):
        super().__init__(titulo, ano, genero)
        self.temporadas = temporadas    

class Catalogo:
    def __init__(self, catalogo = []):
        self.catalogo = catalogo

    def adicionar_midia(self, midia):
        self.catalogo.append(midia)
    
    def salvar_catalogo(self, caminho): 
        with open(f"{caminho}", "a") as arquivo:
            for midias in self.catalogo:
                try:
                    if midias.duracao_minutos:
                        arquivo.write(f"Filme;{midias.titulo};{midias.ano};{midias.genero};{midias.duracao_minutos}\n")

                except AttributeError:
                    if midias.temporadas:
                        arquivo.write(f"Serie;{midias.titulo};{midias.ano};{midias.genero};{midias.temporadas}\n")

    def carregar_catalogo(self, caminho):
        with open(f"{caminho}", "r") as arquivo:
            for linha in arquivo:
                if not linha:
                    continue
                else:
                    linha = linha.strip()
                    divisao = linha.split(";")
                    if divisao[0] == "Filme":
                        tipo, titulo, ano, genero, minutos = divisao
                        midia = Filme(titulo, ano, genero, minutos) 
                    elif divisao[0] == "Serie":
                        tipo, titulo, ano, genero, temporadas = divisao
                        midia = Serie(titulo, ano, genero, temporadas)
                    self.adicionar_midia(midia)

