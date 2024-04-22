from qiskit import QuantumCircuit, Aer, execute
from key import bb84_key
from encryp import encrypt_message
from decryp import decrypt_message
from numpy.random import randint

message = "quantum hola"
key = bb84_key(len(message)*8)
encrypted = encrypt_message(message, key)
decrypted = decrypt_message(encrypted, key)
print("Original Message:", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
