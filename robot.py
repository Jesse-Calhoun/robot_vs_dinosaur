from weapon import Weapon
class Robot:
   
    def __init__(self, name:str):
        excalibur = Weapon('Excalibur', 17)
        grass_cutter = Weapon('The Grass-Cutter', 12)
        mjolnir = Weapon('Mjolnir', 23)
        
        self.name = name
        self.health = 100
        self.active_weapon = [excalibur, grass_cutter, mjolnir]

    def attack(self, dinosaur):
        selected_weapon = self.choose_weapon()
        if self.is_alive():
            dinosaur.health -= selected_weapon.attack_power
            print(f'''
{self.name} attacked {dinosaur.name} with {selected_weapon.name} causing {selected_weapon.attack_power} damage!
{dinosaur.name} has {dinosaur.health} health remaining.
        ''')
    
    def is_alive(self):
        return self.health > 0
    
    def choose_weapon(self):
        return self.active_weapon[int(input(f'Which weapon would you like {self.name} to use? Tyoe 0 for Excalibur, 1 for The Grass-Cutter, or 2 for Mjolnir: '))]