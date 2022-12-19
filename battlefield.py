from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon
class Battlefield:
    def __init__(self, robot: Robot, dinosaur: Dinosaur):
        self.robot = robot
        self.dinosaur = dinosaur
    
    def run_game(self):
        pass

    def display_welcome(self):
        print('Welcome to the battlefield! Let the battle begin!')

    def battle_phase(self):
        pass

    def display_winner(self):
        pass