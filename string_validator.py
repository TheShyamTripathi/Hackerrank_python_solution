if __name__ == '__main__':
    s = input().strip()
    
    is_alnum = False
    is_alpha = False
    is_digit = False
    is_lower = False
    is_upper = False
    
    for char in s:
        if not is_alnum and char.isalnum():
            is_alnum = True
        if not is_alpha and char.isalpha():
            is_alpha = True
        if not is_digit and char.isdigit():
            is_digit = True
        if not is_lower and char.islower():
            is_lower = True
        if not is_upper and char.isupper():
            is_upper = True
    
    print(is_alnum)
    print(is_alpha)
    print(is_digit)
    print(is_lower)
    print(is_upper)
