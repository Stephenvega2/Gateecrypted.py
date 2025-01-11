import numpy as np
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Define Pauli matrices
sigma_x = np.array([[0, 1], [1, 0]])
sigma_y = np.array([[0, -1j], [1j, 0]])
sigma_z = np.array([[1, 0], [0, -1]])

# Define an eigenvalue matrix for added complexity
eigen_matrix = np.array([[5, 1], [1, 10]])

# Function to apply a quantum gate
def apply_gate(state, gate):
    return np.dot(gate, state)

# Function to encode classical bit into a quantum state
def encode_bit(bit):
    return np.array([1, 0]) if bit == '0' else np.array([0, 1])

# Function to encrypt data using quantum gates and eigenvalue matrix
def encrypt_bit(bit):
    state = encode_bit(bit)
    encrypted_state = apply_gate(apply_gate(apply_gate(apply_gate(state, sigma_x), sigma_y), sigma_z), eigen_matrix)
    return encrypted_state

# Convert text to binary
def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

# Function to transform encrypted states to a string
def encrypted_states_to_str(encrypted_states):
    return ''.join([str(state[0]) + ',' + str(state[1]) + ';' for state in encrypted_states])

# Function to encrypt transformed data using AES
def aes_encrypt(data):
    key = get_random_bytes(16)  # AES key must be either 16, 24, or 32 bytes long
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('ascii'))
    return base64.b64encode(nonce + ciphertext).decode('ascii'), key

# User input for the data to encrypt
user_input = input("Enter text to encrypt: ")

# Convert input text to binary
binary_input = text_to_binary(user_input)

# Encrypt the binary data using quantum encryption
encrypted_states = [encrypt_bit(bit) for bit in binary_input]

# Transform encrypted states to a string
encrypted_string = encrypted_states_to_str(encrypted_states)

# Encrypt the transformed string using AES
final_encrypted_text, aes_key = aes_encrypt(encrypted_string)

print("Original text:", user_input)
print("Binary input:", binary_input)
print("Quantum encrypted states:", encrypted_states)
print("Transformed string for AES encryption:", encrypted_string)
print("Final encrypted text (AES):", final_encrypted_text)
