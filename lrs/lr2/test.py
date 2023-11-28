class Tachka():
    def __init__(self, color, horse_power):
        self.color = color
        self.horse_power = horse_power
    def __eq__(self, other):
        return self.color == other.color and self.horse_power == other.horse_power
    

T1 = Tachka("Blue",228)

T2 = Tachka("Blue",228)
print(T1.color, '\n', T2.color)
print(T1==T2)