class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor =  autor
        self.disponivel = True

    def mostrar_dados(self):
            print(f'Titulo: {self.titulo}\n Autor: {self.autor}\n Disponivel: {self.disponivel}\n ')

    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            print('livro emprestado com sucesso!')
        elif self.disponivel == False:
            print('Livro já está emprestado!')

    def devolver(self):
        if self.disponivel == False:
            self.disponivel = True
            print('Livro devolvido!')
        else:
            print('livro está disponivel')


livro1 = Livro('Noites Brancas', 'Fiódor Dostoiévski')
livro2 = Livro('Crime e Castigo', 'Dostoiévski ')
livro3 = Livro('Memórias do Subsolo', 'Fiódor Dostoiévsk')

        
lista_livros = [livro1, livro2, livro3]

for livro in lista_livros:
    livro.mostrar_dados()


while True:
    print('\n ====== BIBLIOTECA ====== ')
    print('1 - Listar Livros')
    print('2 - Emprestar Livro')
    print('3 - Devolver Livro')
    print('4 - Sair')

    opcao = input('Escolha uma opção!: ').strip()

    if opcao == '1':
      for livro in lista_livros:
          livro.mostrar_dados()

    elif opcao == '2':
        livrinho = input('Digite o livro que deseja emprestar: ').lower()
        encontrado = False
        for livro in lista_livros:
            if livrinho in livro.titulo.lower():
                livro.emprestar() 
                encontrado = True
                break
        if not encontrado:
            print('Livro não encontrado!')


    elif opcao ==  '3':
        livrinho = input('Digite o livro que deseja devolver: ').lower()
        encontrado = False
        for livro in lista_livros:
            if livrinho in livro.titulo.lower():
                livro.devolver()
                encontrado = True
                break
        if not encontrado:
            print('Livro não encontrado!')


    elif opcao == '4':
        print('Programa Fechado!')
        break