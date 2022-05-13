## Credit to Haider Imtiaz

# Lock Your Files
#pip install cryptography
from cryptography.fernet import Fernet

def Lock_file(file_name, key):
    with open(file_name, 'rb') as file:
        data = file.read()
    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    with open(file_name, 'wb') as file:
        file.write(encrypted_data)
    print("File Lock...")

def Unlock_file(file_name, key):
    with open(file_name, 'rb') as file:
        data = file.read()
    f = Fernet(key)
    decrypted_data = f.decrypt(data)
    with open(file_name, 'wb') as file:
        file.write(decrypted_data)
    print("File Unlock...")

key = input("Enter the key: ")
Lock_file('test.txt', key)
Unlock_file('test.txt', key)