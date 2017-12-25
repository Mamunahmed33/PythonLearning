class EnemyAgain:
    def __init__(self, x):
        self.energy = x

    def getLife(self):
        print(str(self.energy) + " I am swimming")
    def test(self):
        print("A")

Don = EnemyAgain(10)
BigBoss = EnemyAgain(25)

Don.getLife()
BigBoss.getLife()
print(BigBoss.test()) # Returning none after calling the function