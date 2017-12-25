class Enemy:
    life = 3

    def attact(self):
        print("ouch!")
        self.life -= 1
    def checkLife(self):
        print(str(self.life) + " Life left")

enemy1= Enemy()
enemy2= Enemy()

enemy1.attact()
enemy1.attact()
enemy1.checkLife()

enemy2.checkLife()