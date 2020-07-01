from controller.product_controller import ProductController
from db.product_db import ProductDB

menu_options = [
    "Cadastrar Produto", "Atualizar Produto", "Listar Produto", "Deletar Produto"
]

def menu(menu, options):
    print(f"---- {menu} ----")
    for index, value in enumerate(options):
        print(f"{index} - {value}")
    print("10 - Sair")

def menu_create():
    print("---- Menu Cadastro ----")

    id = input("Digite o id: ")
    name = input("Digite o nome: ")
    price = input("Digite o preco: ")

    product = product_controller.create_product(id, name, price)

def menu_update():
    print("--- Menu Atualizar ----")
    id = -1

    while id < 0:
        try:
            id = int(input("Digite o id do produto: "))
        except ValueError:
            print("Opcao Invalida!")
            continue
        
        product = product_controller.read_product(id)
        if product:
            print(f"Produto #{product['id']}\nNome: {product['name']}\nPreco: {product['price']}")
            name = input("Digite o nome: ")
            price = input("Digite o preco: ")
            product = product_controller.update_product(id, name, price)
            print(f"Produto #{product['id']} atualizado")
        else:
            print("Produto nao encontrado!")

def menu_delete():
    print("--- Menu Deletar ----")
    id = -1

    while id < 0:
        try:
            id = int(input("Digite o id do produto: "))
        except ValueError:
            print("Opcao Invalida!")
            continue
        
        product = product_controller.read_product(id)
        if product:
            print(f"Produto #{product['id']}\nNome: {product['name']}\nPreco: {product['price']}")
            product = product_controller.delete_product(id)
            print(f"Produto #{id} deletado")
        else:
            print("Produto nao encontrado!")

def menu_read():
    print("--- Menu Listar ----")
    id = -1

    while id < 0:
        try:
            id = int(input("Digite o id do produto: "))
        except ValueError:
            print("Opcao Invalida!")
            continue

        product = product_controller.read_product(id)
        if product:
            print(f"Produto #{product['id']}\nNome: {product['name']}\nPreco: {product['price']}")
        else:
            print("Produto nao encontrado!")

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
        product_db = ProductDB()

        if option == 0:
            menu_create()
        elif option == 1:
            menu_update()
        elif option == 2:
            menu_read()
        elif option == 3:
            menu_delete()

