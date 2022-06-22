first, second, third, four = int(input()), int(input()), int(input()), int(input())
if first < second < third < four:
    print(first)
else:
    if second < third < four:
        print(second)
    else:
        if third < four:
            print(third)
        else:
            print(four)
