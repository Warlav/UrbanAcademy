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
        if Product().name not in file:
            self.__file_name.write(f'{Product().__str__()}\n)
        else:
            print(f'Продукт {Product().name} уже есть в магазине'
        close(self.__file_name)


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
