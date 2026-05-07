import collections
word1=input("Enter the first word:").lower()
word2=input("Enter the second word:").lower()
if collections.Counter(word1)==collections.Counter(word2):
    print("This is a anagram")
else:
    print("This is not a anagram")
