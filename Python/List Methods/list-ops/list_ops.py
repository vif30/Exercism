def append(list1, list2):
    for i in list2:
        list1.append(i)
    return(list1)


def concat(lists):
    lista = []
    for i in lists:
        for j in i:
            if j not in lista:
                lista.append(j)
    return lista


def filter(function, list):
    lista = []
    for i in list:
        if function(i):
            lista.append(i)
    return lista


def length(list):
    cant = len(list)
    return cant


def map(function, list):
    lista = []
    for i in list:
        lista.append(function(i))
    return lista


def foldl(function, list, initial):
    pass


def foldr(function, list, initial):
    pass


def reverse(list):
    pass

print(filter(lambda x: x % 2 == 1, []))