import binascii
import math
import hashlib
import os
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.backends import default_backend, openssl

def identify_binary_format(binary_data: bytes):
    """Convert binary data to ASCII format."""
    return binascii.hexlify(binary_data)

def calculate_entropy(data):
    """Calculate the entropy of given data."""
    if not data:
        return 0
    entropy = 0
    length = len(data)
    frequencies = {byte: data.count(byte) for byte in set(data)}
    for freq in frequencies.values():
        prob = freq / length
        entropy -= prob * math.log2(prob)
    return entropy

def load_rsa_key(key_file, is_public=True):
    """Load RSA key from a file."""
    with open(key_file, "rb") as file:
        if is_public:
            return serialization.load_pem_public_key(file.read(), backend=openssl.backend)
        else:
            return serialization.load_pem_private_key(file.read(), password=None, backend=openssl.backend)

def decrypt_using_rsa(encrypted_data, private_key):
    """Decrypt data using RSA."""
    return private_key.decrypt(
        encrypted_data,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )

def identify_algorithm(file_path):
    """Identify the encryption algorithm used in the file."""
    with open(file_path, 'rb') as file:
        data = file.read()

    entropy = calculate_entropy(data)
    print(f"Entropy: {entropy}")

    md5_hash = hashlib.md5(data).hexdigest()
    sha256_hash = hashlib.sha256(data).hexdigest()

    print(f"MD5 Hash: {md5_hash}")
    print(f"SHA256 Hash: {sha256_hash}")

    known_signatures = {
        'md5': 'd41d8cd98f00b204e9800998ecf8427e',
        'sha256': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
    }

    if md5_hash == known_signatures['md5']:
        print("MD5 encryption detected.")
    elif sha256_hash == known_signatures['sha256']:
        print("SHA256 encryption detected.")
    else:
        print("Unknown encryption algorithm.")

def encrypt_text(plaintext, key):
    """Encrypt text using AES."""
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    paddler = sym_padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = paddler.update(plaintext.encode()) + paddler.finalize()
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ciphertext

def decrypt_text(ciphertext, key):
    """Decrypt text using AES."""
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()
    unpadder = sym_padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext.decode()

if __name__ == '__main__':
    # Checking entropy of an encrypted binary
    file_path = '..\\encrypted.bin'
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    binary_format = identify_binary_format(binary_data)
    identify_algorithm(file_path)
    entropy = calculate_entropy(binary_data)
    print(f"Entropy: {entropy}")
    print(f"The binary format of the encrypted file is: {binary_format}")

    # Checking encrypted data by decrypting it using standard algorithm
    private_key = load_rsa_key("..\\private_key.pem", is_public=False)
    print(private_key)

    with open("..\\encrypted_message.bin", 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    print(encrypted_data)

    if not encrypted_data:
        raise ValueError("Encrypted data is empty or corrupted.")

    # Creating encryption and decryption using the RSA algorithm by using Python itself
    key = os.urandom(32)
    plaintext = "This is a secret message."
    ciphertext = encrypt_text(plaintext, key)
    decrypted_plaintext = decrypt_text(ciphertext, key)
    entropy = calculate_entropy(ciphertext)
    print(f"Entropy: {entropy}")
    print(f"Plaintext: {decrypted_plaintext}")
    print(f"Ciphertext: {ciphertext.hex()}")
    print(identify_binary_format(ciphertext))

'''
Conclusion:
Entropy algorithm is successfully tested and can be used to verify the integrity of the Encrypted data.

If we create an shell scripted openssl private public key and creates an encrypted bin, it is not possible to decrypt the -
same using the python script. May be because of additional padding.

If we create encrypted bin using python and decrypt the same, it works fine. 

Steps to use OpenSSL for creating the Encrypted data:

openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048...
openssl rsautl -encrypt -inkey public_key.pem -pubin -in message.txt -out encrypted_message.bin                                                                                                                                                    
'''
