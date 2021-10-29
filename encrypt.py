from aes256 import encrypt
from getpass import getpass

raw = input("Raw : ")
password = getpass("Password : ")

print(encrypt(raw,password).decode("utf-8") )
