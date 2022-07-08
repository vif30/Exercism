"""System module."""
def response(hey_bob):
    """Method Docs."""
    hey_bob = hey_bob.strip()
    if(hey_bob.endswith("?") and not hey_bob.isupper()):
       return "Sure."
    if(hey_bob.isupper() and not hey_bob.endswith("?")):
       return "Whoa, chill out!"
    if(hey_bob.endswith("?") and hey_bob.isupper()):
       return "Calm down, I know what I'm doing!"
    if(not hey_bob):
       return "Fine. Be that way!"
    else:
        return "Whatever."   