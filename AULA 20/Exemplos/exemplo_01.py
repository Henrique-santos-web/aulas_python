import customtkinter as ctk

janela = ctk.CTk()
janela.geometry("400x300")

btn_esq = ctk.CTkButton(
    janela,
    text="Esquerda"
)

btn_esq.pack(side="left", padx=20)

btn_dir = ctk.CTkButton(
    janela,
    text="Direita"
)
btn_dir.pack(side="rigth", padx=20)

janela.mainloop()

#* corrigir depois