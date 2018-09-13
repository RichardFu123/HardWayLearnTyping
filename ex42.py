## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self,name):
        ## Dog has-a function __init__ that takes self and name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self,name):
        ## Cat has-a function __init__ that takes self and name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self,name):
        ## person has-a function __init__ that takes self and name
        self.name = name

        ##Persion has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self,name,salary):
        ## Employee is-a Person which has-a attribute salary
        super(Employee,self).__init__(name)
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## a Dog named Rover
rover = Dog('Rover')

## a Cat named Satan
satan = Cat('Satan')

## a Person named Mary
mary = Person("Mary")

## Mary has-a pet, which is Satan
mary.pet = satan

## Frank is-a Employee with 120000 salary
frank = Employee("Frank",120000)

## Frank has-a pet, which is Rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
