from model.product import Product
from db.product_db import ProductDB

class ProductController:

    def __init__(self):
        self.__product_db = ProductDB()

    def create_product(self, id, name, price):
        product = Product(id, name, price)
        self.__product_db.insert(product)

        return product

    def update_product(self):
        print("--- Menu Atualizar ----")
        pass

    def read_product(self, product_id):
        data = self.__product_db.get_all()
        for item in data["products"]:
            if item['id'] == product_id:
                return item

    def delete_product(self):
        print("--- Menu Deletar ----")
        pass

