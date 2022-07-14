# encrypt/decrypt pkgs
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2
import base64
import hashlib
import environ
env = environ.Env()
environ.Env.read_env()
CIPHER = env('CIPHER')
password = CIPHER
# https://www.quickprogrammingtips.com/python/aes-256-encryption-and-decryption-in-python.html
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def get_private_key():
    salt = b"salt bae"
    kdf = PBKDF2(CIPHER, salt, 64, 1000)
    key = kdf[:32]
    return key

def encrypt(raw):
    private_key = get_private_key()
    raw = pad(raw).encode('utf8')
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CFB, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))

def decrypt(enc):
    private_key = get_private_key()
    enc = base64.urlsafe_b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CFB, iv)
    return unpad(cipher.decrypt(enc[16:]))
