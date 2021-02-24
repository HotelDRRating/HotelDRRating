import rsa,base64 as b64
def generate(bits=2048):
    public,private = rsa.newkeys(bits)
    return {"private" : private, "public" : public}
def encrypt(msg,publickey):
    return b64.b64encode(rsa.encrypt(msg.encode('utf-8'),publickey))
def decrypt(msg,privatekey):
    return rsa.decrypt(b64.b64decode(msg),privatekey).decode('utf-8')