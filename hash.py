import hashlib,random,string,time

def hash(msg):
    #return hashlib.sha256(msg.encode()).hexdigest()
    return hashlib.sha3_512(msg.encode()).hexdigest()
N = 1
while True:
    print(hash(''.join(random.choices(string.ascii_uppercase + string.digits, k=N))))
    N+=1
    time.sleep(1)