import hashlib

sen_1 = b'If you want to keep a secret, you must also hide it from yourself'
sen_2 = b'If you want to eep a secret, you must also hide it from yourself'


# md5
print("md5:")
hash_object_1 = hashlib.md5(sen_1)
print("hashed sentence (original sentence):", hash_object_1.hexdigest())
sen_1_md5 = format(int(hash_object_1.hexdigest(), 16), '0128b')


hash_object_2 = hashlib.md5(sen_2)
print("hashed sentence (without k in keep):", hash_object_2.hexdigest())
sen_2_md5 = format(int(hash_object_2.hexdigest(), 16), '0128b')

diff = [i for i in range(len(sen_1_md5)) if sen_1_md5[i] != sen_2_md5[i]]
print("how many different bits!? ", len(diff))


# SHA256
print("sha256:")
hash_object_1 = hashlib.sha256(sen_1)
print("hashed sentence (original sentence):",hash_object_1.hexdigest())
sen_1_sha = format(int(hash_object_1.hexdigest(), 16), '0256b')

hash_object_2 = hashlib.sha256(sen_2)
print("hashed sentence (without k in keep):", hash_object_2.hexdigest())
sen_2_sha = format(int(hash_object_2.hexdigest(), 16), '0256b')

diff = [i for i in range(len(sen_1_sha)) if sen_1_sha[i] != sen_2_sha[i]]
print("how many different bits!? ", len(diff))
