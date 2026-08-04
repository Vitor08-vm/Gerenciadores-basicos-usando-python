import os

def salvar_aluno(aluno, arquivo):
    with open("alunos.txt", "a") as arquivo:
        arquivo.write(f"{aluno.nome},{aluno.nota1},{aluno.nota2}\n")

def listar_aprovados(arquivo):
    aprovados = []
    with open("alunos.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue
            linha = linha.split(",")
            nome = linha[0]
            nota1 = float(linha[1])
            nota2 = float(linha[2])
            M = (nota1 + nota2) / 2
            if M >= 7:
                if nome not in aprovados:
                    aprovados.append(nome)
                else:
                    continue    
    return aprovados

class Aluno:

    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = float(nota1)
        self.nota2 = float(nota2)

    def calcular(self,nota1,nota2):
        self.media = (self.nota1 + self.nota2) / (2)
        return self.media

#exemplo de uso
aluno = Aluno(nome = "",nota1 = "",nota2 = "") 
salvar_aluno(aluno,"alunos.txt")

print(listar_aprovados("alunos.txt"))