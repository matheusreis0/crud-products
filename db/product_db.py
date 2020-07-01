import json

class ProductDB:
    def __init__(self):
        self.__data = {"products": []}

    def insert(self, product):
        with open('products.txt', 'w') as file:
            for item in products:
                self.__data["products"].append(item.serialize())
            print(self.__data)
            json.dump(self.__data, file, indent=4)

    def insert_list(self, products):
        with open('products.txt', 'w') as file:
            for item in products:
                self.__data["products"].append(item.serialize())
            print(self.__data)
            json.dump(self.__data, file, indent=4)

    def get(self):
        with open('products.txt') as file:
            self.__data = json.load(file)
            print(self.__data)

