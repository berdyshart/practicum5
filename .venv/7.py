N, K, M = map(int, input().split())
option1 = abs(M-K)-1
option2 = N - K + M - 1
print(min(option1, option2))