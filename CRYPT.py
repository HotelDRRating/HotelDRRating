from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

def encrypt(msg:str):
    publickey = RSA.import_key(open('keys/publickey.pem').read())
    sess_key = get_random_bytes(16)

    cipher = PKCS1_OAEP.new(publickey)
    enc_sess = cipher.encrypt(sess_key)

    cipher_aes = AES.new(sess_key, AES.MODE_EAX)
    ciphertext,tag = cipher_aes.encrypt(msg.encode('utf8'))
    q = ["".join(x) for x in (enc_sess,cipher_aes.nonce,tag,ciphertext)]
    return q
print(encrypt("TEST"))