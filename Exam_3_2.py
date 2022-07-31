#2. Напишите функцию, которая возвращает True, если введенный текст 
#читается одинаково слева-направо и справа-налево. Иначе – False.
def palindrome(data):
    data = input('Ввод: ')
    if data == data[::-1]:
        print(True)
    else:
        print(False)
palindrome(bool)
