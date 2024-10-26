# Caesar Cipher encryption and decryption functions
def encrypt(text, shift=3):
    result = ""
    # Traverse the text
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

def decrypt(text, shift=3):
    result = ""
    # Traverse the text
    for char in text:
        # Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

# Main loop with menu options
while True:
    print("\nChoose an option:")
    print("1. Encrypt a word")
    print("2. Decrypt a word")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        # Encryption option
        plaintext = input("Enter the word to encrypt: ")
        encrypted = encrypt(plaintext)
        print(f"Encrypted text: {encrypted}")
    
    elif choice == '2':
        # Decryption option
        ciphertext = input("Enter the word to decrypt: ")
        decrypted = decrypt(ciphertext)
        print(f"Decrypted text: {decrypted}")
    
    elif choice == '3':
        # Exit the program
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
