import json

class ProductDB:
    def __init__(self):
        self.__data = {"products": []}

    def get(self):
        with open('products.txt') as file:
            data = json.load(file)

        return data["products"]

    def insert_in_file(self):
        with open('products.txt', 'w+') as file:
            json.dump(self.__data, file, indent=4)

    def insert(self, product):
        self.__data = self.get_all()
        self.__data["products"].append(product)

        self.insert_in_file()

    def update(self, list_id, product):
        self.__data = self.get_all()
        self.__data["products"][list_id] = product
        
        self.insert_in_file()
    
    def delete(self, list_id):
        self.__data = self.get_all()
        self.__data["products"].pop(list_id)

        self.insert_in_file()

