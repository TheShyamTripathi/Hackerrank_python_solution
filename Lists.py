List = []
n = int(input())

for i in range (n):
    operation, *integer = input().split()
    digit = list(map(int, integer))
    
    if( operation == "insert"):
        List.insert(digit[0],digit[1])
    if( operation == "print"):
        print(List)  
    if( operation == "remove"):
        List.remove(digit[0])
    if( operation == "append"):
        List.append(digit[0])
    if( operation == "sort"):
        List.sort()
    if(operation == "pop"):
        List.pop()
    if(operation == "reverse"):
        List.reverse()
    digit.clear()
     
