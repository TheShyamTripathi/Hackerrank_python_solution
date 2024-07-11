# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eng_sub = list(map(int, input().split()))
b= int(input())
frn_sub = list(map(int, input().split()))

eng_set = {}
frn_set = {}

eng_set = set(eng_sub)
frn_set = set(frn_sub)

number_list = eng_set.union(frn_set)
print(len(number_list))
