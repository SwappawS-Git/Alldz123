class Character:
    def __init__(self, Name, Max_hp):
        self.Name = Name 
        self.__Hp = 10
        self.MaxHp = Max_hp
    @property
    def Hp(self):
        return self.__Hp

    @Hp.setter
    def Hp(self, val):
        if val > self.MaxHp:
            self.__Hp = self.MaxHp
        elif val < 0:
            self.__Hp = 0
        else:
            self.__Hp = val

    def Take_dmg(self, amout):
        self.Hp -= amout 
   

    def Heal(self, amout):
        self.Hp += amout
    
    def is_alive(self, Hp):
        return Hp > 0
a = Character('Pidoras', 20)
a.Heal(11)
a.Take_dmg(11)
print(a.is_alive(a.Hp))
print(a.Hp)
    