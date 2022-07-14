# encrypt/decrypt pkgs
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2
import base64
import hashlib

# https://www.quickprogrammingtips.com/python/aes-256-encryption-and-decryption-in-python.html
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
password = 'spiral'

def get_private_key(password):
    salt = b"salt bae"
    kdf = PBKDF2(password, salt, 64, 1000)
    key = kdf[:32]
    return key

def encrypt(raw, password):
    private_key = get_private_key(password)
    raw = pad(raw).encode('utf8')
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return [base64.b64encode(iv + cipher.encrypt(raw)), private_key]

def decrypt(enc, password):
    private_key = get_private_key(password)
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))

# encrypted = encrypt("message".encode('utf8'), "spiral".encode('utf8'))
# print(encrypted)
# decrypted = decrypt(encrypted[0].decode('utf8'), 'spiral'.encode('utf8'))
# print(decrypted)