# Написать класс, который будет описывать сущность компьютер, добавить несколько полей и методов
# задание полей должно происходить через конструктор класса.
# Создать объекты класса и протестировать поля и методы

class VideoCard:
    def __str__(self) -> str:
        return f'видеокарта {self.brand} {self.model} {self.memory}GB {self.interface}\n'

    def __init__(self, brand: str, model: str, memory: int, interface: str):
        self.brand = brand
        self.model = model
        self.memory = memory
        self.interface = interface


class Computer:
    button ='on'
    def __init__(self, video_card: VideoCard, processor, cooling_system, motherboard):
        self.video_card = video_card
        self.processor = processor
        self.cooling_system = cooling_system
        self.motherboard = motherboard
        print(self)

    def update(self):
        print(f'Компьютер {self.video_card} {self.processor} {self.cooling_system} {self.motherboard} обновляется')

    def reinstalls_drivers(self):
        print(
            f'Компьютер {self.video_card} {self.processor} {self.cooling_system} {self.motherboard} переустанавливает драйвера')

    @classmethod
    def turns_on(cls,x: int) -> int:
        return (f'Компьтер включается после нажатия кнопки {cls.button}')

    @staticmethod
    def Mouse_responsiveness_depending_on_click_speed(x: float, l=0.001) -> float:
        s=x+l
        return print((f'скорость отклика мыши с учетом быстроты нажатия пользователя равна {s}'))



video = VideoCard('acer', '3050', 32, 'pci-x')
comp_1 = Computer(video, 'Intel9', 'water', 'Gigabyte')
print(comp_1)
print(id(comp_1))
print(comp_1.video_card, comp_1.processor, comp_1.cooling_system, comp_1.motherboard)
comp_1.update()
comp_1.reinstalls_drivers()
comp_2 = comp_1
comp_2.processor = 'xxxx'
print(comp_1.processor)
print(comp_1.turns_on('on'))
print(comp_1.Mouse_responsiveness_depending_on_click_speed(1))