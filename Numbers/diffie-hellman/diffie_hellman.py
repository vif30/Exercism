import random
def private_key(p):
    if(p < 1):
         raise ValueError("Only positive integers are allowed")
    else:
        return random.randint(1, p)

def public_key(p, g, private):
    A = pow(g, private) % p
    return A

def secret(p, public, private):
    s = pow(public, private) % p
    return s