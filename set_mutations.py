# Enter your code here. Read input from STDIN. Print output to STDOUT
A = int(input())
set_A = set(list(map(int, input().split(" "))))

N = int(input())

for i in range (N):
    command, size = input().split()
    set_B = set(list(map(int, input().split(" "))))
    if (command == "update"):
        set_A.update(set_B)
    if (command == "intersection_update"):
        set_A.intersection_update(set_B)
    if (command == "difference_update"):
        set_A.difference_update(set_B)
    if (command == "symmetric_difference_update"):
        set_A.symmetric_difference_update(set_B)

# print(sum(set_A))
Sum = 0
for i in  set_A:
    Sum += i

print(Sum)
    
    
