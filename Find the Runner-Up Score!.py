
n = int(input())
arr = map(int, input().split())
arr = list(arr)
arr.sort(reverse=True)
for i in range(n):
    if arr[i]!=arr[0]:
        print(arr[i])
        break


