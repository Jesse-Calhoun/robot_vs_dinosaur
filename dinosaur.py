
class Dinosaur:
    def __init__(self, name:str, attack_power:int):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
    
    def attack(self, robot):
        if self.is_alive():
            robot.health -= self.attack_power
            print(f'''
{self.name} attacked {robot.name} causing {robot.active_weapon.attack_power} damage.
{robot.name} has {robot.health} health remaining.
''')

    def is_alive(self):
        return self.health > 0