


def log_args(func):
        
    def wrapp(*args, **kwargs):
        print(f"arguments - {args} | {kwargs}")
        func(*args, **kwargs)
    
    return wrapp
@log_args
def message(message):
    print(message)


message(message="Hi")

#------------------------------------------
def repeat(times):
    def deco(func):
        def wrapp(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
                
        return wrapp
    return deco
@repeat(3)
def message(message):
    print(message)

message('Hi')


#------------------------------------
List = ['cat', 'Geometry', 'null']

for i in List:
    if (lenghtWord := len(i)) > 4:
        print(i, lenghtWord)
        

#------------------------------------


def CountDown(n):
    for i in range(n, 0, -1):

        yield i

for i in CountDown(10):
    print(i)
    if i <= 1:
        print('Start!')

