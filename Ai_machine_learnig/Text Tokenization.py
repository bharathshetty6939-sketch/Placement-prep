text=input("Enter the text:")
word_count = 0
sentence_count = 0

for char in text:
    if char == " ":
        word_count += 1
    elif char in [".", "!", "?"]:
        sentence_count += 1
        # Logic: Often a punctuation mark also ends a word
        word_count += 1 

print(f"Words: {word_count}, Sentences: {sentence_count}")