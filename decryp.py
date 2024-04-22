def decrypt_message(encrypted_message, key):
    decrypted_message = ''
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        key_bit = key[i % len(key)]
        decrypted_char = chr(ord(char) - key_bit)
        decrypted_message += decrypted_char
    return decrypted_message
