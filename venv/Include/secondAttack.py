import StrTest
class broke_dagger(StrTest.Dagger):
    def attack(self,enemy):
        if enemy == "rock":
            self.damage = 0
        else:
            return "Attack on " + enemy +". Deal " + str(self.damage) + " damage"
weapon = broke_dagger(10,"+5",10)
print(weapon.attack("hog"))
weapon.attack("rock")
print(weapon.attack("hog"))