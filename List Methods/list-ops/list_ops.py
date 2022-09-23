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
    pass


def length(list):
    pass


def map(function, list):
    pass


def foldl(function, list, initial):
    pass


def foldr(function, list, initial):
    pass


def reverse(list):
    pass

print((concat([[1, 2], [3], [], [4, 5, 6]]), [1, 2, 3, 4, 5, 6]))