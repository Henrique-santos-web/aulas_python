from Gato.Gato import Gato
from Cachorro.Cachorro import Cachorro
from Animal.Animal import Animal

meu_animal = Animal("Meu animal")
meu_animal.emitir_som()

meu_cachorro = Cachorro("Pedro")
meu_gato = Gato("Cinza")

meu_cachorro.emitir_som()
meu_gato.emitir_som()

#* Neste contexto — isso inclui o arquivo "Gato" também — foi necessario pôr um ponto e chamar o mesmo nome
#* Pois eu tive que chamar a pasta, depois a class correspondente
