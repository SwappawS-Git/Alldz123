def shout(Func):
    def wrapp(*args, **kwargs):
        return Func(*args, **kwargs).upper()
    return wrapp

@shout
def txt(txt):
    return txt + 'suffix'
print(txt('i'))

def positive_only(func):
    def wrapp(*args, **kwargs):
        check = any(i < 0 for i in args)
        if check: raise ValueError('Знайдене число яке менше 0')
        return func(*args, **kwargs)
    return wrapp
@positive_only
def Num(Val):
    return Val + 2
print(Num(2, -2))