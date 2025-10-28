n = int(input())
if 11<=n<=19:
    print(f"{n} попугаев")
elif n % 10 in [0, 5, 6, 7, 8, 9]:
    print(f"{n} попугаев")
elif n % 10 in [2, 3, 4]:
    print(f"{n} попугая")
else:
    print(f"{n} попугай")