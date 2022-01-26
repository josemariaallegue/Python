import datetime


class Employee:

    # class variable
    numEmployees = 0
    raiseAmount = 1.04

    # constructor
    def __init__(self, name: str, lastName: str, pay: float) -> None:
        self.name = name
        self.lastName = lastName
        self.pay = pay
        # esta variable de clase conviene que se acceda asi porque no se quiere
        # que una instancia pueda modificar el valor
        Employee.numEmployees += 1

    # getter
    @property
    def email(self):
        return self.name + "." + self.lastName + "@company.com"

    @property
    def fullName(self):
        return self.name + " " + self.lastName

    # setter
    @fullName.setter
    def fullName(self, name: str):
        self.name, self.lastName = name.split(" ")

    # deleter
    @fullName.delete
    def fullName(self):
        self.name = None
        self.lastName = None

    # instance methods
    # para manejar los datos de la instancia de la clase
    def showEmployee(self) -> str:
        data = f"Full name: {self.name} {self.lastName}\n"
        data += f"Salary: {self.pay}\n"
        data += f"Email: {self.email}"
        return data

    def applyRaise(self):
        # esta variable de clase conviene que se acceda asi porque se quiere
        # que una instancia pueda modificar el valor
        self.pay = self.pay * self.raiseAmount

    # class methods
    # para manejar los datos de la clase
    @classmethod
    def setRaiseAmount(cls, amount: float):
        cls.raiseAmount = amount

    # los class methods tambien pueden ser utilizados como contructores secundarios
    @classmethod
    def fromStr(cls, employeeStr: str):
        first, last, pay = employeeStr.split("-")
        return cls(first, last, pay)

    # static methods
    # son metodos que no necesitan manejar informacion ni de la instancia ni de la clase
    @staticmethod
    def isWorkDay(day: datetime.date):
        if(day.weekday() == 5 or day.weekday() == 6):
            return False
        return True

    # special methods
    # son un set de metodos predefinidos que se usan para enriquecer las classes
    # __init__ tambien un special method
    def __repr__(self) -> str:
        return f"Employee('{self.name}','{self.lastName}','{self.pay}')"

    def __str__(self) -> str:
        return self.showEmployee()

    def __add__(self, other):
        if(isinstance(self, other)):
            return self.pay + other.pay

        return NotImplemented


class Manager(Employee):
    raiseAmount = 1.12

    def __init__(self, name: str, lastName: str, pay: float, employees: list = None) -> None:
        super().__init__(name, lastName, pay)
        if(employees is None):
            self.employees = []
        else:
            self.employees = employees

    def showEmployee(self) -> str:
        data = super().showEmployee() + "\n"
        data += f"Employees: {self.employees}"
        return data

    def __len__(self):
        return len(self.employees)

    # otra forma de sobreescribir/armar los special methods
    __str__ = showEmployee


class Developer(Employee):
    raiseAmount = 1.1

    # para sobrecargar las funciones del padre se utiliza super()
    def __init__(self, name: str, lastName: str, pay: float, progLang: str) -> None:
        super().__init__(name, lastName, pay)
        self.progLang = progLang

    def showEmployee(self) -> str:
        data = super().showEmployee() + "\n"
        data += f"Programming language: {self.progLang}"
        return data

    def __str__(self) -> str:
        return self.showEmployee()
