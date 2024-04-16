class ElectronicTalon:
    def __init__(self, number):
        self.number = number
        self.status = "Выдан"

    def use_talon(self):
        if self.status == "Выдан":
            print(f"Талон {self.number} использован.")
            self.status = "Использован"
        else:
            print("Талон уже использован.")

# Создаем электронные талоны
talon1 = ElectronicTalon(1)
talon2 = ElectronicTalon(2)

# Используем талоны
talon1.use_talon()
talon2.use_talon()
talon1.use_talon()
