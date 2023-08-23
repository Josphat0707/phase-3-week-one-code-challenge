def my_function(a, b, c):
    if a and b>0 and c<0:
        return True
    elif a and c>0 and b<0:
        return True
    elif b and c>0 and a<0:
        return True
    else: return False

print(my_function(14, 3, -4))