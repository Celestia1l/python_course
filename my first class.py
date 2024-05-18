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


class Processor:
    def __str__(self) -> str:
        return f'процессор {self.brand} {self.model} {self.cores}\n'

    def __init__(self, brand: str, model: str, cores: int):
        self.brand = brand
        self.model = model
        self.cores = cores


class Cooling_system:
    def __str__(self):
        return f'система охлаждения {self.brand} {self.type} {self.noise}\n'

    def __init__(self, brand: str, noise: str, type: str):
        self.brand = brand
        self.noise = noise
        self.type = type


class Motherboard:
    def __srt__(self):
        return f'Материнская плата {self.brand} {self.model} {self.socket} {self.chipset}\n'

    def __init__(self, brand, model, socket, chipset):
        self.brand=brand
        self.model=model
        self.socket=socket
        self.chipset=chipset


class Computer:
    button = 'on'

    def __init__(self, video_card: VideoCard, processor: Processor, cooling_system: Cooling_system, motherboard):
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
    def turns_on(cls, x: int) -> int:
        return (f'Компьтер включается после нажатия кнопки {cls.button}')

    @staticmethod
    def Mouse_responsiveness_depending_on_click_speed(x: float, l=0.001) -> float:
        s = x + l
        return print((f'скорость отклика мыши с учетом быстроты нажатия пользователя равна {s}'))


video = VideoCard('acer', '3050', 32, 'pci-x')
comp_1 = Computer(video, 'Intel9', 'water', 'Gigabyte')
print(comp_1)
print(id(comp_1))
print(comp_1.video_card, comp_1.processor, comp_1.cooling_system, comp_1.motherboard)
comp_1.update()
comp_1.reinstalls_drivers()
print(comp_1.turns_on('on'))
print(comp_1.Mouse_responsiveness_depending_on_click_speed(1))
