import pyDes as pd


key = '133457799BBCDFF1'
message = '0123456789ABCDEF'
key = bytes.fromhex(key)
message = bytes.fromhex(message)

des_obj = pd.des(key)
m = des_obj.encrypt(message)

print(m.hex())