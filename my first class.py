class Computer:
    def __init__(self, video_card, processor, cooling_system, motherboard):
        self.video_card = video_card
        self.processor = processor
        self.cooling_system = cooling_system
        self.motherboard = motherboard
        print(self)

    def update(self):
        print(f'Компьютер {self.video_card} {self.processor} {self.cooling_system} {self.motherboard} обновляется')

    def reinstalls_drivers(self):
        print(f'Компьютер {self.video_card} {self.processor} {self.cooling_system} {self.motherboard} переустанавливает драйвера')
comp_1 = Computer('RTX4090', 'Intel9', 'water', 'Gigabyte')
print(comp_1)
print(id(comp_1))
print(comp_1.video_card, comp_1.processor, comp_1.cooling_system, comp_1.motherboard)
comp_1.update()
comp_1.reinstalls_drivers()
