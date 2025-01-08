print("Iniciando importação")
from playlist import Playlist
print("Importação concluída")

minha_playlist = Playlist('Frank Ocean discografia')
print(minha_playlist.adicionar_musica('Lost!'))
print(minha_playlist.remover_musica('Cayendo'))
print(minha_playlist.reproduzir('White ferrari'))
