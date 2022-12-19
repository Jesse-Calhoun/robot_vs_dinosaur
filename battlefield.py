from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot('Bender')
        self.dinosaur = Dinosaur('Rex', 15)
    
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        

    def display_welcome(self):
        print(f'''
Welcome to the battlefield! 
Only one can survive.
Let the battle begin!
''')

    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)

    def display_winner(self):
        if self.robot.health > 0:
            print(f'''
{self.robot.name} has defeated {self.dinosaur.name}!
{self.robot.name} wins!
''')
        elif self.dinosaur.health > 0:
            print(f'''
{self.dinosaur.name} has defeated {self.robot.name}!
{self.dinosaur.name} wins!
''')