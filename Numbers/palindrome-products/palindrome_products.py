def largest(min_factor, max_factor):
    if(min_factor > max_factor):
        raise ValueError("min must be <= max")
    
    for i in range(max_factor, min_factor, -1):
        for j in range(max_factor, min_factor+1, -1):
            prod = i*j
            if prod in range(1, 10):
                result = (prod, (i,j))
                return result
            if str(i*j) == str(i*j)[::-1]:
                result = (i*j, (i,j))
                return result

print(largest(1, 9))
def smallest(min_factor, max_factor):
    if(min_factor > max_factor):
        raise ValueError("min must be <= max")
    
    for i in range(min_factor, max_factor):
        for j in range(min_factor, max_factor+1):
            if str(i*j) == str(i*j)[::-1]:
                result = (i*j, (i,j))
                return result