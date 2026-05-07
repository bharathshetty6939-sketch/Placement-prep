positive_words = ["good", "great", "happy", "excellent", "fast"]
negative_words = ["bad", "slow", "sad", "error", "fail"]
text=input("Enter a sentence to analyze:").lower()
score=0
for word in text.split():

    if word in positive_words:
        score+=1
    elif word in negative_words:
        score-=1
print("Score of sentence is",score)
if score<0:
    print("Negative sentence")
elif score>0:
    print("Positive sentence")
else:
    print("Neutral sentence")

