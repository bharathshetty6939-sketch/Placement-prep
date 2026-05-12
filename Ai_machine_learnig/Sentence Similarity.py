def get_similarity(sent1, sent2):
    words1 = set(sent1.lower().split())
    words2 = set(sent2.lower().split())
    common_words = words1.intersection(words2)
    all_unique_words = words1.union(words2)
    if not all_unique_words:
        return 0
    return len(common_words) / len(all_unique_words)
sentence_a = "The cat is on the mat"
sentence_b = "The dog is on the mat"
similarity = get_similarity(sentence_a, sentence_b)
print(f"Similarity Score: {similarity:.2f}") 
