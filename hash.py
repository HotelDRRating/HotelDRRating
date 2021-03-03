import hashlib

def hash(msg):
    return hashlib.sha256(msg.encode()).hexdigest()