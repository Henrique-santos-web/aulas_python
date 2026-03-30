nota = float(input("Nota (0 a 10): "))

if nota >= 9:
    print("Aprovado!!!")
elif nota >= 7:
    print("Aprovado!!")
elif nota >= 5:
    print("Recuperação!")
else:
    print("Reprovado")