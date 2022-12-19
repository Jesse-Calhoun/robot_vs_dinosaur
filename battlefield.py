from robot import Robot
from weapon import Weapon
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self, robot: Robot, dinosaur: Dinosaur):
        self.robot = robot
        self.dinosaur = dinosaur
    
    def 