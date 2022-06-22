s = input()
c = len(s) // 2 + len(s) % 2
#print(len(s) // 2, len(s) % 2)
print(s[c:]+s[:c])

print( len(s) % 2)


