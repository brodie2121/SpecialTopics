class Employee:

    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number


def get_name(self):
    return self.__name


def get_number(self):
    return self.__number


class ProductionWorker(Employee):
    def __init__(self, name, number, shiftNumber, hrlyPayRate):
        Employee.__init__(self, name, number)
        self.__shiftNumber = shiftNumber
        self.__hrlyPayRate = hrlyPayRate
# Mutators


def set_shiftNumber(self, shiftNumber):
    self.__shiftNumber = shiftNumber


def set_hrlyPayRate(self, hrlyPayRate):
    self.__hrlyPayRate = hrlyPayRate


def get_shiftNumber(self):
    return self.__shiftNumber


def get_hrlyPayRate(self):
    return self.__hrlyPayRate


qempName = raw_input('Enter Employee Name: ')
empNumber = raw_input('Enter Employee Number: ')
empShift = raw_input('Enter Employee Shift(1-Day, 2-Night): ')
empHrlyRate = raw_input('Enter Employee Hourly rate: ')

prod_Worker = ProductionWorker(empName, empNumber, empShift, empHrlyRate)

print('Employee Name:', prod_Worker.get_name())
print('Employee Number:', prod_Worker.get_number())
print('Employee Shift Numner:', prod_Worker.get_shiftNumber())
print('Employee Hoyrly rate:', prod_Worker.get_hrlyPayRate())
