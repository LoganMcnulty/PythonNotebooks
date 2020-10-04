class SpecialAttack():
    def __init__(self, attackName, attackDamage):
        self.attackName = attackName
        self.attackDamage = attackDamage
        
    def specialDamage(self):
        if self.attackName == 'Fire Breath':
            self.attackDamage += 5
        elif self.attackName == 'Poison Pool':
            self.attackDamage += 3
        elif self.attackName == 'Ultimate Crush':
            self.attackDamage += 2
        else:
            self.attackDamage += 0
        
    def useSpecial(self):
        self.specialDamage()
        return "The Special Attack, " + self.attackName + ", deals " + str(self.attackDamage) + " damage!"
