import customtkinter as ctk

def ao_clicar():
    texto = caixa_texto.get()
    if texto:
        msg_final.configure(text=f"Olá, {texto}")
    else:
        msg_final.configure(text="")

janela = ctk.CTk()

janela.geometry("400x300")

janela.title("Meu App com Configure")

caixa_texto = ctk.CTkEntry(janela)
botao = ctk.CTkButton(
    janela,
    text="Entrar",
    command=ao_clicar
)

msg_final = ctk.CTkLabel(janela, text="")

caixa_texto.pack(pady=20)
botao.pack(pady=10)
msg_final.pack(pady=50)

janela.mainloop()