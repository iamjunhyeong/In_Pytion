# NO.11650
import sys
n = int(sys.stdin.readline())
so = []
for i in range(n):
    so.append(list(map(int, sys.stdin.readline().split())))
so.sort(k=lambda x: (x[0], x[1]))
for i in so:
    print(i[0], i[1])
