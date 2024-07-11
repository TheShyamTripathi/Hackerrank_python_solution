# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for i in range (T):
    A = int(input())
    setA = set(list(map(int, input().split())))
    B = int(input())
    setB = set(list(map(int, input().split())))
    if setA.issubset(setB):
        print(True)
    else:
        print(False)
    
