from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
import base64 as b64,hashlib
def generate(keysize=2048) -> dict:
        key = RSA.generate(keysize)
        return {"public" : key.public_key().export_key().decode(), "private" : key.export_key().decode()}
def encrypt(msg,pubkey) -> str:
    publickey = RSA.importKey(pubkey)
    cipher = PKCS1_v1_5.new(publickey)
    return to_b64(cipher.encrypt(msg.encode('ascii')))
def decrypt(msg,privkey) -> str:
    privatekey = RSA.importKey(privkey)
    cipher = PKCS1_v1_5.new(privatekey)
    return cipher.decrypt(to_str(msg), Random.new().read(20+SHA.digest_size)).decode('utf-8')
def hash(msg) -> str:#dual hash implementation for a much secure verification
    return hashlib.sha3_512(hashlib.sha256(msg.encode()).hexdigest().encode()).hexdigest()
def to_b64(msg):
    return b64.b64encode(msg.encode()).decode('utf-8')
def to_str(msg) -> str:
    return b64.b64decode(msg).decode('utf-8')
