class Car:
    def __init__(self):
        seats = 5

    def enter_race_mode(self):
        self.seats =  4

    def repair(self):
        self.seats = 0

carrace = Car()
carrace.enter_race_mode()
print(carrace.seats)
carrace.repair()
print(carrace.seats)
