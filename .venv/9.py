s = list(map(int, input().split()))
s_final = []
for _ in range(3):
    s_final.append(max(s))
    s.remove(max(s))
print(*s_final)