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
    
def unique_character(s):
    """
    Given a string s, find the first non-repeating character in it and 
    return its index. If it does not exist, return -1.
    """
    seen = {}
    for i in range(len(s)):
        if s[i] not in seen and s[i] not in s[i+1:]:
            return i
        seen[s[i]] = i        
    return -1

def valid_anagram(s, t):
    """
    Given two strings s and t, return true if t is an anagram of s, 
    and false otherwise.
    """
    if len(s) != len(t):
        return False
    
    for c in s:
        if s.count(c) != t.count(c):
            return False
        
    return True

def valid_palindrome(s):
    """
    A phrase is a palindrome if, after converting all uppercase letters 
    into lowercase letters and removing all non-alphanumeric characters, 
    it reads the same forward and backward. Alphanumeric characters 
    include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.
    """
    converted_text = ''.join(c for c in s if c.isalnum()).lower()
    
    if len(converted_text) == 0 or len(converted_text) == 1:
        return True
    
    i = 0
    while i <= len(converted_text)/2:
        if converted_text[i] != converted_text[-1*(i+1)]:            
            return False
        # print(f"char[{i}]={converted_text[i]}, char[{-1*(i+1)}]={converted_text[-1*(i+1)]}")
        i += 1
    return True

def myatoi(s):
    """
    Implement the myAtoi(string s) function, which converts a string to a 32-bit signed 
    integer (similar to C/C++'s atoi function).

    The algorithm for myAtoi(string s) is as follows:

    >>> Read in and ignore any leading whitespace.
    >>> Check if the next character (if not already at the end of 
        the string) is '-' or '+'. Read this character in if it is either. 
        This determines if the final result is negative or positive respectively. Assume the result 
        is positive if neither is present.
    >>> Read in next the characters until the next non-digit character or 
        the end of the input is reached. The rest of the string is ignored.
    >>> Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). 
        If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
    >>> If the integer is out of the 32-bit signed integer range [-2**31, 2**31 - 1], 
        then clamp the integer so that it remains in the range. Specifically, integers 
        less than -2**31 should be clamped to -2**31, and integers greater than 2**31 - 1 should be clamped to 2**31 - 1.
    >>> Return the integer as the final result.

    Note:

    >>> Only the space character ' ' is considered a whitespace character.
    >>> Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

    """
    my_str = s.lstrip()
    sign_char = "+"
    index = 0
    my_int = 0
    
    if len(my_str) == 0:
        return 0
    
    if my_str[0] == "-" or my_str[0] == "+":
        sign_char = my_str[0]
        index = 1
    
    for ch in my_str[index:]:
        if ch.isnumeric() == False:
            break
        my_int = my_int * 10 + int(ch)
    
    if sign_char == "-":
        my_int *= -1
    
    if my_int < -2**31:
        return -2**31
    elif my_int > 2**31 - 1:
        return -2**31 - 1
    else:
        return my_int

x = "abcd"
print(myatoi(x))