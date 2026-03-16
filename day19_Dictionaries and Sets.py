k=int(input())
rooms=list(map(int,input().split()))
counts={}
for room in rooms:
    if room in counts:
        counts[room]+=1;
    else:
        counts[room]=1;
for room in counts:
    if counts[room]==1:
        print(room)