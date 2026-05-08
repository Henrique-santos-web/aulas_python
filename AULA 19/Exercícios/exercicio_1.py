import customtkinter as ctk

janela = ctk.CTk()

janela.geometry("600x400")

janela.title("Painel de Controle")

lbl_painel_de_controle = ctk.CTkLabel(
    janela,
    text=("Painel de controle 1"),
    font=("Arial", 20, "bold")
)

lbl_painel_de_controle2 = ctk.CTkLabel(
    janela,
    text=("Painel de controle 2"),
    font=("Helvetica", 20)
)

lbl_painel_de_controle3 = ctk.CTkLabel(
    janela,
    text=("Painel de controle 3"),
    font=("Georgia", 20)
)

lbl_painel_de_controle.pack(pady=10)
lbl_painel_de_controle2.pack(pady=5)
lbl_painel_de_controle3.pack(pady=60)

janela.mainloop()