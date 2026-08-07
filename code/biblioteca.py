import os

class Livro:
    def __init__(self, id, titulo, autor, disponivel = True): 
        self.id = str(id)
        self.titulo = str(titulo) 
        self.autor = str(autor)
        self.disponivel = bool(disponivel)

class Usuario:
    def __init__(self, id, nome, livros_emprestados = []): 
        self.id = str(id)
        self.nome = str(nome)
        self.livros_emprestados = list(livros_emprestados)

class SistemaBiblioteca:

    def __init__(self, livros = {}, usuarios = {}):
        self.livros = livros
        self.usuarios = usuarios

    def cadastrar_livro(self,livro):
        self.livros.update({livro.id:livro})
        return self.livros
    
    def cadastrar_usuario(self,user):
        self.usuarios.update({user.id:user})
        return self.usuarios

    def obter_livro(self, id_livro):
        self.id_livro = self.livros.get(id_livro, False)
        if self.id_livro:
            return self.id_livro

    def obter_usuario(self, id_u):    
        self.id_u = self.usuarios.get(id_u, False)
        if self.id_u:
            return self.id_u
        
    def realizar_emprestimo(self,id_usuario, id_livro):
        if self.obter_livro(id_livro) and self.obter_usuario(id_usuario):
            if self.livros[id_livro].disponivel:
                self.obter_usuario(id_usuario).livros_emprestados.append(self.livros[id_livro])
                self.livros[id_livro].disponivel = False
                return True
        else:
            return "Empréstimo não realizado"    
        
    def salvar_dados(self, arq_livros, arq_usuarios):
        with open("livros.txt", "a") as arq_livros:
            for id1, objeto in self.livros.items():
                arq_livros.write(f"{id1};{objeto.autor}; {objeto.titulo}; {objeto.disponivel}")           

        with open("usuarios.txt", "a") as arq_usuarios:
            aux = []
            for id2, objeto in self.usuarios.items():
                for livros in objeto.livros_emprestados:
                    aux.append(livros.id)
            aux = "|".join(aux)        
            arq_usuarios.write(f"{id2};{objeto.nome};{aux}\n")

    def carregar_dados(self, arq_livros, arq_usuarios):
        with open("livros.txt", "r") as arquivo:
            for linhas in arquivo:
                if not linhas:
                    continue
                else:
                    try:
                        id, titulo, autor, disponivel = linhas.split(";")
                        livro = Livro(id, titulo, autor, disponivel == 'True')
                        self.livros.update({id:livro})
                    except IndexError:
                        continue

        with open("usuarios.txt", "r") as arquivo:
                for linhas in arquivo:
                    if not linhas:
                        continue
                    else:
                        usuario = Usuario(id, nome, [])
                        divisao = linhas.split(";") 
                        id, nome = divisao[0], divisao[1]
                        if len(divisao) > 2:
                            livros_emprestados = divisao[2]
                            livros_emprestados = livros_emprestados.split("|")

                            for index in livros_emprestados:
                                objeto = self.obter_livro(index)
                                if objeto:
                                    usuario.livros_emprestados.append(objeto)                                 
                        try:
                            self.usuarios.update({id:usuario}) 
                        except IndexError:
                            continue    
    
