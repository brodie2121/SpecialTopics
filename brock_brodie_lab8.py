class Pet:

    __name = ''
    __animal_type = ''
    __age = ''


def __init__(self):

    self.__name = ''
    self.__animal_type = ''
    self.__age = ''


def get_name(self):

    return self.__name


def set_name(self, name):

    self.__name = name


def get_animalType(self):

    return self.__animal_type


def set_animalType(self, animalType):

    self.__animal_type = animalType


def get_age(self):

    return self.__age


def set_age(self, age):

    self.__age = age


obj1 = Pet()

name = input('Please enter the name : ')
obj1.set_name(name)
animalType = input('Please enter animal Type : ')
obj1.set_animalType(animalType)
age = input('Please enter the age of Pet : ')
obj1.set_age(age)
# Printing the result
print('Pet name : ', obj1.get_name(), ' animal Type :',
      obj1.get_animalType(), ' Pet age : ', obj1.get_age())
