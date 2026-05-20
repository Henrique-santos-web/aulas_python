import customtkinter as ctk
from banco import conectar

def salvar_dados():
    nome_digitado = caixa_nome.get()
    email_digitado = caixa_email.get()

    if nome_digitado == "" or email_digitado == "":
        lbl_mensagem.configure(text="Preencha todos os campos!", text_color="red")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    cmd_sql = "INSERT INTO clientes (nome, email) VALUES (?, ?)"
    cursor.execute(cmd_sql, (nome_digitado, email_digitado))

    conexao.commit()
    conexao.close()

    lbl_mensagem.configure(text="Cliente salvo com sucesso!", text_color="green")
    
    caixa_nome.delete(0, "end")
    caixa_email.delete(0, "end")
    atualizar_lista_visual()


def buscar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes")

    dados = cursor.fetchall()

    conexao.close()
    return dados


def atualizar_lista_visual():
    area_lista.delete("0.0", "end")

    clientes = buscar_clientes()

    for cliente in clientes:
        texto = f"ID: {cliente[0]} | {cliente[1]}\n"

        area_lista.insert("end", texto)


def excluir_cliente():
    id_digitado = caixa_id.get()
    if id_digitado == "": return

    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id_digitado, ))
    conexao.commit()

    if cursor.rowcount == 0:
        lbl_mensagem_excluir.configure(text="ID não econtrado!", text_color="red")
    else:
        lbl_mensagem_excluir.configure(text="Excluido!", text_color="black")
        caixa_id.delete(0, "end") # == ESSE DELETE 0 end significa que vai apagar qualquer resquício que tenha ficado na caixa de testo
        atualizar_lista_visual()


def buscar_cliente(id_cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    cmd_sql = "SELECT nome FROM clientes WHERE id = ?"
    cursor.execute(cmd_sql, (id_cliente, ))

    resultado = cursor.fetchone()

    if resultado:
        return resultado[0]
    

def salvar_alteracoes(id_cliente, novo_nome, janela_secundaria):
    cmd_sql = "UPDATE clientes SET nome=? WHERE id=?"
    
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute(cmd_sql, (novo_nome, id_cliente))
    conexao.commit()

    atualizar_lista_visual()
    janela_secundaria.destroy()
    

def abrir_janela_edicao():
    janela_edicao = ctk.CTkToplevel(janela)
    janela_edicao.geometry("300x200")
    janela_edicao.title("Editar")

    id_cliente = caixa_id.get()
    if id_cliente == "": return
    
    nome_antigo = buscar_cliente(id_cliente)

    cx_novo_nome = ctk.CTkEntry(janela_edicao)
    cx_novo_nome.pack(pady=20)

    if nome_antigo:
        cx_novo_nome.insert(0, nome_antigo)
    else:
        cx_novo_nome.insert(0, "Não encontrado")

    btn_salvar = ctk.CTkButton(
        janela_edicao,
        text="Salvar Alteração",
        command=lambda: salvar_alteracoes(id_cliente, cx_novo_nome.get(), janela_edicao)
    )
    btn_salvar.pack(pady=10)

    janela_edicao.focus()
    janela_edicao.grab_set() # == ENQUANTO TU NÃO FIZER O QUE ESTÁ SENDO PEDIDO, ESSA JANELA NÃO FECHA


janela = ctk.CTk()
janela.geometry("800x600")
janela.title("Cadastro de Clientes")

lbl_titulo= ctk.CTkLabel(janela, text="NOVO CLIENTE")
lbl_titulo.pack(pady=20)

caixa_nome = ctk.CTkEntry(janela, placeholder_text="Nome")
caixa_nome.pack(pady=10)

caixa_email = ctk.CTkEntry(janela, placeholder_text="E-mail")
caixa_email.pack(pady=10)

btn_salvar = ctk.CTkButton(
    janela, 
    text="Salvar", 
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
atualizar_lista_visual()

caixa_id = ctk.CTkEntry(
    janela,
    placeholder_text="ID p/ Excluir ou Editar"
) # == ESSA PARTE DO CÓDIGO MOSTRA PRO USUARIO A OPÇÃO DE ESCREVER ALGO(O que está sendo exigido) == 
caixa_id.pack(pady=5)

btn_excluir = ctk.CTkButton(
    janela,
    text="Excluir",
    fg_color="red",
    hover_color="darkred",
    command=excluir_cliente
)
btn_excluir.pack(pady=10)

btn_edicao = ctk.CTkButton(
    janela,
    text="Editar",
    fg_color="orange",
    hover_color="darkorange",
    command=abrir_janela_edicao
)
btn_edicao.pack(pady=10)

lbl_mensagem_excluir = ctk.CTkLabel(janela, text="")
lbl_mensagem_excluir.pack()

janela.mainloop()