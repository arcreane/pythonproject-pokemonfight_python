import pygame
from characters.attack import Attack

class Pokemon:

    def __init__(self, hp, atck, defense, speed, name):
        self.HP = hp
        self.Attack = atck
        self.Defense = defense
        self.Speed = speed
        self.Name = name
        self.listAttack = list()
        # self.Type

    #def update(self, name, attack, defense, hp, speed):

    def health_update(self, surface, position):
        bar_color = (111, 250, 46)
        back_bar_color = (60, 63, 60)

        bar_position = [position[0], position[1], 200, 10]
        back_bar_position = [position[0], position[1], 200, 10]

        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
        pass

class Salamèche(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, 30, 40, 30, 30, 'Salamèche')
        atck1 = Attack('Charge', 30)
        atck2 = Attack('Flammèche', 30)
        self.listAttack.append(atck1)
        self.listAttack.append(atck2)

class Bulbizarre(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, 30, 30, 30, 40, 'Bulbizarre')
        atck1 = Attack('Charge', 30)
        atck2 = Attack('Vol-vie', 30)
        self.listAttack.append(atck1)
        self.listAttack.append(atck2)

class Carapuce(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, 35, 30, 35, 30, 'Carapuce')
        atck1 = Attack('Charge', 30)
        atck2 = Attack('Pistolet à O', 30)
        self.listAttack.append(atck1)
        self.listAttack.append(atck2)

class Rattata(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, 35, 30, 30, 30, 'Rattata')
        atck1 = Attack('Charge', 30)
        atck2 = Attack('Vive-attaque', 30)
        self.listAttack.append(atck1)
        self.listAttack.append(atck2)
