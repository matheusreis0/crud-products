from controller.product_controller import ProductController

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
        product_controller = ProductController()
        if option == 0:
            product_controller.create_product()
        elif option == 1:
            product_controller.update_product()
        elif option == 2:
            product_controller.read_product()
        elif option == 3:
            product_controller.delete_product()
