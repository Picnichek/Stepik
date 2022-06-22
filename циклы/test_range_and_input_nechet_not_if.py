m = int(input())
n = int(input())
start = ((m - 1) // 2) * 2 + 1 # example with m = 6, n = -2
                                # ((6-1) // 2) * 2 + 1 = 5 * 2 + 1
for i in range(start, n - 1, -2):
    print(i)