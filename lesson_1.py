""" ООП - Объектно Ориентированое Програмирование """

# hello_world_geeks_backend = "Geeks" # Змеинный регистр

# HelloWorld = "Geeks" # Верблюжий регистр

# def geeks(num1 : int, num2 : int = 20) -> int:
#     return (num1 * num2)

# print(geeks(20))

# class Car: # Шаблон или чертеж
#     def __init__(self, wheel, motor, body): # __init__ - это конструктор
#         self.wheel = wheel
#         self.motor = motor # self - ссылка на текущий объект
#         self.body = body # атрибут класса
        
#         self.bak = 20
#         self.is_start = False
    
#     def info(self): # функция внутри класса превращается в метод
#         print(f"Колесо - {self.wheel}, Мотор - {self.motor}, Кузов - {self.body} ")
        
#     def start(self):
#         if self.bak > 0:
#             self.is_start = True
#             print(f"Машина заведена")
#         else:
#             print("У машины нет топлива")  ==
            
#     def stop(self):
#         self.is_start = False
#         print("Машина заглушена")
        
#     def drive(self, city):
#         if self.is_start == True:
#             print(f"Машина едет в {city}")
#         else:
#             print("Машина не заведена")
        
# car = Car("R20", "V8", "Sedan") # экземпля́р класса
# car.info() # вызов метода, обращаясь к экземпля́ру
# car.start()
# # car.stop()
# car.drive("Дубай")


name = ("Asko", "Isko", "Sema")
list_exapmle = list(name)
list_exapmle.append("Aslan")
name = tuple(list_exapmle)
print(name)

""" Создать класс (Book).Передать параметры (avtor, book_name, year). Создать метод info. Вызвать переданный аргумент """