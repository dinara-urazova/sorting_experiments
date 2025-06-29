def do_operation (a, b, operation):
    return operation (a, b)  
# вызов фунции sum_up, после 5 строки и выхода из ф-ции возврат знач во 2 стр
def sum_up (c, d):
    return c + d
    
print(do_operation (5, 7, sum_up))  #cссылка на ф-ю в кач аргумента без ()



