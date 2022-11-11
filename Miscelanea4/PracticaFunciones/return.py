'''def boring_function():
    print("'Modo aburrimiento' ON.")
    return 123

print("¡Esta lección es interesante!")
boring_function()
print("Esta lección es aburrida...")'''



'''value = None
if value is None:
    print("Lo siento, no contienes ningún valor")'''




'''def strange_function(n):
    if(n % 2 == 0):
        return True

print(strange_function(2))
print(strange_function(1))'''



'''def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s

print(list_sum([5, 4, 3]))'''



'''def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(10))'''




def is_year_leap(year):
    if year%4!=0:#Si el año no es divisible entre 4, no es bisiesto
        return False
    elif year%4==0 and year%100!=0:#Si el año es divisible entre 4 pero no entre 100, es bisiesto
        return True
    elif year%4==0 and year%100==0 and year%400!=0:#Si el año es divisible entre 4 y 100 pero no entre 400, no es bisiesto
        return False 
    elif year%4==0 and year%100==0 and year%400==0:#Si el año es divisible entre 4, 100 y 400, es bisiesto
        return True

print(is_year_leap(1900))



