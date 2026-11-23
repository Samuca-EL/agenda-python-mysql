import conexao
import validacao


def inserir(con, nome, telefone, email):
    cursor = con.cursor()
    query = f"insert into contatos (nome, telefone, email) values ('{nome}', '{telefone}', '{email}')"
    cursor.execute(query)
    con.commit()
    cursor.close()


def consultar(con, query):
    cursor = con.cursor()
    cursor.execute(query)
    resultado = cursor.fetchall()
    cursor.close()
    return resultado


def listar(con):
    return consultar(con, "select id, nome, telefone, email from contatos")


def buscar_por_nome(con, nome):
    return consultar(con, f"select id, nome, telefone, email from contatos where nome like '%{nome}%'")


def mostrar(contatos):
    if len(contatos) == 0:
        print("Nenhum contato encontrado.")
    for contato in contatos:
        print(f"{contato[0]} - {contato[1]} | Tel: {contato[2]} | E-mail: {contato[3]}")


def ler_texto(mensagem, tamanho):
    texto = input(mensagem)
    while validacao.texto_valido(texto, tamanho) == False:
        print(f"Inválido. Não deixe vazio, use até {tamanho} caracteres e não use aspas simples.")
        texto = input(mensagem)
    return texto


def menu():
    print()
    print("===== AGENDA =====")
    print("1 - Cadastrar contato")
    print("2 - Listar contatos")
    print("3 - Buscar por nome")
    print("0 - Sair")
    return input("Escolha uma opção: ")


con = conexao.conectar("agenda")

opcao = ""
while opcao != "0":
    opcao = menu()
    match opcao:
        case "1":
            nome = ler_texto("Nome: ", 50)
            telefone = ler_texto("Telefone: ", 20)
            email = ler_texto("E-mail: ", 70)
            inserir(con, nome, telefone, email)
            print("Contato cadastrado!")
        case "2":
            mostrar(listar(con))
        case "3":
            nome = ler_texto("Nome para buscar: ", 50)
            mostrar(buscar_por_nome(con, nome))
        case "0":
            print("Até logo!")
        case _:
            print("Opção inválida.")

con.close()
