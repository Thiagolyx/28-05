class Livro:
    def __init__(self):
        self.__titulo = ""

    def definir_titulo(self, t):
        self.__titulo = t

    def mostrar_titulo(self):
        print(f"O título do livro é: {self.__titulo}")

# Criando dois objetos
livro1 = Livro()
livro2 = Livro()

# Definindo títulos
livro1.definir_titulo("ed & Lorraine Warren")
livro2.definir_titulo("Guerra e a Paz")

# Mostrando os títulos
livro1.mostrar_titulo()
livro2.mostrar_titulo()