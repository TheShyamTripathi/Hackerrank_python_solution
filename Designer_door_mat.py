N, M = map(int, input().split())

# Top part of the mat
for i in range(1, N, 2):
    pattern = '.|.' * i
    print(pattern.center(M, '-'))

# Middle line
print('WELCOME'.center(M, '-'))

# Bottom part of the mat (mirror of the top part)
for i in range(N-2, -1, -2):
    pattern = '.|.' * i
    print(pattern.center(M, '-'))
