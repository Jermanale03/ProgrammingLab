def sum_list(lista):
    risultato = 0
    if lista == []:
        return 0
    for item in lista:
         risultato = risultato+item
    return risultato

my_list = [10,5,8,12]

print( "La sommatoria vale: {}".format(sum_list(my_list)))