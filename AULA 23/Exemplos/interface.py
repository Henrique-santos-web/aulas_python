import customtkinter as ctk
from banco import conectar, banco_estoque, buscar_clientes

def salvar_dados():
    nome_digitado = caixa_nome.get()
    produto_digitado = caixa_produto.get()

    if nome_digitado == "" or produto_digitado == "":
        lbl_mensagem.configure(text="Preencha todos os campos!", text_color = "red")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    cmd_sql = "INSERT INTO produtos (nome_produto, quantidade) VALUES (?, ?)"
    cursor.execute(cmd_sql, (nome_digitado, produto_digitado))

    conexao.commit()
    conexao.close()

    lbl_mensagem.configure(text="Produto salvo com sucesso!", text_color="green")

    caixa_nome.delete(0, "end")
    caixa_produto.delete(0, "end")


def atualizar_lista_visual():
    area_lista.delete("0.0", "end")

    clientes = buscar_clientes()

    for cliente in cliente:

        texto = f"ID: {cliente[0]} | {cliente[1]}\n"

    area_lista.insert("end", texto)



janela = ctk.CTk()
janela.geometry("400x400")
janela.title("Cadastro de Cliente")

lbl_titulo = ctk.CTkLabel(janela, text="NOVO CLIENTE ")
lbl_titulo.pack(pady=20)

caixa_nome = ctk.CTkEntry(janela, placeholder_text = "nome")
caixa_nome.pack(pady=20)

caixa_produto = ctk.CTkEntry(janela, placeholder_text = "quantidade")
caixa_produto.pack(pady=20)

btn_salvar = ctk.CTkButton(
    janela, 
    text="cadastrar", 
    command=salvar_dados
)
btn_salvar.pack(pady=20)

lbl_mensagem = ctk.CTkLabel(janela, text="")
lbl_mensagem.pack()

area_lista = ctk.CTkTextbox(
    janela,
    width=350,
    height=150
)
area_lista.pack(pady=10)


janela.mainloop()