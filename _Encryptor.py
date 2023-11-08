from cryptography.fernet import Fernet

class Encryptor:
    def __init__(self, key_file_path: str):
        self.key = self.load_key(key_file_path)

    @staticmethod
    def load_key(key_file_path: str) -> bytes:
        # Open the file containing the key
        with open(key_file_path, 'rb') as key_file:
            key = key_file.read()
        return key

    def encrypt_string(self, input_string: str) -> bytes:
        # Create a Fernet object with the encryption key
        f = Fernet(self.key)
        # Encode the input string to bytes, then encrypt
        encrypted = f.encrypt(input_string.encode())
        return encrypted

    def decrypt_string(self, encrypted_string: bytes) -> str:
        # Create a Fernet object with the encryption key
        f = Fernet(self.key)
        # Decrypt the data, then decode to a string
        decrypted = f.decrypt(encrypted_string).decode()
        return decrypted

# Usage example
if __name__ == '__main__':
    # Path to the key file
    key_path = 'key.txt'
    
    # Create an Encryptor instance with the key
    e = Encryptor(key_path)

    # Example usage
    secret_message = 'Hello, this is a secret message!'
    encrypted_message = e.encrypt_string(secret_message)
    print('Encrypted:', encrypted_message)

    decrypted_message = e.decrypt_string(encrypted_message)
    print('Decrypted:', decrypted_message)
