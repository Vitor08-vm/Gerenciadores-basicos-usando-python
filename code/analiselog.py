import os

class LogParser:
    def __init__(self,dicionario = {}):
        self.dicionario = dict(dicionario) 

    def analisar_arquivos(self, arq_entrada):
        with open(f"{arq_entrada}", "r") as arq:
            for linha in arq:
                if not linha:
                    continue
                else:
                    linha = linha.strip()
                    divisao = linha.split("-")
                    tipo, mensagem = divisao[0], divisao[4]
                    tipo = list(tipo)
                    for carac in tipo:
                        if carac == " ":
                            tipo.remove(carac)
                    tipo = "".join(tipo)        
                    if tipo in ("ERROR", "CRITICAL"):
                        self.dicionario.update({tipo:mensagem})
                    else:
                        continue    

    def gerar_relatorios(self, arq_saida):        
        with open(f"{arq_saida}", "a") as arq:    
            if len(self.dicionario) > 0:
                for erro, mensagem in self.dicionario.items():
                    arq.write(f"[{erro}] {mensagem}\n")
            else:
                arq.write(f"Nenhum log critico ou erro econtrado")
