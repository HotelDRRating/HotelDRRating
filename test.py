class binary(object):
    def __init__(self):
        return
    def convert_to_binary(self,hotel:str,fullname:str,email:str,password:str):
        self.hotel_binary = []
        self.fullname_binary = []
        self.email_binary = []
        self.password_binary = []
        for byte in hotel.encode('utf8'):
            self.hotel_binary.append(bin(byte))
        for byte in fullname.encode('utf8'):
            self.fullname_binary.append(bin(byte))
        for byte in email.encode('utf8'):
            self.email_binary.append(bin(byte))
        for byte in password.encode('utf8'):
            self.password_binary.append(bin(byte))
        
        return {"hotel":" ".join(self.hotel_binary),"fullname":" ".join(self.fullname_binary),"email":" ".join(self.email_binary),"password": " ".join(self.password_binary)}
    def convert_to_string(self,hotel:str,fullname:str,email:str,password:str):
        a = hotel.split(" ")
        b = fullname.split(" ")
        c = email.split(" ")
        d = password.split(" ")
        return {"hotel":"".join([chr(int(q,2)) for q in a]), "fullname":"".join([chr(int(q, 2)) for q in b]), "email":"".join([chr(int(q,2)) for q in c]), "password":"".join([chr(int(q,2)) for q in d])}

a = binary()
print(a.convert_to_string('0b1010100 0b1001000 0b1001001 0b1010011 0b100000 0b1001001 0b1010011 0b100000 0b1000001 0b100000 0b1010100 0b1000101 0b1010011 0b1010100','0b1110100 0b1100101 0b1110011 0b1110100 0b1110100','0b1010001 0b1010111 0b1000101 0b1010100 0b1010010','0b1000001 0b1010011 0b1000100 0b1000001 0b1010011 0b1000100'))
