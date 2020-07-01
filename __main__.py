menu_options = [
    "Cadastrar Produto", "Atualizar Produto", "Listar Produto", "Deletar Produto"
]

def menu(menu, options):
    print(f"---- {menu} ----")
    for index, value in enumerate(options):
        print(f"{index} - {value}")
    print("10 - Sair")

option = 0
while option != 10:
    menu("Menu initial", menu_options)
    try:
        option = int(input("Escolha uma opcao "))
    except ValueError:
        print("Opcao Invalida!")
        continue
    
    if option not in range(len(menu_options)) and option != 10:
        print("Opcao Invalida!")
        continue
    else:
        if option == 0:
            print("menu cadastro")
        elif option == 1:
            print("menu atualizar")
        elif option == 2:
            print("menu listar")
        elif option == 3:
            print("menu deletar")
