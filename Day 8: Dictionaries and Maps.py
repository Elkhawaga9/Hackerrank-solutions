t = int(input())
dict1 = {}
for _ in range(t):
    name,phone = map(str,input().split())
    dict1[name]= phone
#print(dict1)
while True:
    try:
        q = input()
        if q in dict1:
            print("{}={}".format(q,dict1[q]))
        else:
            print('Not found')
    except EOFError:
        break



