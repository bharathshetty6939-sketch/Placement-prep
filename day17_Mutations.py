if __name__ == '__main__':
    arr = [2, 3, 6, 6, 5] 
    unique_scores = set(arr)
    sorted_scores = sorted(list(unique_scores))
    runner_up = sorted_scores[-2]
    
    print(f"The original scores were: {arr}")
    print(f"The Runner-Up score is: {runner_up}")