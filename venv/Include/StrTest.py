
class Sword(object):
    """docstring"""

    def __init__(self, lenght, upper, damage):
        """Constructor"""
        self.lenght = lenght
        self.upper = upper
        self.damage = damage

    def attack(self,enemy):

        return "Attack on " + enemy +". Deal " + str(self.damage) + " damage"


class Dagger(Sword):
    def throw(self,enemy):
        return "Throw on " + enemy + ". Deal " + str(self.damage*5) + " damage"

