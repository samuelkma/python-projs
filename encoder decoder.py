message = input("Enter a message to encode or decode: ")
codevalue = int(input("Type what key value to shift by: "))
message = message.upper()
output = ""
for letter in message:
    if letter.isupper():
        value = ord(letter) + codevalue
        letter = chr(value)
        if not letter.isupper():
            value -= 21
            letter = chr(value)
    output += letter
print("Output message: ", output)


# to test a letter's ordinal, use ord("letter")
# to find an ordinal's letter, use chr(number)
