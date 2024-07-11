if __name__ == '__main__':
    records = []
    
    # Read number of records
    n = int(input())
    
    # Read each name and score pair into records
    for _ in range(n):
        name = input()
        score = float(input())
        records.append([name, score])
    
    # Extract numeric scores and sort them
    scores = sorted([num for sublist in records for num in sublist if isinstance(num, (int, float))])
    
    # Find the second-largest score
    second_lowest = None
    if len(scores) > 1:
        lowest = scores[0]
        for num in scores:
            if num > lowest:
                second_lowest = num
                break
    
    # Extract names associated with the second-largest score and sort them
    sorted_names = sorted([name for sublist in records if second_lowest in sublist for name in sublist if isinstance(name, str)])
    
    # Print each name in sorted order
    for name in sorted_names:
        print(name)
