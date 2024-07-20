n = 5
k = 2
arr = [1,2,3,4,5]
ans = 0
print(n,k,arr) 
for i in range(n-k+1):
    sub_arr = arr[i:i+k]
    sum = 0
    for j in range(1,k+1):
        sum += sub_arr[j-1]*j
    if sum > ans:
        ans = sum
print(ans)