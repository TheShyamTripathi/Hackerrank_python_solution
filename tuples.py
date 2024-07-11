# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
digits = input().strip().split(" ")
# print(digits)
digitst = tuple(map(int, digits))
# print(digitst)
print(hash(digitst))
