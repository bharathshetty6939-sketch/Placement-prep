if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # One-liner to remove duplicates and sort
    unique_scores = sorted(list(set(arr))) 
    
    print(unique_scores[-2])