nome_usuario = str(input("Qual o seu nome completo? "))

email_usuario = nome_usuario.strip().lower().replace(" ", "") + "@miranda.hs.com"

print(f"O seu novo email é: {email_usuario}")
