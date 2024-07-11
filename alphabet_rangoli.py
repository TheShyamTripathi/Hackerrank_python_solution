def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase
    
    # Create the top part of the rangoli
    for i in range(size):
        # Create dashes for padding
        dashes = '-' * (2 * (size - i - 1))
        
        # Create the sequence of characters for the current line
        chars = '-'.join(alphabet[size-j-1] for j in range(i + 1))
        
        # Combine the left part, characters, reversed characters, and right part
        line = dashes + chars + chars[-2::-1] + dashes
        print(line)
    
    # Create the bottom part of the rangoli (mirror of the top part)
    for i in range(size - 1, 0, -1):
        dashes = '-' * (2 * (size - i))
        chars = '-'.join(alphabet[size-j-1] for j in range(i))
        line = dashes + chars + chars[-2::-1] + dashes
        print(line)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)