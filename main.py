from dictionary import MORSE_DICT


def to_morse(text):
    morse = ""
    try:
        for letter in text:
            if letter == " ":
                morse += " "
            else:
                morse += MORSE_DICT[letter.lower()] + " "
        return morse[:-1]

    except KeyError:
        print("Sorry, you entered symbols that can not be converted to morse code!\nPlease try again!")
        return None


print(45 * "*")
print("THIS APP CONVERTS EVERY TEXT TO MORSE CODE!")
print(45 * "*")

space_symbol = input("Do you want to use | for space? (y/n): ")

while True:
    input_text = input("\nPlease enter your text: ")
    morse_text = to_morse(input_text)
    if morse_text:
        if space_symbol == "y":
            morse_text = morse_text.replace("  ", "|")
        print(f"\nThe morse code for your text '{input_text}' is: \n{morse_text}\n")

    another = input("Wanna convert another text? (y/n): ")
    if another.lower() == "n":
        print("\nThank you for using this converter. Bye!")
        print("*" * 45)
        break
