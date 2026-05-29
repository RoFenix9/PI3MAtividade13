class Tarefa:
    tarefas = []

    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.concluido = False
        Tarefa.tarefas.append(self)

    def __str__(self):
        return f'{self.titulo} | {self.descricao}'

    @classmethod
    def listarTarefas(cls):
        for tarefa in cls.tarefas:
            print(tarefa)

    @classmethod
    def quantidadeTarefas(cls):
        return len(cls.tarefas)


tarefa_01 = Tarefa('Corrigir provas', 'Corrigir provas da turma')
tarefa_02 = Tarefa('Estudar Python', 'Estudar orientação a objetos')

print('Lista de tarefas:')
Tarefa.listarTarefas()

print('\nQuantidade de tarefas:', Tarefa.quantidadeTarefas())


#=========================================


class Pessoa:
    pessoas = []

    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        Pessoa.pessoas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.idade} anos | {self.profissao}'

    def aniversario(self):
        self.idade += 1


pessoa1 = Pessoa('Rodrigo', 17, 'Estudante e bolsista')

print('\nDados da pessoa:')
print(pessoa1)

pessoa1.aniversario()

print('\nDepois do aniversário:')
print(pessoa1)