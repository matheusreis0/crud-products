from model.product import Product

class ProductController:

    def __init__(self):
        super().__init__()

    def create_product(self):
        print("---- Menu Cadastro ----")

        id = input("Digite o id: ")
        name = input("Digite o nome: ")
        price = input("Digite o preco: ")

        product = Product(id, name, price)
        return product
    
    def update_product(self):
        pass

    def read_product(self):
        pass

    def delete_product(self):
        pass
