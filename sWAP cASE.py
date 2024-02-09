def swap_case(s):
    w = ""
    for i in s:
        if i.islower():
            w+=i.upper()
        else :
            w+=i.lower()
            
    return w

