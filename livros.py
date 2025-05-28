class Livro:
    def __init__(self):
        self.__titulo = ""

    def definir_titulo(self, t):
        self.__titulo = t

    def mostrar_titulo(self):
        print(f"O título do livro é: {self.__titulo}")

# Criando dois objetos
livro3 = Livro()
livro4 = Livro()

# Definindo títulos
livro3.definir_titulo("it a coisa")
livro4.definir_titulo("diario de um banana")

# Mostrando os títulos
livro3.mostrar_titulo()
livro4.mostrar_titulo()