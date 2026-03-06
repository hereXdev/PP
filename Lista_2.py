# ------------------------------------------- ZADANIE 2.0.1 -------------------------------------------

# class Vehicle:

#     def __init__(self, marka, predkosc_max):
#         self.marka = marka
#         self.predkosc_max = predkosc_max

#     def info(self):
#         return f"Pojazd marki {self.marka}, maksymalna prędkość {self.predkosc_max} km/h"


# class Car(Vehicle):

#     def __init__(self, marka, predkosc_max, liczba_drzwi):
#         super().__init__(marka, predkosc_max)
#         self.liczba_drzwi = liczba_drzwi

#     def info(self):
#         return f"Samochód marki {self.marka}, max prędkość {self.predkosc_max} km/h, drzwi: {self.liczba_drzwi}"


# class Bike(Vehicle):

#     def __init__(self, marka, predkosc_max, typ):
#         super().__init__(marka, predkosc_max)
#         self.typ = typ

#     def info(self):
#         return f"Rower marki {self.marka}, max prędkość {self.predkosc_max} km/h, typ: {self.typ}"


# # tworzenie obiektów

# auto = Car("Toyota", 220, 4)
# rower = Bike("Kross", 60, "górski")

# print(auto.info())
# print(rower.info())










# ------------------------------------------- ZADANIE 2.0.2 -------------------------------------------


# ------------------------------------------- ZADANIE 2.0.2 -------------------------------------------

class Animal:

    def make_sound(self):
        return "Nieznany dźwięk"


class Dog(Animal):

    def make_sound(self):
        return "Hau hau"


class Cat(Animal):

    def make_sound(self):
        return "Miau"


class Cow(Animal):

    def make_sound(self):
        return "Muu"


def animal_sound(animal):

    print(animal.make_sound())


# przykładowe obiekty

dog = Dog()
cat = Cat()
cow = Cow()

animal_sound(dog)
animal_sound(cat)
animal_sound(cow)