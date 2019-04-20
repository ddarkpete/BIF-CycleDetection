import hashlib
import sys
hex_ind_no = 'Dq'


def hash_md5(text):
    tempHash = hashlib.md5(text.encode('utf-8')).digest()
    #print(tempHash)
    tempHash = hashlib.md5(tempHash) #.encode('utf-8')).hexdigest()
    #temp = str.encode(tempHash)
    
    #print(tempHash)
    #print(sys.getsizeof(temp))
    #print(temp.decode())
    #product = truncate_unicode_to_byte_limit(tempHash,54)
    #print(sys.getsizeof(tempHash[:14]))
    
    return tempHash.hexdigest() [:14]

def floyd(fx, x0):
    tortoise = fx(x0)
    hare = fx(fx(x0))

    print("First stage of Floyd's algorithm.")
    print("Searching for a cycle...")

    counter = 0

    while(tortoise !=  hare):
        tortoise = fx(tortoise)
        hare = fx(fx(hare))

        counter += 1

        if(counter % 10000000 == 0):
            print(counter)

    print("Cycle found!")
    print("Second stage - finding the colission")

    tortoise = x0
    counter = 0
    while(tortoise != hare):
        tortoise = fx(tortoise)
        hare = fx(hare)

        counter += 1

        if(counter % 10000000 == 0):
            print(counter)

        if(tortoise != hare): #remembering last pair of hashes
            last_tortoise = tortoise
            last_hare = hare
        
        if(fx(tortoise) == fx(hare)):
            print("Colission found!")
            print("Hare: {}".format(last_hare))
            print("Tortoise: {}".format(last_tortoise))
            print("hash({}) = {}".format(last_hare,fx(last_hare)))
            print("hash({}) = {}".format(last_tortoise,fx(last_tortoise)))
            with open('colision.txt', 'w') as file:
                file.write("Hare = {} \n Tortoise = {}".format(last_hare,last_tortoise))

    print("hash({}) = {}".format(last_hare,fx(last_hare)))
    print("hash({}) = {}".format(last_tortoise,fx(last_tortoise)))




floyd(hash_md5,hex_ind_no)
#floyd(hash_md5,'renmich')
#print(len(hex_ind_no))
#xd = hash_md5(hex_ind_no)

#text = input('Please type text to hash:')
#print(hash_md5(hex_ind_no))
#print(xd)
#print(sys.getsizeof(hash_md5(hex_ind_no)))
#print(sys.getsizeof(hash_md5(hex_ind_no)))