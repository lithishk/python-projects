

def encrypt_text():
    while True:
        try:
            text = input("Enter your text without spaces: ")
            if ' ' in text:
                print("Please enter a valid text without spaces!.")
                continue
            break
        except Exception:
            print("Please enter a valid text without spaces!")
            continue

    while True:
        try:
            key = int(input("Enter your positive key: "))
            if key <= 0:
                print("Please enter a positive key!")
                continue
            break

        except ValueError:
            print("Please enter a valid number for the key!")
            continue

    text_ascii_values = []
    text_characters = []
    for i in text:
        text_ascii_values.append(ord(i))
    for j in text_ascii_values:
        j -= key
        text_characters.append(chr(j))

    return ''.join(text_characters)



def decrypt_text():
    while True:
        try:
            text = input("Enter the text to decrypt without spaces: ")
            if " " in text:
                print("Please enter a valid text without spaces!")
                continue
            break
        except Exception:
            print("Please enter a valid text without spaces!")
            continue

    while True:
        try:
            key = int(input("Enter your positive key: "))
            if key <= 0:
                print("Please enter a positive key!")
                continue
            break
        except ValueError:
            print("Please enter a valid number for the key!")
            continue

    text_ascii_values = []
    text_characters = []
    for i in text:
        text_ascii_values.append(ord(i))
    for j in text_ascii_values:
        j += key
        text_characters.append(chr(j))
    return ''.join(text_characters)




if __name__ == '__main__':
    print("Encrypted Text: ", encrypt_text())
    print("Decrypted Text: ", decrypt_text())
