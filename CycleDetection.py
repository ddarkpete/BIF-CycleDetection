import hashlib
hex_ind_no = 'Dq'



def hash_md5(text):
    tempHash = hashlib.md5(text.encode('utf-8')).hexdigest()
    return tempHash

text = input('Please type text to hash:')
print(hash_md5(hash_md5(text)))



