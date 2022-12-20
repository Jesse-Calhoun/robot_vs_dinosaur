from robot import Robot

class Fleet:
    def __init__(self,name: str, soldiers: list):
        self.name = name
        self.fleet_health = 0
        self.fleet_power = 0
        self.soldiers = soldiers



    def combine_health(self):
        for i in range(len(self.soldiers)):
            self.fleet_health += self.soldiers[i].health
            
    def combine_power(self):
        for i in range(len(self.soldiers)):
            self.fleet_power += (self.soldiers[i].choose_weapon().attack_power)

    def attack(self, herd: list):
        if self.is_alive():
            herd.herd_health -= self.fleet_power
            print(f'''
            The fleet of robots, {self.name}, attack the herd of dinosaurs, called {herd.name} causing {self.fleet_power} points of damage.
            {herd.name} has {herd.herd_health} health remaining.
            ''')
    
    def is_alive(self):
        return self.fleet_health