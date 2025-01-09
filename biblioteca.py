class Livro:
    lista_livro = []

    def __init__(self, titulo, autor, ano_publicado):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicado = ano_publicado
        self._disponivel = True
        Livro.lista_livro.append(self)

    def emprestar(self):
        if self._disponivel:
            self._disponivel = False
            return f'O livro {self.titulo} foi emprestado.'
        else:
            return f'O livro {self.titulo} já está emprestado.'

    def devolver(self):
        if not self.disponivel:
            self._disponivel = True
            return f'O livro {self.titulo} foi devolvido.'   
        else:
            return f'O livro {self.titulo} já está disponível.'
    
    def esta_disponivel(self):
        return self._disponivel

        
            