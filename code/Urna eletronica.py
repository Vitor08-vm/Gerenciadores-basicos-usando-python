import os 

class Candidato:
    def __init__(self, numero, nome, voto = 0):
        self.numero = int(numero)
        self.nome = str(nome)
        self.voto = int(voto)

class UrnaEletronica:
    def __init__(self, arquivo_auditoria="auditoria.txt", dicionario = {}):
        self.arquivo_auditoria = arquivo_auditoria
        self.dicionario = dicionario

    def cadastrar_candidato(self, candidato):
        self.dicionario.update({candidato.numero:candidato})

    def votar(self, numero): 
        with open(f"{self.arquivo_auditoria}","a") as arquivo:
            arquivo.write(f"Voto computado para: {numero}\n")

    def gerar_resultado_txt(self, arq_saida):     
        with open(f"{self.arquivo_auditoria}","r") as entrada:
            for linha in entrada:
                if not linha:
                    continue
                else: 
                    linha = linha.split(":")
                    num_candidato = linha[1]
                    for num, objeto in self.dicionario.items():
                        if num == int(num_candidato):
                            objeto.voto += 1

        chaves = list(self.dicionario.keys())
        for k in range(len(chaves)):
            maior_indice = k
            mais_votado = chaves[maior_indice]
            for j in range(k+1, len(chaves)):
                menos_votado = chaves[j]
                objeto1 = self.dicionario[mais_votado]
                objeto2 = self.dicionario[menos_votado]
                if objeto1.voto < objeto2.voto:
                    maior_indice = j        
            chaves[k], chaves[maior_indice] = chaves[maior_indice], chaves[k]       

        with open(f"{arq_saida}", "a") as saida:
            for chave in chaves:
                candidato = self.dicionario[chave]
                saida.write(f"{chave};{candidato.nome};{candidato.voto}\n")
