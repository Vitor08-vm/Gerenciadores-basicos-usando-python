import os

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = str(nome)
        self.telefone = str(telefone)
        self.email = str(email)

class Agenda:
    def __init__(self):
        self.agenda_salvar = []
    
    def adicionar_contato(self, contato):
        self.agenda_salvar.append(contato)

    def salvar_contatos(self,contacts):
        with open(contacts, "w") as c:
            for contato in self.agenda_salvar:
                c.write(f"{contato.nome};{contato.telefone};{contato.email}\n")

    def carregar_contatos(self, contacts):            
        with open(contacts,"r") as c:
            for linha in c:
                if not linha:
                    continue
                linha = linha.strip()
                nome, telefone, email = linha.split(";")
                amigo = Contato(nome, telefone, email)
                self.agenda_salvar.append(amigo)
        return self.agenda_salvar

#exemplo de uso    
amigo = Contato(nome = "", telefone = "", email = "")
contact = Agenda()
contact.adicionar_contato(amigo)
contact.salvar_contatos("agenda.txt")

