# Program to find the ASCII value of the given character

i = 1
while i < 6:
    c = input('Enter Character: ')
    print("The ASCII value of '" + c + "' is", ord(c))
    if (i == 3):
        break
    i += 1
