import sys
input = sys.stdin.readline

n = int(input().rstrip())
array = list(map(int, input().rstrip().split()))
v = int(input().rstrip())

print(array.count(v))