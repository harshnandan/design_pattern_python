from abc import ABC, abstractmethod


class Beverage(ABC):
    '''
    Abstract beverage class
    '''
    def __init__(self):
        self.description = "Unknown beverage"
    
    def get_description(self):
        return self.description
    
    @abstractmethod
    def cost(self):
        pass

class Espresso(Beverage):
    '''
    Concrete implementation of Beverage - this is the core entity on top of
    which decoration can happen
    '''
    def __init__(self):
        self.description = "Espresso"
    
    def cost(self):
        return 1.99

class HouseBlend(Beverage):
    '''
    Another concrete implementation of Beverage - this is the core entity on top of
    which decoration can happen
    '''
    def __init__(self):
        self.description = "House Blend Coffee"
    
    def cost(self):
        return 0.99

class Condiments(Beverage):
    '''
    Abstract condiment subclass
    We want the condiment concrete class to reimplement get description too
    '''

    @abstractmethod
    def get_description(self):
        return self.description

class Soy(Condiments):
    def __init__(self, obj_beverage):
        self.beverage = obj_beverage
    
    def get_description(self):
        return self.beverage.get_description() + ", Soy"

    def cost(self):
        return self.beverage.cost() + 0.49

class Whip(Condiments):
    def __init__(self, obj_beverage):
        self.beverage = obj_beverage
    
    def get_description(self):
        return self.beverage.get_description() + ", Whip Cream"

    def cost(self):
        return self.beverage.cost() + 0.2

# making some orders
# just an espresso
es = Espresso()
print("The cost of an {} is ${:0.2f}".format(es.get_description(), es.cost()))

# just an house blend
hb = HouseBlend()
print("The cost of an {} is ${:0.2f}".format(hb.get_description(), hb.cost()))

# espresson with double soy
es_mo = Soy(Soy(es))
print("The cost of an {} is ${:0.2f}".format(es_mo.get_description(), es_mo.cost()))

# house blend with mocha and whip crea
hb_mo_wc = Whip(Soy(hb))
print("The cost of an {} is ${:0.2f}".format(hb_mo_wc.get_description(), hb_mo_wc.cost()))