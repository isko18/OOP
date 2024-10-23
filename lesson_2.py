""" Наследование """

class Game:
    def __init__(self, game_name, graphics, game_year, company):
        self.game_name = game_name
        self.graphics = graphics
        self.game_year = game_year
        self.company = company
        
    def info(self):
        print(f"Game - {self.game_name} - {self.graphics} - {self.game_year} - {self.company} - {self.multiplayer}")
        
game = Game('MobileLegends', 'FULL HD', 2017, 'Tencent')
game.info()

class Roblox(Game):
    def __init__(self, game_name, graphics, game_year, company, multiplayer):
        # super().__init__(game_name, graphics, game_year, company)
        Game.__init__(self, game_name, graphics, game_year, company)
        self.multiplayer = multiplayer
        self.name = 'Iskhak'
        self.gender = 'man'
        self.skin = 'naruto'
        self.hp = '100'
        
    def info(self):
        print(f"Game - {self.game_name} - {self.graphics} - {self.game_year} - {self.company} - {self.multiplayer}")
        
    def info_player(self):
        print(f'Игрок - {self.name} - {self.gender} - {self.skin} - {self.hp}')
        
    def edit_player(self):
        name = input("Введите имя игрока: ")
        gender = input("Введите пол игрока: ")
        skin = input("Введите облик для игрока: ")
        self.name = name
        self.gender = gender
        self.skin = skin
    
# roblox = Roblox("Roblox", "ULTRA", 2006, 'Roblox Corporation', 'ДА')
# roblox.info()
# roblox.edit_player()
# roblox.info_player()

class Strike(Roblox):
    def __init__(self, game_name, graphics, game_year, company, multiplayer):
        super().__init__(game_name, graphics, game_year, company, multiplayer)
        
    def info_player(self):
        return super().info_player()
    
st = Strike("Roblox", "ULTRA", 2006, 'Roblox Corporation', 'ДА')
st.edit_player()
st.info_player()


''''Задание: Симуляция Зоопарка с Конструкторами
Создайте классы, которые будут моделировать разных животных в зоопарке, используя множественное наследование и конструкторы для инициализации объектов.

Базовые классы:

Создайте класс Animal, который будет представлять общее животное. У этого класса должен быть конструктор __init__(), который принимает параметр name для имени животного. Также добавьте методы eat() и sleep(), которые выводят сообщения, например, "{name} ест" и "{name} спит".

Создайте класс Walker, который будет представлять животных, которые могут ходить. У этого класса должен быть метод walk(), который выводит сообщение "{name} ходит".

Создайте класс Swimmer, который будет представлять животных, которые могут плавать. У этого класса должен быть метод swim(), который выводит сообщение "{name} плавает".

Создайте класс Flyer, который будет представлять животных, которые могут летать. У этого класса должен быть метод fly(), который выводит сообщение "{name} летает".

Комбинированные классы:
                                            
Создайте класс Penguin, который наследуется от Animal, Walker, и Swimmer. Реализуйте конструктор, который принимает параметр name и вызывает конструктор класса Animal. Добавьте метод describe(), который выводит сообщение о том, что пингвин может ходить и плавать.

Создайте класс Duck, который наследуется от Animal, Walker, Swimmer, и Flyer. Реализуйте конструктор, который принимает параметр name и вызывает конструктор класса Animal. Добавьте метод describe(), который выводит сообщение о том, что утка может ходить, плавать и летать.

Создайте класс Bat, который наследуется от Animal и Flyer. Реализуйте конструктор, который принимает параметр name и вызывает конструктор класса Animal. Добавьте метод describe(), который выводит сообщение о том, что летучая мышь может летать.

Тестирование:

Создайте экземпляры каждого из созданных вами классов, передавая им имена, и вызовите для них методы describe(), а также методы, относящиеся к их поведению (например, walk(), swim(), fly()).'''

# print(bool('False'))
# # print(bool)

# a = (i for i in range(10))
# print(type(a))


# for i in range(101):
#     print(i, end=" ")

# for i in range(1 , 11):
#     for j in range(1, 11):
#         print(f'{i * j: ^5}', end=" ")
#     print("")