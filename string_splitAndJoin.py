def split_and_join(line):
    words = line.split(" ")
    word = "-". join(words)
    return word

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)