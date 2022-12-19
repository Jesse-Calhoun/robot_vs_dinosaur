from weapon import Weapon
class Robot:
   
    def __init__(self, name:str, active_weapon: Weapon):
        self.name = name
        self.health = 100
        self.active_weapon = active_weapon

    def attack(self, dinosaur):
        while self.health and dinosaur.health > 0:
            dinosaur.health -= self.active_weapon.attack_power
            print(f'''
{self.name} attacked {dinosaur.name} with {self.active_weapon.name} causing {self.active_weapon.attack_power} damage!
{dinosaur.name} has {dinosaur.health} health remaining.
        ''')
