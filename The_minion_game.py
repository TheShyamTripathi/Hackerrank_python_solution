def minion_game(string):
    string = string.upper()
    score_k = 0
    score_s = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    length = len(string)
    
    for i in range(length):
        if string[i] in vowels:
            score_k += length - i
        else:
            score_s += length - i

    if score_s > score_k:
        print(f"Stuart {score_s}")
    elif score_k > score_s:
        print(f"Kevin {score_k}")
    else:
        print("Draw")
            
    

if __name__ == '__main__':
    s = input()
    minion_game(s)