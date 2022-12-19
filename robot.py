
class Robot:
   
    def __init__(self, name, active_weapon):
        self.name = name
        self.health = 100
        self.active_weapon = active_weapon.attack_power

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon
        print(dinosaur.health)
