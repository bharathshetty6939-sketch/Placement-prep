sentence = "The cat is on the table"
stopwords = ["the", "is", "at", "which", "on"]
words = sentence.lower().split()
filtered_words = [w for w in words if w not in stopwords]
filtered_sentence = " ".join(filtered_words)
print("Original:", sentence)
print("Filtered:", filtered_sentence)