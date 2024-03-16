"""
Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
- как минимум один атрибут должен быть с уровнем доступа private.
 Соответственно, для получания значений этого атрибута нужно использовать методы get и set
"""


class Person:
    country = "Russia"  # атрибут класса

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def hello(self):
        return f"Hello, {self.get_fullname()}"

    def get_fullname(self):
        return f'{self.lname} {self.fname}'


class Programmer(Person):
    abbr = "PG"

    def __init__(self, lname, fname, language, salary):
        super().__init__(fname, lname)
        self.language = language
        self.__salary = salary

    def coding(self):
        return f"*** I'm coding with {self.language} ***"

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary


class Tester(Person):
    abbr = "Ts"

    def __init__(self, fname, lname, framefork, job_title):
        super().__init__(fname, lname)
        self.framefork = framefork
        self._job_title = job_title

    def testing(self):
        return f'I\'m testing with {self.framefork}'


person_1 = Person("Ekaterina", "Gordeeva")
print(person_1.fname)
print(person_1.lname)
print(person_1.__dict__)
print(person_1.get_fullname())
print(person_1.country)
print(person_1.hello())


programmer_1 = Programmer("Andrew", "Egorov", "python", "50000")
print(programmer_1.fname)
print(programmer_1.lname)
print(programmer_1.get_fullname())
print(programmer_1.country)
print(programmer_1.hello())
print(programmer_1.coding())
print(programmer_1.get_salary())
programmer_1.set_salary(10000)
print(programmer_1.get_salary())

tester_1 = Tester("Ivan", "Ivanov", "pytest", "auto tester")
print(tester_1.fname)
print(tester_1.country)
print(tester_1.testing())
