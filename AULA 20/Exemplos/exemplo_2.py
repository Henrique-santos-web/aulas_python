import customtkinter as ctk

janela = ctk.CTk()
janela.geometry("600x600")

lbl = ctk.CTkLabel(
    janela,
    text="Nome: "
)
lbl.grid(row=0, column=0, padx=10)

caixa = ctk.CTkEntry(janela)
caixa.grid = ctk.CTk(row=0, column=1)

btn = ctk.CTkButton(janela, text="Salvar")
btn.grid(row=1, column=0, columnspan=2, )