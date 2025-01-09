from biblioteca import Livro
#adicionando livros
livro1 = Livro('As ondas', 'Virginia Woolf', 1931)
livro2 = Livro('Mortes em pleno verão', 'Yukio Mishima', 2024)
livro3 = Livro('Noites brancas', 'Fiódor Dostoiévski', 1848)
livro4 = Livro('Perto do coração selvagem', 'Clarice Lispector', 1943)
livro5 = Livro('Relatos de um gato viajante', 'Hiro Arikawa', 2017)

# utilizando os métodos da classe
print(livro1.emprestar())
print(livro1.emprestar())  # tentativa de emprestar um livro que já está sendo emprestado
print(livro4.esta_disponivel())
print(livro5.emprestar())
print(livro2.esta_disponivel())

# listando os livros
for livro in Livro.lista_livro:
    status = "Disponível" if livro.esta_disponivel() else "Emprestado"
    print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano_publicado}, Status: {status}")

