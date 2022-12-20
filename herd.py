from dinosaur import Dinosaur

class Herd:
    def __init__(self, name: str, herd: list):
        self.name = name
        self.herd_health = 0
        self.herd_power = 0
        self.herd = herd

    def combine_health(self):
        for i in range(len(self.herd)):
            self.herd_health += self.herd[i].health
    
    def combine_power(self):
        for i in range(len(self.herd)):
            self.herd_power += self.herd[i].attack_power
    
    def attack(self, fleet: list):
        if self.is_alive():
            fleet.fleet_health -= self.herd_power
            print(f'''
            The herd of dinosaurs, named {self.name}, attacks the fleet, named {fleet.name} causing {self.herd_power} points of damage.
            {fleet.name} has {fleet.fleet_health} health remaining.
            ''')
    
    def is_alive(self):
        return self.herd_health > 0