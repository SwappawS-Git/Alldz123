class CandyStash:
    def __init__(self, count):
        self.validate_amount(count)
        self.__candys = count
        self.MaxCapacity = 50
    @staticmethod
    def validate_amount(value):
        if type(value) != int and value < 0:
            raise ValueError
        
    @classmethod 
    def full_stash(cls):
        cls.candys = 50
        cls.MaxCapacity = 50
    @property 
    def candys(self):
        return self.__candys
    @candys.setter
    def candy(self, val):
        
        if val > self.MaxCapacity:
            self.__candys = self.MaxCapacity
            return
        if val < 0:
            self.__candys = 0
            return
        self.__candys = val
 
    
    def __str__(self):
        
        return f"CandyStash ({self.__candys}/{self.MaxCapacity})"
        
    def __add__(self, val):
        Result = self.__candys+val
        if Result > self.MaxCapacity:
            self.__candys = self.MaxCapacity
            return self.__candys
        if Result < 0:
            self.__candys = 0
            return self.__candys
        self.__candys = Result
        return self.__candys
        # self.candy = self.__candys+val 
        # це другий вариант він більш 'компактний' але add буде залежити від setter 
        # тому я зробив власний валидатор методу add
        
        
    def __sub__(self, val):
        Result = self.__candys-val
        if Result > self.MaxCapacity:
            self.__candys = self.MaxCapacity
            return self.__candys
        if Result < 0:
            self.__candys = 0
            return self.__candys
        self.__candys = int(Result) # Щоб було без залишку
        return self.__candys
        # Теж саме що я писав у коментари в __add__ другий вариант self.candy = self.__candys-val 
    def __eq__(self, val):
        GreenList = [type(self), int] # по условию як ви писали повинно бути int чи CandyStash
        if type(val) in GreenList:
            return self.__candys == val
        return False
    
CandyStashObj = CandyStash(40)
CandyStashObj2 = CandyStash(45)


print(CandyStashObj + 10)
print(CandyStashObj - 5)
print(CandyStashObj == CandyStashObj2)
