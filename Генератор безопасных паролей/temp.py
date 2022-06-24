digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '#$%&*+-=?@^_'

chars = digits + lowercase_letters + uppercase_letters + punctuation
chars -= digits
print(chars)
