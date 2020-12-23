import hashlib,os,time,sys
from time import sleep
import timeit
import threading


Aqua = '\033[1;36m'
BRed='\033[1;31m'
BYellow='\033[1;33m'


def clear():
    banner = f'''{Aqua}
  _   _           _               
 | | | | __ _ ___| |__   ___ _ __ 
 | |_| |/ _` / __| '_ \ / _ \ '__|
 |  _  | (_| \__ \ | | |  __/ |   
 |_| |_|\__,_|___/_| |_|\___|_|   
                        {BRed}By RedMad :P {BYellow}v1{Aqua}
    '''
    os.system("clear")
    print(banner)



def hashing_md5():
    #! This function hashing with MD5 :D   
    clear()
    print(f"{BYellow}[{Aqua}MD5{BYellow}/{Aqua}List{BYellow}/{Aqua}hash{BYellow}]{Aqua}")
    print(" ")
    counter = 0
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.md5(i.encode())
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()



def hashing_sha1():
    #! This function hashing with SHA1 :D 
    clear()
    counter = 0 
    print(f"{BYellow}[{Aqua}SHA-1{BYellow}/{Aqua}List{BYellow}/{Aqua}hash{BYellow}]{Aqua}")
    print(" ")
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.sha1(i.encode())
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()




def hashing_sha224():
    #! This function hashing with SHA224 :D 
    clear()
    counter = 0
    print(f"{BYellow}[{Aqua}SHA-224{BYellow}/{Aqua}List{BYellow}/{Aqua}hash{BYellow}]{Aqua}")
    print(" ")
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.sha224(i.encode())
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()




def hashing_sha256():
    #! This function hashing with SHA256 :D 
    clear()
    counter = 0
    print(f"{BYellow}[{Aqua}SHA-256{BYellow}/{Aqua}List{BYellow}/{Aqua}hash{BYellow}]{Aqua}")
    print(" ")
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.sha256(i.encode())
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()




def hashing_sha384():
    #! This function hashing with SHA384 :D 
    clear()
    counter = 0
    print(f"{BYellow}[{Aqua}SHA-384{BYellow}/{Aqua}List{BYellow}/{Aqua}hash{BYellow}]{Aqua}")
    print(" ")
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.sha384(i.encode())
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()




def hashing_sha512():
    #! This function hashing with SHA512 :D 
    clear()
    counter = 0
    print(f"{BYellow}[{Aqua}SHA-512{BYellow}/{Aqua}List{BYellow}/{Aqua}hash{BYellow}]{Aqua}")
    print(" ")
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.sha512(i.encode())
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()




def hashing_sha3_224():
    #! This function hashing with SHA3-224 :D 
    clear()
    counter = 0
    print(f"{BYellow}[{Aqua}SHA3-224{BYellow}/{Aqua}List{BYellow}/{Aqua}hash{BYellow}]{Aqua}")
    print(" ")
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.sha3_224(i.encode())
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()



def hashing_sha3_256():
    #! This function hashing with SHA3-256 :D 
    clear()
    counter = 0
    print(f"{BYellow}[{Aqua}SHA3-256{BYellow}/{Aqua}List{BYellow}/{Aqua}hash{BYellow}]{Aqua}")
    print(" ")
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.sha3_256(i.encode())
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()



def hashing_sha3_384():
    #! This function hashing with SHA3-384 :D 
    clear()
    counter = 0
    print(f"{BYellow}[{Aqua}SHA3-384{BYellow}/{Aqua}List{BYellow}/{Aqua}hash{BYellow}]{Aqua}")
    print(" ")
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.sha3_384(i.encode())
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()



def hashing_sha3_512():
    #! This function hashing with SHA3-512 :D 
    clear()
    counter = 0
    print(f"{BYellow}[{Aqua}SHA3-512{BYellow}/{Aqua}List{BYellow}/{Aqua}hash{BYellow}]{Aqua}")
    print(" ")
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.sha3_512(i.encode())
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()




def hashing_blake_2b():
    #! This function hashing with BLAKE-2B :D 
    clear()
    counter = 0
    print(f"{BYellow}[{Aqua}BLAKE-2B{BYellow}/{Aqua}List{BYellow}/{Aqua}hash{BYellow}]{Aqua}")
    print(" ")
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.blake2b(i.encode())
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()




def hashing_blake_2s():
    #! This function hashing with BLAKE-2S :D 
    clear()
    counter = 0
    print(f"{BYellow}[{Aqua}BLAKE-2S{BYellow}/{Aqua}List{BYellow}/{Aqua}hash{BYellow}]{Aqua}")
    print(" ")
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.blake2s(i.encode())
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()





def output_write_md5():
    clear()
    print(f"{BYellow}[{Aqua}MD5{BYellow}/{Aqua}List{BYellow}/{Aqua}word:hash{BYellow}]{Aqua}")
    print(" ")
    counter = 0 
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w+")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.md5(i.encode())
            file.write(i)
            file.write(":")
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()





def output_write_sha1():
    clear()
    print(f"{BYellow}[{Aqua}SHA-1{BYellow}/{Aqua}List{BYellow}/{Aqua}word:hash{BYellow}]{Aqua}")
    print(" ")
    counter = 0 
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w+")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.sha1(i.encode())
            file.write(i)
            file.write(":")
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
            
    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()






def output_write_sha224():
    clear()
    print(f"{BYellow}[{Aqua}SHA-224{BYellow}/{Aqua}List{BYellow}/{Aqua}word:hash{BYellow}]{Aqua}")
    print(" ")
    counter = 0 
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w+")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.sha224(i.encode())
            file.write(i)
            file.write(":")
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()

    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()






def output_write_sha256():
    clear()
    print(f"{BYellow}[{Aqua}SHA-256{BYellow}/{Aqua}List{BYellow}/{Aqua}word:hash{BYellow}]{Aqua}")
    print(" ")
    counter = 0 
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()
    
    file = open("hashed.txt","w+")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.sha256(i.encode())
            file.write(i)
            file.write(":")
            file.write(hashed.hexdigest())
            file.write("\n")
                
    except:
        exit()
    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()





def output_write_sha384():
    clear()
    print(f"{BYellow}[{Aqua}SHA-384{BYellow}/{Aqua}List{BYellow}/{Aqua}word:hash{BYellow}]{Aqua}")
    print(" ")
    counter = 0 
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w+")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.sha384(i.encode())
            file.write(i)
            file.write(":")
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
            

    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()






def output_write_sha512():
    clear()
    print(f"{BYellow}[{Aqua}SHA-512{BYellow}/{Aqua}List{BYellow}/{Aqua}word:hash{BYellow}]{Aqua}")
    print(" ")
    counter = 0 
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w+")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.sha512(i.encode())
            file.write(i)
            file.write(":")
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
            

    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()




def output_write_sha3_224():
    clear()
    print(f"{BYellow}[{Aqua}SHA3-224{BYellow}/{Aqua}List{BYellow}/{Aqua}word:hash{BYellow}]{Aqua}")
    print(" ")
    counter = 0 
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w+")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.sha3_224(i.encode())
            file.write(i)
            file.write(":")
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
            

    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()



def output_write_sha3_256():
    clear()
    print(f"{BYellow}[{Aqua}SHA3-256{BYellow}/{Aqua}List{BYellow}/{Aqua}word:hash{BYellow}]{Aqua}")
    print(" ")
    counter = 0 
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w+")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.sha3_256(i.encode())
            file.write(i)
            file.write(":")
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
            

    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()



def output_write_sha3_384():
    clear()
    print(f"{BYellow}[{Aqua}SHA3-384{BYellow}/{Aqua}List{BYellow}/{Aqua}word:hash{BYellow}]{Aqua}")
    print(" ")
    counter = 0 
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w+")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.sha3_384(i.encode())
            file.write(i)
            file.write(":")
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
            

    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()




def output_write_sha3_512():
    clear()
    print(f"{BYellow}[{Aqua}SHA3-512{BYellow}/{Aqua}List{BYellow}/{Aqua}word:hash{BYellow}]{Aqua}")
    print(" ")
    counter = 0 
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w+")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.sha3_512(i.encode())
            file.write(i)
            file.write(":")
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
            

    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()




def output_write_blake_2b():
    clear()
    print(f"{BYellow}[{Aqua}BLAKE-2B{BYellow}/{Aqua}List{BYellow}/{Aqua}word:hash{BYellow}]{Aqua}")
    print(" ")
    counter = 0 
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w+")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.blake2b(i.encode())
            file.write(i)
            file.write(":")
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
            

    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()




def output_write_blake_2s():
    clear()
    print(f"{BYellow}[{Aqua}BLAKE-2S{BYellow}/{Aqua}List{BYellow}/{Aqua}word:hash{BYellow}]{Aqua}")
    print(" ")
    counter = 0 
    try:
        s = open("words.txt","r")
    except:
        print(f"{BYellow}[{BRed}!{BYellow}]{BRed} List {BYellow}words.txt{BRed} is not found!{BYellow},{BYellow} Create one with same name\n")
        sleep(0.5)
        sys.exit()

    file = open("hashed.txt","w+")
    print(f"{Aqua}Hashing{BYellow}...")
    start_time = timeit.default_timer()
    try:
        s_read = s.read()
        for i in s_read.split("\n"):
            counter = counter + 1
            hashed = hashlib.blake2s(i.encode())
            file.write(i)
            file.write(":")
            file.write(hashed.hexdigest())
            file.write("\n")
    except:
        exit()
            

    print(" ")
    print(f"{Aqua}Done{BYellow}!{Aqua} {counter} hashes, Saved As {BYellow}hashed.txt")
    stop = timeit.default_timer()
    print('Time:', format(stop - start_time,".2f"),"Sec!")
    file.close()





def md5_single():
    clear()
    print(f"{BYellow}[{Aqua}MD5{BYellow}/{Aqua}Single{BYellow}]")
    print(" ")
    word = input(f"{BYellow}[{Aqua}#{BYellow}]{Aqua} Enter The Word ~{BYellow}>{Aqua} ")    
    hashed_word = hashlib.md5(word.encode())
    print(" ")
    print(str(hashed_word.hexdigest()))
    print(" ")





def sha1_single():
    clear()
    print(f"{BYellow}[{Aqua}SHA-1{BYellow}/{Aqua}Single{BYellow}]")
    print(" ")
    word = input(f"{BYellow}[{Aqua}#{BYellow}]{Aqua} Enter The Word ~{BYellow}>{Aqua} ")    
    hashed_word = hashlib.sha1(word.encode())
    print(" ")
    print(str(hashed_word.hexdigest()))







def sha224_single():
    clear()
    print(f"{BYellow}[{Aqua}SHA-224{BYellow}/{Aqua}Single{BYellow}]")
    print(" ")
    word = input(f"{BYellow}[{Aqua}#{BYellow}]{Aqua} Enter The Word ~{BYellow}>{Aqua} ")  
    hashed_word = hashlib.sha224(word.encode())
    print(" ")
    print(str(hashed_word.hexdigest()))







def sha256_single():
    clear()
    print(f"{BYellow}[{Aqua}SHA-256{BYellow}/{Aqua}Single{BYellow}]")
    print(" ")
    word = input(f"{BYellow}[{Aqua}#{BYellow}]{Aqua} Enter The Word ~{BYellow}>{Aqua} ")   
    hashed_word = hashlib.sha256(word.encode())
    print(" ")
    print(str(hashed_word.hexdigest()))







def sha384_single():
    clear()
    print(f"{BYellow}[{Aqua}SHA-384{BYellow}/{Aqua}Single{BYellow}]")
    print(" ")
    word = input(f"{BYellow}[{Aqua}#{BYellow}]{Aqua} Enter The Word ~{BYellow}>{Aqua} ")   
    hashed_word = hashlib.sha384(word.encode())
    print(" ")
    print(str(hashed_word.hexdigest()))







def sha512_single():
    clear()
    print(f"{BYellow}[{Aqua}SHA-512{BYellow}/{Aqua}Single{BYellow}]")
    print(" ")
    word = input(f"{BYellow}[{Aqua}#{BYellow}]{Aqua} Enter The Word ~{BYellow}>{Aqua} ")    
    hashed_word = hashlib.sha512(word.encode())
    print(" ")
    print(str(hashed_word.hexdigest()))
    



def sha3_224_single():
    clear()
    print(f"{BYellow}[{Aqua}SHA3-224{BYellow}/{Aqua}Single{BYellow}]")
    print(" ")
    word = input(f"{BYellow}[{Aqua}#{BYellow}]{Aqua} Enter The Word ~{BYellow}>{Aqua} ")    
    hashed_word = hashlib.sha3_224(word.encode())
    print(" ")
    print(str(hashed_word.hexdigest()))



def sha3_256_single():
    clear()
    print(f"{BYellow}[{Aqua}SHA3-256{BYellow}/{Aqua}Single{BYellow}]")
    print(" ")
    word = input(f"{BYellow}[{Aqua}#{BYellow}]{Aqua} Enter The Word ~{BYellow}>{Aqua} ")    
    hashed_word = hashlib.sha3_256(word.encode())
    print(" ")
    print(str(hashed_word.hexdigest()))



def sha3_384_single():
    clear()
    print(f"{BYellow}[{Aqua}SHA3-384{BYellow}/{Aqua}Single{BYellow}]")
    print(" ")
    word = input(f"{BYellow}[{Aqua}#{BYellow}]{Aqua} Enter The Word ~{BYellow}>{Aqua} ")    
    hashed_word = hashlib.sha3_384(word.encode())
    print(" ")
    print(str(hashed_word.hexdigest()))



def sha3_512_single():
    clear()
    print(f"{BYellow}[{Aqua}SHA3-512{BYellow}/{Aqua}Single{BYellow}]")
    print(" ")
    word = input(f"{BYellow}[{Aqua}#{BYellow}]{Aqua} Enter The Word ~{BYellow}>{Aqua} ")    
    hashed_word = hashlib.sha3_512(word.encode())
    print(" ")
    print(str(hashed_word.hexdigest()))




def blake_2b_single():
    clear()
    print(f"{BYellow}[{Aqua}BLAKE-2B{BYellow}/{Aqua}Single{BYellow}]")
    print(" ")
    word = input(f"{BYellow}[{Aqua}#{BYellow}]{Aqua} Enter The Word ~{BYellow}>{Aqua} ")    
    hashed_word = hashlib.blake2b(word.encode())
    print(" ")
    print(str(hashed_word.hexdigest()))




def blake_2s_single():
    clear()
    print(f"{BYellow}[{Aqua}BLAKE-2s{BYellow}/{Aqua}Single{BYellow}]")
    print(" ")
    word = input(f"{BYellow}[{Aqua}#{BYellow}]{Aqua} Enter The Word ~{BYellow}>{Aqua} ")    
    hashed_word = hashlib.blake2s(word.encode())
    print(" ")
    print(str(hashed_word.hexdigest()))
