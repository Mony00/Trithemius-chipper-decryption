def decrypt_trithemius(ciphertext):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = ""

    for i, char in enumerate(ciphertext.upper()):
        if char in alphabet:
            shift = i % 26  # Reverse the progressive shift
            new_index = (alphabet.index(char) + shift) % 26
            plaintext += alphabet[new_index]
        else:
            plaintext += char
    return plaintext