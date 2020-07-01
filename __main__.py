def menu_inicial():
    print(""
        "--- CRUD de produtos ---\n"
        "1 - Cadastrar Produto\n"
        "2 - Atualizar Produto\n"
        "3 - Listar Produto\n"
        "4 - Deletar Produto\n"
        "")

menu_inicial()
try:
    opcao = int(input("Escolha uma opcao"))
except ValueError:
    print("Opcao Invalida!")
