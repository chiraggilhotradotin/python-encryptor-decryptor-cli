from aes256 import decrypt
from getpass import getpass

encrypted = input("Encrypted string : ")
password = getpass("Password : ")

print(decrypt(encrypted,password).decode("utf-8") )
