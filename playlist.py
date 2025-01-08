class Playlist:
    def __init__(self,nome):
        self.nome = nome
        self.musica = []
    
    def adicionar_musica(self,musica):
        self.musica.append(musica)
        return f'Música {musica} adicionada a playlist {self.nome}'
    
    def remover_musica(self,musica):
        if musica in self.musica:
            self.musica.remove(musica)
            return f'Música {musica} removida da playlist {self.nome}'
            return f'Música {musica} não encontrada na playlist {self.nome}'
    
    def reproduzir(self,musica):
        if self.musica:
            return f'Reproduzindo {musica} da playlist {self.nome}'
        
            return f'Música {musica} não está na playlist {self.nome}'