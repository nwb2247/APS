A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

sec = 0
while A < B :
    if A < 0 :
        sec += C
        A += 1
    elif A == 0 :
        sec += D
        sec += E
        A += 1
    else :
        sec += E
        A += 1

print(sec)