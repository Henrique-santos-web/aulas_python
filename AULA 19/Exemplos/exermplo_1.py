import customtkinter as ctk
#* "as" é apelidar o custom pra facilicar a hora de chamar ele (aqui será ctk)

janela = ctk.CTk()

janela.geometry("500x300")

janela.title("Meu primeiro App")

boas_vindas = ctk.CTkLabel(
    janela,
    text="Olá, Mundo!", 
    font=("Arial", 24)
)

boas_vindas.pack(pady=20)

janela.mainloop()