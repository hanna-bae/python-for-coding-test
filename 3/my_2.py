import sys
#n, k = sys.stdin.readline().rstrip()
# 이렇게는 두 개 받을 수 없는듯 
n, k = map(int, input().split())
count = 0

while n > 0:
    n -= 1
    if n % k == 0:
        n = n/k 
    count += 1

print(count)