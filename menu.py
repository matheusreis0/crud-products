from controller.product_controller import ProductController

class Menu:
    def __init__(self):
        self.__menu_options = [
            "Cadastrar Produto", "Atualizar Produto", "Listar Produto", "Deletar Produto",
            "Sair"
        ]
        self.__product_controller = ProductController()

    def menu(self, menu, options):
        print(f"---- {menu} ----")
        for index, value in enumerate(options):
            print(f"{index} - {value}")

    def menu_create(self):
        print("---- Menu Cadastro ----")

        id = input("Digite o id: ")
        name = input("Digite o nome: ")
        price = input("Digite o preco: ")

        product = self.__product_controller.create_product(id, name, price)

    def menu_update(self):
        print("--- Menu Atualizar ----")
        id = -1

        while id < 0:
            try:
                id = int(input("Digite o id do produto: "))
            except ValueError:
                print("Opcao Invalida!")
                continue
            
            product = self.__product_controller.read_product(id)
            if product:
                print(f"Produto #{product['id']}\nNome: {product['name']}\nPreco: {product['price']}")
                name = input("Digite o nome: ")
                price = input("Digite o preco: ")
                product = self.__product_controller.update_product(id, name, price)
                print(f"Produto #{product['id']} atualizado")
            else:
                print("Produto nao encontrado!")

    def menu_delete(self):
        print("--- Menu Deletar ----")
        id = -1

        while id < 0:
            try:
                id = int(input("Digite o id do produto: "))
            except ValueError:
                print("Opcao Invalida!")
                continue
            
            product = self.__product_controller.read_product(id)
            if product:
                print(f"Produto #{product['id']}\nNome: {product['name']}\nPreco: {product['price']}")
                product = self.__product_controller.delete_product(id)
                print(f"Produto #{id} deletado")
            else:
                print("Produto nao encontrado!")

    def menu_read_item(self):
        print("--- Menu Listar ----")
        id = -1

        while id < 0:
            try:
                id = int(input("Digite o id do produto: "))
            except ValueError:
                print("Opcao Invalida!")
                continue

            product = self.__product_controller.read_product(id)
            if product:
                print(f"Produto #{product['id']}\nNome: {product['name']}\nPreco: {product['price']}")
            else:
                print("Produto nao encontrado!")

    def principal_menu(self):
        option = -1

        while option != 4:
            self.menu("Menu initial", self.__menu_options)
            try:
                option = int(input("Escolha uma opcao "))
            except ValueError:
                print("Opcao Invalida!")
                continue

            if option not in range(len(self.__menu_options)) and option != 4:
                print("Opcao Invalida!")
                continue
            else:
                if option == 0:
                    self.menu_create()
                elif option == 1:
                    self.menu_update()
                elif option == 2:
                    self.menu_read_item()
                elif option == 3:
                    self.menu_delete()
                elif option == 4:
                    break
