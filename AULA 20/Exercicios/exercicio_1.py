import customtkinter as ctk

janela = ctk.CTk()
janela.geometry("600x400")

painel_topo = ctk.CTkFrame(janela)
painel_topo.pack(side="top", fill="x", pady=10)
lbl = ctk.CTkLabel(painel_topo, text="Sistema ERP")
lbl.pack

painel_baixo = ctk.CTkFrame(janela)
painel_baixo.pack(side="bottom", fill="both", expand=True)
painel_baixo = ctk.CTkButton(text="Entrar")

janela.mainloop()