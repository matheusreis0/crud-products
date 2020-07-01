from model.product import Product
from db.product_db import ProductDB

class ProductController:

    def __init__(self):
        self.__product_db = ProductDB()

    def create_product(self):
        print("---- Menu Cadastro ----")

        id = input("Digite o id: ")
        name = input("Digite o nome: ")
        price = input("Digite o preco: ")

        product = Product(id, name, price)
        self.__product_db.insert(product)

        return product

    def update_product(self):
        print("--- Menu Atualizar ----")
        pass

    def read_product(self, product_id):
        print("--- Menu Listar ----")
        data = self.__product_db.get()
        for item in data:
            if item['id'] == product_id:
                print(f"Produto #{item['id']}\nNome: {item['name']}\nPreco: {item['price']}")

    def delete_product(self):
        print("--- Menu Deletar ----")
        pass

