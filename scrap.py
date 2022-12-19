from robot import Robot
from weapon import Weapon
from dinosaur import Dinosaur

trex= Dinosaur('Rex', 14)
sword = Weapon('Excal', 18)
bender = Robot('Bender', sword)

bender.attack(trex)
trex.attack(bender)