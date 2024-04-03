print('1)==================>')
txt = "0123456789"
print(txt[1:9:3])
print(txt[::2])

print('\n2)==================>')
txt = "1a2b3c4d5e6f"
print(f"Чётный индекс: {txt[0::2]}")
print(f"Нечётный индекс: {txt[1::2]}")
print(f"конкатенация: {txt[0::2] + txt[1::2]}")

print('\n3)==================>')
txt = "0123456789"
print(txt[2:5:-1], '1)')
print(txt[5:2:-1])
print(txt[-1:2:-1])
print(txt[-1::-1])

print('\n4)==================>')
txt = "поход"
print(True if txt == txt[::-1] else False)
