import customtkinter as ctk

cliques = 0

def ao_clicar():
    global cliques
    cliques += 1
    print(f"Número de cliques: {cliques}")

janela = ctk.CTk()
janela.geometry("400x300")
janela.title("Janela de cliques")


botao = ctk.CTkButton(
    janela,
    text="Me clique(lá ele)",
    command=ao_clicar
)


botao.pack(pady=10)

janela.mainloop()