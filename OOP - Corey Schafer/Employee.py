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
        self.email = name + "." + lastName + "@company.com"
        # esta variable de clase conviene que se acceda asi porque no se quiere
        # que una instancia pueda modificar el valor
        Employee.numEmployees += 1

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


def main():
    employee1 = Employee("Jose", "Allegue", 2000)
    print(employee1.showEmployee())
    print(Employee.numEmployees)


if __name__ == "__main__":
    main()
