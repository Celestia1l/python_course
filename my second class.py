#Написать класс, который будет описывать сущность война из игры
#добавить несколько полей и методов, задание полей должно происходить через конструктор класса.
#Создать объекты класса и протестировать его поля и методы
class Warrior:
    def __init__(self, weapons, armor, state):
        self.weapons = weapons
        self.armor = armor
        self.state = state
        print(self)

    def attack(self):
        print((f'Воин {self.armor} {self.weapons} {self.state} атакует оппонента'))
    def retreat(self):
        print((f'Воин {self.armor} {self.weapons} {self.state} отступает с поля битвы'))

samurai_1 = Warrior('катана','пластинчитые доспехи', 'Япония')
print(samurai_1)
print(id(samurai_1))
print(samurai_1.weapons, samurai_1.armor, samurai_1.state)
samurai_1.attack()
samurai_1.retreat()
