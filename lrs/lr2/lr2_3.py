class Machine:
    
    def __init__(self,horse_power,brand, model):
        self.horse_power = horse_power
        self.brand = brand
        self.model = model
    

class Car(Machine):
    def __init__(self, wheels_count,type_of_gearbox,type_of_engine):
        self.wheels_count = wheels_count
        self.type_of_gearbox = type_of_gearbox
        self.type_of_engine = type_of_engine

class Cabriolet(Car):
    def __init__(self, type_of_roof):
        self.type_of_roof = type_of_roof
    def __str__(self):
        return f'Car\nbrand: {self.brand}\nHorse power: {self.horse_power}'
    def __repr__(self):
        return f'{self.__class__.__name__}("{self.type_of_roof}").poehala()'
    def poehala(self):
        print('vzhzvhzvzhvzh')

    def __eq__(self,other):
        return (self.horse_power == other.horse_power and self.brand == other.brand and self.model == other.model)
    
    
    


Convert = Cabriolet("Otkidnaya")
Convert.horse_power = 228
Convert.brand = "Lada"
Convert.model = "Priora"

Convert2 = Cabriolet("Otkidnaya")
Convert2.horse_power = 228
Convert2.brand = "Lada"
Convert2.model = "Priora"
print(Convert2 == Convert)
