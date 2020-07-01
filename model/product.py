class Product:

    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price

    def serialize(self):
        return {
            'id': int(self.__id),
            'name': self.__name,
            'price': float(self.__price)
        }

