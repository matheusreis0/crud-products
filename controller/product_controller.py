from model.product import Product
from db.product_db import ProductDB

class ProductController:

    def __init__(self):
        self.__product_db = ProductDB()

    def create_product(self, id, name, price):
        product = Product(id, name, price)
        product = product.serialize()
        self.__product_db.insert(product)

        return product

    def update_product(self, product_id, name, price):
        data = self.__product_db.get()
        list_index = 0

        for index, item in enumerate(data):
            if item['id'] == product_id:
                list_index = index

        product = Product(product_id, name, price)
        product = product.serialize()

        self.__product_db.update(list_index, product)
        return product

    def read_product(self, product_id):
        data = self.__product_db.get()
        for item in data:
            if item['id'] == product_id:
                return item

    def delete_product(self, product_id):
        data = self.__product_db.get()
        list_index = 0

        for index, item in enumerate(data):
            if item['id'] == product_id:
                list_index = index

        self.__product_db.delete(list_index)
        return product_id

