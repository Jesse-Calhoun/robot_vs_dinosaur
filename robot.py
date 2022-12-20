from weapon import Weapon
class Robot:
   
    def __init__(self, name:str):
        excalibur = Weapon('Excalibur', 17)
        grass_cutter = Weapon('The Grass-Cutter', 14)
        mjolnir = Weapon('Mjolnir', 25)
        
        self.name = name
        self.health = 100
        self.active_weapon = [excalibur, grass_cutter, mjolnir]

    def attack(self, dinosaur):
        if self.is_alive():
            active_weapon = self.active_weapon[int(input(f'Which weapon would you like {self.name} to use? Tyoe 0 for Excalibur, 1 for The Grass-Cutter, or 2 for Mjolnir: '))]
            dinosaur.health -= active_weapon.attack_power
            print(f'''
{self.name} attacked {dinosaur.name} with {active_weapon.name} causing {active_weapon.attack_power} damage!
{dinosaur.name} has {dinosaur.health} health remaining.
        ''')
    
    def is_alive(self):
        return self.health > 0
    