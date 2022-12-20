from weapon import Weapon
class Robot:
   
    def __init__(self, name:str):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Excal', 20)

    def attack(self, dinosaur):
        if self.is_alive():
            dinosaur.health -= self.active_weapon.attack_power
            print(f'''
{self.name} attacked {dinosaur.name} with {self.active_weapon.name} causing {self.active_weapon.attack_power} damage!
{dinosaur.name} has {dinosaur.health} health remaining.
        ''')
    
    def is_alive(self):
        return self.health > 0