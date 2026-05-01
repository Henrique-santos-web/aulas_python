from Cachorro import Cachorro
from Gato import Gato
from Vaca import Vaca

meu_cao = Cachorro("Rex")
meu_gato = Gato("Kimi")
minha_vaca = Vaca("Mimosa")

animais = [meu_cao, meu_gato, minha_vaca]

for animal in animais:
    print(animal.emitir_som())