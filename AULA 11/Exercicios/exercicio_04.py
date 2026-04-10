# import datetime

# def saudacao_hora():
#     hora_atual = datetime.datetime.now().hour
    
#     if hora_atual == 6:
#         print("Bom dia!")
#     elif hora_atual >= 12 and hora_atual < 18:
#         print("Boa tarde!")
#     elif hora_atual >= 19 and hora_atual < 00:
#         print("Boa noite")
#     else:
#         print("O crime nunca dorme, Batman!")
# saudacao_hora()

# *Minha versão acima

import datetime

def saudacao_hora():
    hora_atual = datetime.datetime.now().hour

    if hora_atual < 12:
        print("Bom dia")
    elif hora_atual < 18:
        print("Boa tarde")
    else:
        print("Boa noite")

saudacao_hora()

# ! Estudar a minha versão para saber o pq dela  ter mostrado o Boa noite