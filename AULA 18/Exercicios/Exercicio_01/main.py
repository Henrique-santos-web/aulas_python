from Forma import Forma #* Aqui n foi importado a mãe, pois sua função foi mudada
from Quadrado import Quadrado
from Retangulo import Retangulo

quadrado = Quadrado(10)
retangulo = Retangulo(10, 2)

formas = [quadrado, retangulo]

for forma in formas:
    print(forma.calcular_area()) #* Aqui nesse .calcular_area(), ele acessou cada forma de calcular area dos objetos