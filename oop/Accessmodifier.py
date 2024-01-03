# public: accessible from anywhere
# protected: accessible from same class and subclass
# private: accessible from same class only

class Car:
    name = 'audi'
    _color = 'red'
    __model = 2020
    __price=0

    def get_price(self):
        return self.__price
    
    def set_price(self,price):
        self.__price = price

    def get_model(self):
        return self.__model

obj = Car()
obj.set_price(1000)
print(obj.get_price())

    