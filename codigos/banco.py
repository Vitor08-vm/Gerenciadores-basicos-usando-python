import os

class GerenciadorContas:
    
    def __init__(self):
        self.conta = []


    def adicionar_conta(self, conta):
        self.conta.append(conta)

    def obter_conta(self, titular):
        for conta in self.conta:
            if conta.titular == titular:
                return conta

    def salvar_contas(self, arquivo2):
        with open(arquivo2, "w") as f:
            for conta in self.conta:
                f.write(f"{conta.titular};{conta.saldo}\n")

    def carregar_contas(self, arquivo2):
        with open("contas.txt", "r") as f:
            for linha in f:
                if not linha:
                    continue
                titular, saldo = linha.split(";")
                conta =  ContaBancaria(titular, saldo)
                self.conta.append(conta)
        return self.conta                     

class ContaBancaria:

    def __init__(self, titular, saldo = 0.0):
        self.titular = str(titular)
        self.saldo = float(saldo)

    def depositar(self, valor):
        self.valor = float(valor)
        with open("transacoes.log", "a+") as arquivo1:
            arquivo1.write(f"DEPÓSITO DE {self.valor} | Saldo atual: {self.valor + self.saldo}\n")
        self.saldo += self.valor 

    def sacar(self, valor):
        if self.saldo > 0:        
            self.valor = float(valor)
            if self.valor <= self.saldo:
                with open("transacoes.log", "a+") as arquivo1:
                    arquivo1.write(f"SAQUE DE {self.saldo} | Saldo atual: {self.saldo-self.valor}\n")
            self.saldo -= self.valor

usuario = ContaBancaria(titular = "", saldo = 0.0)
usuario.depositar(0.0)
usuario.sacar(0.0)

conta = GerenciadorContas()
conta.adicionar_conta(usuario)
conta.salvar_contas("contas.txt")

conta2 = GerenciadorContas()
conta2.carregar_contas("contas.txt")
