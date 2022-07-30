

class Tank:
    def __init__(self, name, dmg, hp):
        self.name = name
        self.dmg = dmg
        self.hp = hp

    def shoot(self):
        return '발사!'




duke_t = Tank('duke', 300, 3000)
cannon_t = Tank('cannon', 800, 1700)