months = [
    "Січень",      
    "Лютий",
    "Березень",    
    "Квітень",     
    "Травень",     
    "Червень",     
    "Липень",      
    "Серпень",     
    "Вересень",    
    "Жовтень",
    "Листопад",    
    "Грудень"      
]
nums = [67, 14, 88, 52, 46662, 99, 1, 8, 66, 0, 11, 12] 
res = dict(zip(nums, months))

def Info(Mdict):
    reg = {
        'MaxMinInfo': lambda Md: (f'{Md[max(Md)]} / {max(Md)} ', f'{Mdict[min(Md)]} / {min(Md)} '),      
        'SumInfo': lambda Md: (sum(Md), sum(Md)//len(Md)),
        
           }
    MaxMinInfo = reg['MaxMinInfo'](Mdict)
    SumInfo = reg['SumInfo'](Mdict)
    return f"Сумма всіх опадів - {SumInfo[0]}  Середнемісячне - {SumInfo[1]} / Найбільше Опадів - {MaxMinInfo[0]}, Найменше опадів - {MaxMinInfo[1]}"

print(Info(res))
