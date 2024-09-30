class Priduct:
    
    def __init__(self, name, weight, category):
    self.name = name
    self.weighlt = weight
    self.category = category

    def __str__(self):
        return f'{self.name}, {self.weighlt}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        open(self.__file_name, r)
        file = self.__file_name.read()
        close(self.__file_name)
        return self.__str__(file)

    def add(self, *products):
        open(self.__file_name, w)
        file = self.__file_name.read()
        
        close(self.__file_name)

