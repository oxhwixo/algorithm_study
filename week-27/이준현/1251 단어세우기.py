import sys

input = sys.stdin.readline

word = input().rstrip()
arr = []
for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        first = word[:i]
        second = word[i:j]
        last = word[j:]
        arr.append(first[::-1] + second[::-1] + last[::-1])
arr.sort()
print(arr[0])
