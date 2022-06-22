
palindromes = [i for i in range (100, 1001) if i // 100 == i % 10]  # создаем список от 100 до 1000 если первый символ элемента равен последнему

print(palindromes)



# palindromes = [i for i in range(100, 1001) if str(i) == str(i)[::-1]] # другой вариант со строкой

# print(palindromes)
