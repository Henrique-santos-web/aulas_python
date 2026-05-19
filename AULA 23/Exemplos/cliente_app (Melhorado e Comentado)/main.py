# Importa a biblioteca de interface gráfica (versão moderna do Tkinter)
import customtkinter as ctk
# Importa a biblioteca nativa do Python para lidar com banco de dados SQLite
import sqlite3
# Importa a função de conexão do arquivo banco.py (que criamos separadamente)
from banco import conectar

# ==========================================
# --- Função Auxiliar de Interface (UX) ---
# ==========================================

def exibir_mensagem(label, texto, cor):
    """
    Atualiza um rótulo (label) na tela com uma mensagem e altera sua cor.
    A mensagem desaparece automaticamente após 3 segundos.
    """
    # Altera o texto e a cor da letra do label passado por parâmetro
    label.configure(text=texto, text_color=cor)
    
    # Como 'janela' é global, usamos o método .after() para agendar uma ação.
    # 3000 milissegundos = 3 segundos. Após esse tempo, o texto do label vira vazio ("").
    janela.after(3000, lambda: label.configure(text=""))


# ==========================================
# --- Funções de Banco de Dados e Lógica ---
# ==========================================

def salvar_dados(caixa_nome, caixa_email, lbl_mensagem, area_lista):
    """
    Pega os dados digitados, valida, salva no banco de dados e atualiza a lista na tela.
    """
    # .get() pega o texto da caixa. .strip() remove espaços em branco no começo e no fim.
    nome_digitado = caixa_nome.get().strip()
    email_digitado = caixa_email.get().strip()

    # Verifica se algum dos campos ficou vazio após remover os espaços
    if not nome_digitado or not email_digitado:
        exibir_mensagem(lbl_mensagem, "Preencha todos os campos!", "red")
        return # Interrompe a função aqui se faltar dados

    try:
        # Abre a conexão com o banco usando 'with' (fecha automaticamente no final)
        with conectar() as conexao:
            cursor = conexao.cursor()
            # Comando SQL para inserir dados. Os '?' são proteções contra injeção de SQL.
            cmd_sql = "INSERT INTO clientes (nome, email) VALUES (?, ?)"
            # Executa o comando substituindo os '?' pelas variáveis correspondentes
            cursor.execute(cmd_sql, (nome_digitado, email_digitado))
        
        # Se deu tudo certo, exibe mensagem de sucesso
        exibir_mensagem(lbl_mensagem, "Cliente salvo com sucesso!", "green")
        
        # Limpa as caixas de texto (do índice 0 até o final "end")
        caixa_nome.delete(0, "end")
        caixa_email.delete(0, "end")
        
        # Atualiza a caixa de texto grande que mostra todos os clientes
        atualizar_lista_visual(area_lista)
        
        # Devolve o "foco" (o cursor piscando) para a caixa de nome
        caixa_nome.focus()
        
    except sqlite3.Error as erro:
        # Se ocorrer algum erro no banco de dados, exibe na tela
        exibir_mensagem(lbl_mensagem, f"Erro ao salvar: {erro}", "red")


def buscar_clientes():
    """
    Faz uma busca de todos os clientes registrados na tabela do banco de dados.
    Retorna uma lista com os registros encontrados.
    """
    try:
        with conectar() as conexao:
            cursor = conexao.cursor()
            # Seleciona TODAS as colunas (*) da tabela 'clientes'
            cursor.execute("SELECT * FROM clientes")
            # Pega todos os resultados encontrados e os retorna
            return cursor.fetchall()
    except sqlite3.Error:
        return [] # Se der erro, retorna uma lista vazia


def atualizar_lista_visual(area_lista):
    """
    Pega os clientes do banco e os exibe na caixa de texto grande (Textbox).
    """
    # Limpa a caixa de texto antes de inserir os dados atualizados (da linha 0.0 até o fim)
    area_lista.delete("0.0", "end")
    
    # Chama a função que busca os clientes no banco de dados
    clientes = buscar_clientes()
    
    # Para cada cliente encontrado, monta um texto e insere na caixa
    for cliente in clientes:
        # cliente[0] é o ID, cliente[1] é o Nome, cliente[2] é o Email
        texto = f"ID: {cliente[0]} | {cliente[1]} ({cliente[2]})\n"
        # Insere o texto montado no final da caixa de texto
        area_lista.insert("end", texto)


def excluir_cliente(caixa_id, lbl_mensagem_excluir, area_lista):
    """
    Exclui um cliente do banco de dados baseado no ID digitado.
    """
    id_digitado = caixa_id.get().strip()
    
    # Verifica se o que foi digitado é realmente um número
    if not id_digitado.isdigit():
        exibir_mensagem(lbl_mensagem_excluir, "Digite um ID numérico válido!", "red")
        return

    sucesso = False # Variável de controle para saber se devemos atualizar a tela

    try:
        # Abre a conexão e deleta
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM clientes WHERE id = ?", (id_digitado, ))
            
            # Se rowcount for maior que 0, significa que ele encontrou e deletou alguém
            if cursor.rowcount > 0:
                sucesso = True
        
        # Fora do 'with', o banco já salvou (commit) a exclusão.
        # Então podemos atualizar a parte visual da tela com segurança.
        if sucesso:
            exibir_mensagem(lbl_mensagem_excluir, "Excluído com sucesso!", "green")
            caixa_id.delete(0, "end")
            atualizar_lista_visual(area_lista)
        else:
            exibir_mensagem(lbl_mensagem_excluir, "ID não encontrado!", "red")
                
    except sqlite3.Error as erro:
        exibir_mensagem(lbl_mensagem_excluir, f"Erro: {erro}", "red")


def buscar_cliente_por_id(id_cliente):
    """
    Busca nome e e-mail de um cliente específico pelo ID. 
    Usado para preencher a janela de edição.
    """
    try:
        with conectar() as conexao:
            cursor = conexao.cursor()
            # Busca apenas nome e e-mail filtrando pelo ID
            cursor.execute("SELECT nome, email FROM clientes WHERE id = ?", (id_cliente, ))
            # Retorna apenas 1 resultado (fetchone), que será uma tupla (nome, email)
            return cursor.fetchone() 
    except sqlite3.Error:
        return None


def salvar_alteracoes(id_cliente, novo_nome, novo_email, janela_secundaria, area_lista, lbl_mensagem_excluir, caixa_id):
    """
    Recebe os dados novos da janela de edição e atualiza o banco de dados.
    """
    # Valida se os campos não estão em branco
    if not novo_nome.strip() or not novo_email.strip():
        return # Sai da função sem fazer nada se estiver em branco

    try:
        with conectar() as conexao:
            cursor = conexao.cursor()
            # Atualiza (UPDATE) nome e email onde o ID for igual ao selecionado
            cmd_sql = "UPDATE clientes SET nome=?, email=? WHERE id=?"
            cursor.execute(cmd_sql, (novo_nome, novo_email, id_cliente))
        
        # Atualiza a lista na janela principal
        atualizar_lista_visual(area_lista)
        
        # Fecha e destrói a janela de edição (a janela menor)
        janela_secundaria.destroy()
        
        exibir_mensagem(lbl_mensagem_excluir, "Cliente editado com sucesso!", "green")
        caixa_id.delete(0, "end")
        
    except sqlite3.Error as erro:
        print(f"Erro ao atualizar: {erro}")


def abrir_janela_edicao(caixa_id, lbl_mensagem_excluir, area_lista):
    """
    Abre uma janela secundária para editar os dados de um cliente existente.
    """
    id_cliente = caixa_id.get().strip()
    
    # Valida se o ID digitado é número
    if not id_cliente.isdigit():
        exibir_mensagem(lbl_mensagem_excluir, "Digite um ID numérico válido!", "red")
        return
    
    # Busca os dados atuais do cliente para preencher as caixas de texto
    dados_antigos = buscar_cliente_por_id(id_cliente)

    # Se a busca retornou None, o ID não existe
    if not dados_antigos:
        exibir_mensagem(lbl_mensagem_excluir, "ID não encontrado!", "red")
        return

    # Cria uma nova janela que fica "por cima" da principal (Toplevel)
    janela_edicao = ctk.CTkToplevel(janela)
    janela_edicao.geometry("350x250")
    janela_edicao.title("Editar Cliente")
    # Mantém a janela secundária vinculada e na frente da janela principal
    janela_edicao.transient(janela) 

    # Desempacota a tupla retornada do banco em duas variáveis
    nome_antigo, email_antigo = dados_antigos

    # Cria a caixa para o novo nome e insere o nome antigo nela
    cx_novo_nome = ctk.CTkEntry(janela_edicao, width=250)
    cx_novo_nome.pack(pady=(20, 10))
    cx_novo_nome.insert(0, nome_antigo)

    # Cria a caixa para o novo e-mail e insere o e-mail antigo nela
    cx_novo_email = ctk.CTkEntry(janela_edicao, width=250)
    cx_novo_email.pack(pady=10)
    cx_novo_email.insert(0, email_antigo)

    # Botão para salvar as edições
    btn_salvar_edicao = ctk.CTkButton(
        janela_edicao,
        text="Salvar Alteração",
        # Usamos lambda para poder passar parâmetros para a função no momento do clique
        command=lambda: salvar_alteracoes(
            id_cliente, cx_novo_nome.get(), cx_novo_email.get(), 
            janela_edicao, area_lista, lbl_mensagem_excluir, caixa_id
        )
    )
    btn_salvar_edicao.pack(pady=10)

    # Foca na nova janela e bloqueia interações com a principal até essa fechar
    janela_edicao.focus()
    janela_edicao.grab_set() 


# ==========================================
# --- Inicialização da Interface Principal ---
# ==========================================

def iniciar_aplicativo():
    """
    Cria e configura a janela principal e todos os seus elementos visuais.
    """
    global janela # Informa ao Python que 'janela' será usada em todo o código (escopo global)
    
    # Instancia a janela principal
    janela = ctk.CTk()
    janela.geometry("800x650") # Define a largura x altura
    janela.title("Cadastro de Clientes") # Define o título da janela

    # --- Criação dos Elementos (Widgets) ---

    # Rótulo de título
    lbl_titulo = ctk.CTkLabel(janela, text="NOVO CLIENTE", font=("Arial", 18, "bold"))
    lbl_titulo.pack(pady=20) # pack() adiciona o elemento na tela, pady dá uma margem vertical

    # Caixa de texto para o nome
    caixa_nome = ctk.CTkEntry(janela, placeholder_text="Nome", width=300)
    caixa_nome.pack(pady=5)

    # Caixa de texto para o e-mail
    caixa_email = ctk.CTkEntry(janela, placeholder_text="E-mail", width=300)
    caixa_email.pack(pady=5)

    # Label invisível para mostrar mensagens de erro ou sucesso ao salvar
    lbl_mensagem = ctk.CTkLabel(janela, text="")
    lbl_mensagem.pack()

    # Caixa de texto grande onde a lista de clientes será exibida
    area_lista = ctk.CTkTextbox(janela, width=450, height=200)
    area_lista.pack(pady=10)

    # Botão que chama a função de salvar. 
    # O lambda permite passar os elementos da tela como parâmetros.
    btn_salvar = ctk.CTkButton(
        janela, text="Salvar", 
        command=lambda: salvar_dados(caixa_nome, caixa_email, lbl_mensagem, area_lista)
    )
    btn_salvar.pack(pady=15)

    # Caixa de entrada para digitar o ID que será excluído ou editado
    caixa_id = ctk.CTkEntry(janela, placeholder_text="ID p/ Excluir ou Editar")
    caixa_id.pack(pady=10)

    # Label invisível para mostrar mensagens referentes a exclusão/edição
    lbl_mensagem_excluir = ctk.CTkLabel(janela, text="")
    lbl_mensagem_excluir.pack(pady=5)

    # Um 'Frame' atua como uma caixa invisível para agrupar botões lado a lado
    frame_botoes = ctk.CTkFrame(janela, fg_color="transparent")
    frame_botoes.pack(pady=5)

    # Botão de excluir dentro do frame (alinhado à esquerda)
    btn_excluir = ctk.CTkButton(
        frame_botoes, text="Excluir", fg_color="red", hover_color="darkred", 
        command=lambda: excluir_cliente(caixa_id, lbl_mensagem_excluir, area_lista)
    )
    btn_excluir.pack(side="left", padx=10)

    # Botão de editar dentro do frame (alinhado à esquerda do botão anterior)
    btn_edicao = ctk.CTkButton(
        frame_botoes, text="Editar", fg_color="orange", hover_color="darkorange", 
        command=lambda: abrir_janela_edicao(caixa_id, lbl_mensagem_excluir, area_lista)
    )
    btn_edicao.pack(side="left", padx=10)

    # --- Carregamento Inicial ---
    # Assim que os elementos são criados, chamamos a função para preencher a lista
    atualizar_lista_visual(area_lista)

    # --- Loop da Interface ---
    # Mantém a janela aberta e o programa rodando aguardando ações do usuário
    janela.mainloop()


# ==========================================
# --- Ponto de Partida ---
# ==========================================

# Se este arquivo estiver sendo executado diretamente (e não importado por outro), 
# ele chama a função iniciar_aplicativo()
if __name__ == "__main__":
    iniciar_aplicativo()