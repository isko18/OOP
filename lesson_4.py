""" Полиморфиз """

# num1 = 1
# num2 = 2
# print(num1 + num2)

# string1 = "Hello"
# string2 = "Geeks"

# print(string1 + string2)

# print(len("ООП - программирование"))
# print(len(['python', 'JS', 'PHP', 'Scala', 'Ruby']))
# print(len({'python': 'Django', 'JS': 'React'}))

# class Cat:
#     def __init__(self, name, preferences):
#         self.name = name 
#         self.preferences = preferences
        
#     def info(self):
#         print(f'Я кот. Меня зовут {self.name}. Мне {self.preferences} года')
        
#     def make_sound(self):
#         print("Мяу!")
        
# class Dog:
#     def __init__(self, name, preferences):
#         self.name = name 
#         self.preferences = preferences
        
#     def info(self):
#         print(f'Я собака. Меня зовут {self.name}. Мне {self.preferences} года')
        
#     def make_sound(self):
#         print("Гаф!")
        
# cat = Cat("Васька", 2)
# dog = Dog("Мухтар", 3)

# for animal in (cat, dog):
#     animal.make_sound()
#     animal.info()

        
# class PaymetMethod:
#     def pay(self, amount):
#         pass 
    
# class CreditCard(PaymetMethod):
#     def pay(self, amount):
#         return f'Сумма {amount}, оплачивается по кредитной карте'

# class PayPal(PaymetMethod):
#     def pay(self, amount):
#         return f'Сумма {amount}, оплачивается PayPal'
    
# class BankTransfer(PaymetMethod):
#     def pay(self, amount):
#         return f'Сумма {amount}, оплачивается по банковскому переводу'
    
# payments = [CreditCard(), PayPal(), BankTransfer()]

# for payment in payments:
#     print(payment.pay(100))


# from abc import abstractmethod

class Vehicle:
    def start_engine(self):
        pass 
    
    def stop_engine(self):
        pass 
    
    def drive(self):
        pass 
    
class Car(Vehicle):
    def start_engine(self):
        return 'Двигатель автомобиля заведен'
    
    def stop_engine(self):
        return 'Двигатель автомобиля не заведен'
    
    def drive(self):
        return 'Автомобиль едет' 
    
class Bycycle(Vehicle):
    def start_engine(self):
        return 'У велосипеда нет двигателя'
            
    def stop_engine(self):
        return 'У велосипеда нет двигателя'

    def drive(self):
        return 'Велосипед едет'
    
vehicle = [Car(), Bycycle()]

for vehicles in vehicle:
    print(vehicles.start_engine())
    print(vehicles.stop_engine())
    print(vehicles.drive())
    
    
'''Задание: Система оплаты сотрудников

Описание:
Ваша задача — создать систему для расчета зарплаты сотрудников, которая демонстрирует абстракцию, наследование и полиморфизм. Не используйте модуль abc, используйте только базовые механизмы Python.

Требования:  
Базовый класс Employee:

Создайте класс Employee с методом calculate_salary(), который возвращает нулевую зарплату по умолчанию. Также добавьте метод display_info(), который выводит информацию о сотруднике.
Конструктор класса должен принимать имя сотрудника и его базовую ставку.
Классы-наследники для разных типов сотрудников:

Создайте классы FullTimeEmployee и PartTimeEmployee, которые наследуются от класса Employee.
Для класса FullTimeEmployee метод calculate_salary должен возвращать зарплату как базовую ставку умноженную на фиксированный коэффициент (например, 1.2).
Для класса PartTimeEmployee метод calculate_salary должен возвращать зарплату как базовую ставку умноженную на коэффициент, зависящий от количества отработанных часов (например, базовая ставка умноженная на 0.5 за каждый час).
Использование полиморфизма:

Создайте функцию process_salary(employee), которая принимает объект типа Employee и вызывает его методы calculate_salary и display_info.
Функция должна корректно работать для всех производных классов, демонстрируя полиморфизм.'''

# import time

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def display_info(self):
        print(f"Имя: {self.name}")

    def calculate_salary(self):
        return 0


class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)

    def calculate_salary(self):
        return self.base_salary * 1.2


class PartTimeEmployee(Employee):
    def __init__(self, name, base_salary, hours_worked):
        super().__init__(name, base_salary)
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.base_salary * 0.5 * self.hours_worked


def process_salary(employee):
    employee.display_info()
    salary = employee.calculate_salary()
    print(f"Зарплата: {salary}")


# Пример использования
full_time_employee = FullTimeEmployee("Иван", 50000)
part_time_employee = PartTimeEmployee("Мария", 500, 20)

process_salary(full_time_employee)
process_salary(part_time_employee)
    
