import random
class Rolls:
    def Roll(self, a, b):
        roll = random.randint(a, b)

        return roll
Obj = Rolls()

def Test_Roll_return():
    
    res = Obj.Roll(0, 0)
    assert res == 0

    res = Obj.Roll(3, 3)
    assert res == 3

    res = Obj.Roll(-10, -1)
    assert res < 0

   
Test_Roll_return()
