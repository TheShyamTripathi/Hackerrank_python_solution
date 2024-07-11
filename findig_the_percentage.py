if __name__ == '__main__':
    n = int(input())
    student_marks= {}
    for i in range(n):
        name , *line = input().split()
        scores = list(map(float,line))
        student_marks[name] = scores
    query_name = input()
    
    scores = student_marks[query_name]
    total = sum(scores)
    avg = total/len(scores)
    
    print(f"{avg:.2f}")
    
