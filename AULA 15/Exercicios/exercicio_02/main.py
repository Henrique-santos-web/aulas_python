from Carro import Carro

meu_carro = Carro()
carro_do_chefe = Carro()

if __name__ == "__main__":
    meu_carro.marca = "Ford"
    meu_carro.cor = "Azul Goiaba"

    carro_do_chefe.marca = "BMW"    
    carro_do_chefe.cor = "Preto"

print(f"O meu carro é:\nCor: {meu_carro.cor}\nMarca: {meu_carro.marca}")
print(f"O carro do meu chefe é:\nCor: {carro_do_chefe.cor}\nMarca: {carro_do_chefe.marca}")