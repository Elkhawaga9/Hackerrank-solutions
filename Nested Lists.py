l1 = []
min = 100
second_min = 100
for _ in range(int(input())):
    name = input()
    score = float(input())
    if score < min:
        second_min = min
        min = score
    elif min < score < second_min:
        second_min = score

    l1.append([name, score])

#print(second_min)
l1 = sorted(l1)
for i in l1:
    if i[1]==second_min:
        print (i[0])

