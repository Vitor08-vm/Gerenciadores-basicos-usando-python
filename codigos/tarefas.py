import os

class Tarefa:
    
    def __init__(self, titulo, descricao, prioridade, concluida = False):
        self.titulo = str(titulo)
        self.descricao = str(descricao)
        self.prioridade = str(prioridade)
        self.concluida = bool(concluida)

class ListaTarefas:
    
    def __init__(self):
        self.lista_salvar = {}
    
    def adicionar(self, tarefa):
        self.lista_salvar.update({tarefa.titulo:tarefa})

    def concluir(self, titulo):
        if titulo in self.lista_salvar:
            self.lista_salvar[titulo].concluida = True
        return self.lista_salvar        
    
    def obter_tarefa(self, titulo):
        try:
            if titulo in self.lista_salvar:
                return self.lista_salvar[titulo]
        except:
            return      

    def salvar(self, tasks):
        with open(tasks, "w") as t:
            for tarefas in self.lista_salvar.values():
                t.write(f"{tarefas.titulo};{tarefas.descricao};{tarefas.prioridade};{tarefas.concluida}\n")

    def carregar(self, tasks):
        with open(tasks,"r") as t:
            for linha in t:
                if not linha:
                    continue 
                linha = linha.strip()
                titulo, descricao, prioridade, concluida = linha.split(";")
                tarefa = Tarefa(titulo, descricao, prioridade, concluida == "True") 
                self.lista_salvar.update({titulo:tarefa})

commitment = Tarefa(titulo = "Estudar G.A", descricao = "das 9 às 12:00", prioridade = "Alta", concluida = False)

task_daily = ListaTarefas()
task_daily.adicionar(commitment)
task_daily.concluir(commitment.titulo)

task_daily.salvar("tarefas.txt")
task_daily2 = ListaTarefas()
task_daily2.carregar("tarefas.txt")



                
