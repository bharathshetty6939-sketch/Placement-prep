score=[85,90,78]
print("Initial list is",score)
score_add=[98,54,67]
score.extend(score_add)
print("After extending the list",score)
removed_item=score.pop()
print(f"removed item {removed_item} list now",score)
inserted_item=score.insert(1,15)
print(f"after inserting at index 1 now list is",score)
print("occurance of 90 is ",score.count(90))
pos=score.index(90)
print("position of 90 is",pos)