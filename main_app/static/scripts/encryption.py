# encrypt/decrypt pkgs
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2
import base64

# https://www.quickprogrammingtips.com/python/aes-256-encryption-and-decryption-in-python.html
pad = lambda s: s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

# def get_private_key():
#     salt = b"salt bae"
#     kdf = PBKDF2(CIPHER, salt, 64, 1000)
#     key = kdf[:32]
#     return key

# def encrypt(raw):
#     private_key = get_private_key()
#     raw = pad(raw).encode('utf8')
#     iv = Random.new().read(AES.block_size)
#     cipher = AES.new(private_key, AES.MODE_CFB, iv)
#     return base64.b64encode(iv + cipher.encrypt(raw))

# def decrypt(enc):
#     private_key = get_private_key()
#     enc = base64.b64decode(enc)
#     iv = enc[:16]
#     cipher = AES.new(private_key, AES.MODE_CFB, iv)
#     return unpad(cipher.decrypt(enc[16:]))

def get_private_key(password):
    salt = b"this is a salt"
    kdf = PBKDF2(password, salt, 64, 1000)
    key = kdf[:32]
    print(key)
    return key
 
 
def encrypt(raw, password):
    private_key = get_private_key(password)
    raw = pad(raw).encode('utf-8')
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CFB, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))
 
 
def decrypt(enc, password):
    private_key = get_private_key(password)
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CFB, iv)
    return unpad(cipher.decrypt(enc[16:]))