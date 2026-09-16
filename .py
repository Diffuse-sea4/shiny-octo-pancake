letter = input("Letter: ").upper()

if len(letter) == 1 and letter.isalpha():
    if letter in ["A", "E", "I", "O", "U"]:
        print(letter, "is a vowel")
    else:
        print(letter, "is a consonant")
else:
    print("invalid input, please enter a single letter")

# this may look ai generated but i only do stuff like , and then a space like print(letter, "e") tho its easier to do print(letter,"e") i like doing the other way its just like more... yk
# alr