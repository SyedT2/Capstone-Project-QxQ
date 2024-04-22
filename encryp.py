def encrypt_message(message, key):
    encrypted_message = ''
    for i in range(len(message)):
        char = message[i]
        key_bit = key[i % len(key)]
        encrypted_char = chr(ord(char) + key_bit)
        encrypted_message += encrypted_char
    return encrypted_message