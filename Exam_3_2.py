def palindrome(data):
    data = input('Ввод: ')
    if data == data[::-1]:
        print(True)
    else:
        print(False)
palindrome(bool)