from caesor_art import logo

print(logo)


# def encrypt(original_text, shift_amount):
#     shifted_position = ""
#     for letter in original_text:
#         shifts = alphabet.index(letter) + shift_amount
#         shifts %= len(alphabet)
#         shifted_position += alphabet[shifts]
#     print(shifted_position)
#
#
# def decrypt(original_text, shift_amount):
#     shifted_position = ""
#     for letter in original_text:
#         shifts = alphabet.index(letter) - shift_amount
#         shifts %= len(alphabet)
#         shifted_position += alphabet[shifts]
#     print(shifted_position)
def ceasor(original_text, shift_amount, encode_or_decode):
    shifted_position = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            shifted_position += letter
        else:
            shifts = alphabet.index(letter) + shift_amount
            shifts %= len(alphabet)
            shifted_position += alphabet[shifts]
    print(shifted_position)


continue_or_not = True
while continue_or_not:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    direction = input('Type "encode" to encrypt or "decode" to decrypt : ').lower()
    text = input("Type ur msg : ")
    shift = int(input("Type ur shift : "))
    ceasor(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input('Do you want to restart "yes" or "no" : ').lower()
    if restart == "no":
        continue_or_not = False
        print("Goodbye")


