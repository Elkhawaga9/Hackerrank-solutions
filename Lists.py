N = int(input())
l1=[]
for _ in range(N):
    arr = list(map(str, input().split()))
    arr = list(arr)
    if arr[0]=='insert':
        l1.insert(int(arr[1]), int(arr[2]))
    elif arr[0]=='print':
        print(l1)
    elif arr[0]=='remove':
        l1.remove(int(arr[1]))
    elif arr[0]=='pop':
        l1.pop()
    elif arr[0]=='sort':
        l1.sort()
    elif arr[0]=='append':
        l1.append(int(arr[1]))
    elif arr[0]=='reverse':
        l1.reverse()



