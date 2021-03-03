from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
import base64 as b64
def generate(keysize=2048):
        key = RSA.generate(keysize)
        privatekey = key.export_key()
        publickey = key.public_key().export_key()
        return {"public" : publickey.decode(), "private" : privatekey.decode()}
def encrypt(msg,pubkey):
    publickey = RSA.importKey(pubkey)
    cipher = PKCS1_v1_5.new(publickey)
    return b64.b64encode(cipher.encrypt(msg.encode('ascii'))).decode('ascii')
def decrypt(msg,privkey):
    privatekey = RSA.importKey(privkey)
    cipher = PKCS1_v1_5.new(privatekey)
    return cipher.decrypt(b64.b64decode(msg), Random.new().read(20+SHA.digest_size)).decode('utf-8')

for i in range(10):
    print("Key Pair" + str(generate()))