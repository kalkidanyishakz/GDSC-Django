from car import Car


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity=battery_capacity
        self.charge_amount=0
    
    def charge(self, amount):
        if self.charge_amount+amount>=self.battery_capacity:
            self.charge_amount=self.battery_capacity
        else:
            self.charge_amount+=amount
        
    def display_info(self):
        super().display_info()
        print(f'battery capacity: {self.battery_capacity}')
        print(f'charge: {self.charge_amount}')

            
my_car2 = ElectricCar("Toyota", "Corolla", 2022, 200)
my_car2.charge(100)
my_car2.display_info()

