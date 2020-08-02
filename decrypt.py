import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

PASSWORD = input().encode()

backend = default_backend()
salt = "\x05\xb0\x96\xff\xfc\x84\xf9\xf0\x95|\x91\xf9\x87\x12pM".encode()

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA3_512(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=backend
)
key = base64.urlsafe_b64encode(kdf.derive(PASSWORD))

f = Fernet(key)

with open("fixkosten.txt", "rb") as file:
    data = file.read()

dec = f.decrypt(data).decode()

print(dec)

