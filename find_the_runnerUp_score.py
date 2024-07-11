n = int(input())
arr = list(map(int, input().split()))

arr.sort()

second_largest = None
largest = arr[-1]

for i in reversed(arr):
    if i< largest:
        second_largest= i
        break
print(second_largest)
