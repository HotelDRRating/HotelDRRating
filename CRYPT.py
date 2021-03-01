import rsa, base64 as b64
class c(object):
    def __init__(self):
        return
    def generate(self,bits=2048):
        public,private = rsa.newkeys(bits)
        return {'public':public,'private':private}
    def encrypt(self,msg,publickey):
            return b64.b64encode(rsa.encrypt(msg.encode('utf-8'),publickey)).decode('utf-8')
    def decrypt(self,msg,privatekey):
        return rsa.decrypt(b64.b64decode(msg),privatekey).decode('utf-8')

