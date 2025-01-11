import numpy as np

# Define Pauli matrices
sigma_x = np.array([[0, 1], [1, 0]])
sigma_y = np.array([[0, -1j], [1j, 0]])
sigma_z = np.array([[1, 0], [0, -1]])

# Define a matrix with eigenvalues 1, 5, 10
eigen_matrix = np.array([[5, 1], [1, 10]])

# Function to apply a quantum gate
def apply_gate(state, gate):
    return np.dot(gate, state)

# Function to encode classical bit into a quantum state
def encode_bit(bit):
    return np.array([1, 0]) if bit == '0' else np.array([0, 1])

# Function to encrypt data using quantum gates
def encrypt_bit(bit):
    state = encode_bit(bit)
    # Apply Pauli matrices and eigenvalue matrix
    encrypted_state = apply_gate(apply_gate(apply_gate(apply_gate(state, sigma_x), sigma_y), sigma_z), eigen_matrix)
    return encrypted_state

# Convert text to binary
def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

# Convert binary to text
def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

# User input for the data to encrypt
user_input = input("Enter text to encrypt: ")

# Convert input text to binary
binary_input = text_to_binary(user_input)

# Encrypt the binary data
encrypted_states = [encrypt_bit(bit) for bit in binary_input]

print("Original text:", user_input)
print("Binary input:", binary_input)
print("Encrypted states:", encrypted_states)
