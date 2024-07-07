def caesar_cipher(text, shift, direction):
    result = ""
    
    # Determine the direction of shift: positive for encryption, negative for decryption
    if direction == "decrypt":
        shift = -shift

    # Traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt/Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt/Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        # Keep other characters unchanged
        else:
            result += char

    return result

# Input from user
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))
direction = input("Choose 'encrypt' or 'decrypt': ").lower()

# Perform the Caesar Cipher
result = caesar_cipher(text, shift, direction)
print(f"Result: {result}")

