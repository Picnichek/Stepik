# for a in range(1, 151):
#     for b in range(a, 151):
#         for c in range(b, 151):
#             for d in range(c, 151):
#                 for e in range(d, 151):
#                     if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
#                         print(a + b + c + d + e)

for a in range(1, 36):
    for b in range(1, 36):
        for c in range(1, 36):
            for d in range(1, 36):
                if  a ** 3 + b ** 3 == c ** 3 + d ** 3 and a != b and a != c and a != d and b != c and b != d and c != d:
                    print(a ** 3 + b ** 3)

