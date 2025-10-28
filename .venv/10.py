pin = input()
if 1900 <= int(pin) <= 2050:
    print("ERROR")
elif len(set([i for i in pin])) != len(pin):
    print("ERROR")
elif len(pin) != 4:
    print("ERROR")
else:
    print("OK")