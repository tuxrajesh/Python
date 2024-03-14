def reverse(x):
    """
    Given a signed 32-bit integer x, return x with its digits reversed. 
    If reversing x causes the value to go outside the signed 32-bit integer 
    range [-231, 231 - 1], then return 0.Assume the environment does not 
    allow you to store 64-bit integers (signed or unsigned).
    """    
    if x < -2**31 or x > 2**31:
        return 0
    
    if x > 0:
        sign = 1
    else:
        sign = -1
        
    rev = 0
    while abs(x) > 0:
        rev = rev * 10 + abs(x) % 10
        x = int(abs(x)/ 10)
        
    rev = rev * sign
            
    if rev < -2**31 or rev > 2**31:
        return 0
    else:
        return rev

x = -123
print(reverse(x))
    