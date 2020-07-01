import json

class ProductDB:
    def __init__(self):
        self.__data = {"products": []}

    def get(self):
        with open('products.txt') as file:
            data = json.load(file)

        return data["products"]

    def get_all(self):
        with open('products.txt') as file:
            data = json.load(file)

        return data

    def insert(self, product):
        self.__data = self.get_all()
        self.__data["products"].append(product.serialize())

        with open('products.txt', 'w+') as file:
            json.dump(self.__data, file, indent=4)

    def insert_list(self, products):
        with open('products.txt', 'w') as file:
            for item in products:
                self.__data["products"].append(item.serialize())
            print(self.__data)
            json.dump(self.__data, file, indent=4)

