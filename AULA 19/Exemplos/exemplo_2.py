import customtkinter as ctk
#* "as" é apelidar o custom pra facilicar a hora de chamar ele (aqui será ctk)

def ao_clicar():
    nome_digitado = caixa_nome.get()
    print(f"O usuario digitou o {nome_digitado}")

janela = ctk.CTk()

janela.geometry("400x300")

janela.title("Meu App com Caixas de Texto")

caixa_nome = ctk.CTkEntry(
    janela,
    placeholder_text="Digite o seu nome",
    placeholder_text_color ="red",
    width=200
)

bota_enviar = ctk.CTkButton(
    janela, 
    text="Enviar dados",
    command=ao_clicar
)

caixa_nome.pack(pady=20)
bota_enviar.pack(pady=10)
janela.mainloop()