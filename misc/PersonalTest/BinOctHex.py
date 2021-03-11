# Python program to convert decimal into other number systems
i = 1
while i < 6:
    dec = input('Enter Character: ')

    print("The decimal value of", dec, "is:")
    print(bin(dec), "in binary.")
    print(oct(dec), "in octal.")
    print(hex(dec), "in hexadecimal.")
    if (i == 3):
        break
i += 1
