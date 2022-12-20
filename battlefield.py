from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
class Battlefield:
    def __init__(self):
        trex = Dinosaur('Rex', 17)
        ptero = Dinosaur('Petrie', 15)
        snork = Dinosaur('Dino', 13)
        dinos = [trex, ptero, snork]
        bender = Robot('Bender') 
        wall_e = Robot('Wall-E')
        t_800 = Robot('Arnold')
        fleet_of_robots = [bender, wall_e, t_800]
        self.herd = Herd('Jurassic Pride', dinos)
        self.fleet = Fleet('The Tin Men', fleet_of_robots)
        # self.robot = Robot('Bender')
        # self.dinosaur = Dinosaur('Rex', 15)
    
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
        self.fleet.combine_health()
        self.herd.combine_health()
        self.herd.combine_power()
        while self.fleet.is_alive() and self.herd.is_alive():
            self.fleet.fleet_power = 0
            self.fleet.combine_power()
            self.fleet.attack(self.herd)
            self.herd.attack(self.fleet)

    # def battle_phase(self):
    #     while self.robot.is_alive() and self.dinosaur.is_alive():
    #         self.robot.attack(self.dinosaur)
    #         self.dinosaur.attack(self.robot)

    def display_winner(self):
        if self.fleet.fleet_health > 0:
            print(f'''
{self.fleet.name} has defeated {self.herd.name}!
{self.fleet.name} wins!
''')
        elif self.herd.herd_health > 0:
            print(f'''
{self.herd.name} has defeated {self.fleet.name}!
{self.herd.name} wins!
''')
#     def display_winner(self):
#         if self.robot.health > 0:
#             print(f'''
# {self.robot.name} has defeated {self.dinosaur.name}!
# {self.robot.name} wins!
# ''')
#         elif self.dinosaur.health > 0:
#             print(f'''
# {self.dinosaur.name} has defeated {self.robot.name}!
# {self.dinosaur.name} wins!
# ''')