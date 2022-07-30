import random

class Tank:
    def __init__(self, name, dmg, hp):
        self.name = name
        self.dmg = dmg
        self.hp = hp

    def shoot(self):
        return '발사!'


duke_t = Tank('duke', 450, 2500)
cannon_t = Tank('cannon', 800, 1700)
comp_t = Tank('comp', 700, 3000)


duke_t.hp -= 500
print(duke_t.hp)

    


