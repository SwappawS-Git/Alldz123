import random
def Number_99():
    k = 23
    n = int(input())

    PageNumber = n//k
    Index = n%k
    print(f'Номер рядка на сторінці - {Index}')
    print(f'Рядок знаходиться на сторінці - {PageNumber}')

#Number_99()

def Number_177(Num):
    res = [int(i) for i in str(Num)]
    check = sorted(res)
    if res == check:
        return True 
    return False

#print(Number_177(1))

def Number_291(Num):
    res = str(Num)[::-1]
    return int(res)
#print(Number_291(1234))

class CoinBox:
    def __init__(self, c):
        self.capacity = c
        self.Coins=0

    def CanAdd(self, Num):
        return self.Coins+Num <= self.capacity
    def Add(self, Num):
        self.Coins += Num
    def AddCoin(self, Num):
        if self.CanAdd(Num):
            self.Add(Num)
            return True 
        return False
    def Res(self):
        m = int(input('Скільки ви поклали в скарбничку'))
        if not self.AddCoin(m): print('Не зараховано, сумма перебільшую ліміт')
        k = int(input('Скільки ви хочете покласти?'))
        return self.AddCoin(k)

#Box = CoinBox(10)
#print(Box.Res())
class Buffer:
    def __init__(self):
        self.Buf = []
        self.FullBuf = []
    def Scroll(self, radius, lenRadius):
        lenght = random.randint(lenRadius[0], lenRadius[1])
        res = [random.randint(radius[0], radius[1]) for i in range(lenght)]
        self.add(res)
        return res
    
    def add(self, Roll):
        self.Buf += Roll
        self.FullBuf +=Roll

    def PrintSum(self):
        if len(self.Buf) >= 5:
            result = sum(self.Buf[0: 5])
            self.Buf = self.Buf[5: len(self.Buf)]
            print(f'Summa = {result}')
            return 
        print(f'Not Summa = {self.Buf}')

    def Run(self, Move):
        r = random.randint
        reg = {
            'Scroll': lambda: self.Scroll([1, 10], [2, 5]),
            'Sum': lambda: self.PrintSum() 
        }
        for i in Move:
            print()
            print()
            reg[i]()
            print(i)
            print('------------------------------')
            print(self.FullBuf)
            
#B = Buffer()
#B.Run(['Scroll', 'Sum'])
#B.Run(['Scroll', 'Sum'])
#B.Run(['Scroll', 'Sum'])
