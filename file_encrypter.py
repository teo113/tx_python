# author: github.com/teo113 & github.com/waggett96
# desc: This script encrypts a plain text config file for use within a db connector

from cryptography.fernet import Fernet

# function to generate a key and save to a .key file
def write_key():
    key = Fernet.generate_key()
    with open(r'encrypter_files/key.key', 'wb') as key_file:
        key_file.write(key)

# function to load a key from directory
def load_key():
    return open(r'encrypter_files/key.key', 'rb').read()

# function to encrypt a file with a key, writing output to file
def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, 'wb') as file:
        file.write(encrypted_data)

# create key (only use on first run)
write_key()
# load key
key = load_key()
# file to encrypt
creds_file = r'C:\Users\theo\Documents\tasks_c\configs\db_creds.ini'
# encrypt the file
encrypt(creds_file, key)
print(f'encrypted: {creds_file}')
