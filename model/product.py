class Product:

    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price

    def serialize(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'price': self.__price
        }

