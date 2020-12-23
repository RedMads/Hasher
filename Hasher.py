import hashlib,os,time,sys
from time import sleep
import moduels.des as des
import moduels.moud as moud
import timeit

Aqua = '\033[1;36m'
BRed='\033[1;31m'
BYellow='\033[1;33m'

def start():
    banner = f''' {Aqua}
  _   _           _               
 | | | | __ _ ___| |__   ___ _ __ 
 | |_| |/ _` / __| '_ \ / _ \ '__|
 |  _  | (_| \__ \ | | |  __/ |   
 |_| |_|\__,_|___/_| |_|\___|_|   
                        {BRed}by RedMad :P {BYellow}v1{Aqua}
'''
    os.system("clear")
    print(banner)


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(0.05)


def choose_end():
    print(" ")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back main menu")
    print(" ")
    try:
        enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    except:
        pass

    while True:
        if enter == "0":
            choose()
        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{Aqua}${BYellow}>{Aqua} ")



#? -----------------------------------------------------

#! +--------------------+
#! | Choose functions :D|
#! +--------------------+



def choose_md5():
    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:
        if enter == "1":
            des.print_type_write_md5()
            type_write_md5()
            break
            
        elif enter == "2":
            start()
            moud.md5_single()
            choose_end()

            
        elif enter == "0":
            choose()
            break
            
        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")



def choose_sha1():
    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:
        if enter == "1":

            des.print_type_write_sha1()
            type_write_sha1()
            break

        elif enter == "2":

            moud.sha1_single()
            choose_end()
            break

        elif enter == "0":

            choose()
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")


def choose_sha224():
    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:
        if enter == "1":

            des.print_type_write_sha224()
            type_write_sha224()
            break

        elif enter == "2":

            moud.sha224_single()
            choose_end()
            break

        elif enter == "0":

            choose()
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")



def choose_sha256():
    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:
        if enter == "1":

            des.print_type_write_sha256()
            type_write_sha256()
            break
        elif enter == "2":

            moud.sha256_single()
            choose_end()
            break
        elif enter == "0":

            choose()
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")


def choose_sha384():
    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:
        if enter == "1":

            des.print_type_write_sha384()
            type_write_sha384()
            break

        elif enter == "2":

            moud.sha384_single()
            choose_end()
            break

        elif enter == "0":

            choose() 
            break
        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")


def choose_sha512():
    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:
        if enter == "1":

            des.print_type_write_sha512()
            type_write_sha512()
            break

        elif enter == "2":

            moud.sha512_single()
            choose_end()
            break

        elif enter == "0":

            choose() 
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")



def choose_sha3_224():
    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:
        if enter == "1":

            des.print_type_write_sha3_224()
            type_write_sha3_224()
            break

        elif enter == "2":

            moud.sha3_224_single()
            choose_end()
            break

        elif enter == "0":
            choose() 
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")



def choose_sha3_256():
        
    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:
        if enter == "1":

            des.print_type_write_sha3_256()
            type_write_sha3_256()
            break

        elif enter == "2":

            moud.sha3_256_single()
            choose_end()
            break

        elif enter == "0":
            choose() 
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")



def choose_sha3_384():
        
    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:
        if enter == "1":

            des.print_type_write_sha3_384()
            type_write_sha3_384()
            break

        elif enter == "2":

            moud.sha3_384_single()
            choose_end()
            break

        elif enter == "0":
            choose() 
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")



def choose_sha3_512():
        
    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:
        if enter == "1":

            des.print_type_write_sha3_512()
            type_write_sha3_512()
            break

        elif enter == "2":

            moud.sha3_512_single()
            choose_end()
            break

        elif enter == "0":
            choose() 
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")



            
def choose_blake_2b():
        
    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:
        if enter == "1":

            des.print_type_write_blake_2b()
            type_write_blake_2b()
            break

        elif enter == "2":

            moud.blake_2b_single()
            choose_end()
            break

        elif enter == "0":
            choose() 
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")




def choose_blake_2s():
        
    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:
        if enter == "1":

            des.print_type_write_blake_2s()
            type_write_blake_2s()
            break

        elif enter == "2":

            moud.blake_2s_single()
            choose_end()
            break

        elif enter == "0":
            choose() 
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ") 

#? -----------------------------------------------------

#! +------------------------+
#! | Type_write functions :D|
#! +------------------------+


def type_write_md5():

    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:
        if enter == "1":
            moud.output_write_md5()
            choose_end()
            break

        elif enter == "2":
            moud.hashing_md5()
            choose_end()
            break

        elif enter == "0":
            des.print_md5()
            choose_md5()
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")



def type_write_sha1():

    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:

        if enter == "1":
            moud.output_write_sha1()
            choose_end()
            break

        elif enter == "2":
            moud.hashing_sha1()
            choose_end()
            break

        elif enter == "0":
            des.print_sha1()
            choose_sha1()
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")

def type_write_sha224():

    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:

        if enter == "1":
            moud.output_write_sha224()
            choose_end()
            break

        elif enter == "2":
            moud.hashing_sha224()
            choose_end()
            break
            
        elif enter == "0":
            des.print_sha224()
            choose_sha224()
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")



def type_write_sha256():

    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:

        if enter == "1":
            moud.output_write_sha256()
            choose_end()
            break

        elif enter == "2":
            moud.hashing_sha256()
            choose_end()
            break

        elif enter == "0":
            des.print_sha256()
            choose_sha256() 
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")              



def type_write_sha384():

    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:

        if enter == "1":
            moud.output_write_sha384()
            choose_end()
            break

        elif enter == "2":
            moud.hashing_sha384()
            choose_end()
            break

        elif enter == "0":
            des.print_sha384()
            choose_sha384()
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")



def type_write_sha512():

    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:

        if enter == "1":
            moud.output_write_sha512()
            choose_end()
            break

        elif enter == "2":
            moud.hashing_sha512()
            choose_end()
            break

        elif enter == "0":
            des.print_sha512()
            choose_sha512() 
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")



def type_write_sha3_224():


    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:

        if enter == "1":
            moud.output_write_sha3_224()
            choose_end()
            break

        elif enter == "2":
            moud.hashing_sha3_224()
            choose_end()
            break

        elif enter == "0":
            des.print_sha3_224()
            choose_sha3_224() 
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")



def type_write_sha3_256():

    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:

        if enter == "1":
            moud.output_write_sha3_256()
            choose_end()
            break

        elif enter == "2":
            moud.hashing_sha3_256()
            choose_end()
            break

        elif enter == "0":
            des.print_sha3_256()
            choose_sha3_256()
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")



def type_write_sha3_384():


    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:

        if enter == "1":
            moud.output_write_sha3_384()
            choose_end()
            break

        elif enter == "2":
            moud.hashing_sha3_384()
            choose_end()
            break

        elif enter == "0":
            des.print_sha3_384()
            choose_sha3_384()
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")




def type_write_sha3_512():

    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:

        if enter == "1":
            moud.output_write_sha3_512()
            choose_end()
            break

        elif enter == "2":
            moud.hashing_sha3_512()
            choose_end()
            break

        elif enter == "0":
            des.print_sha3_512()
            choose_sha3_512()
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")




def type_write_blake_2b():

    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:

        if enter == "1":
            moud.output_write_blake_2b()
            choose_end()
            break

        elif enter == "2":
            moud.hashing_blake_2b()
            choose_end()
            break

        elif enter == "0":
            des.print_blake_2b()
            choose_blake_2b() 
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")
  



def type_write_blake_2s():

    enter = input(f"{BYellow}${Aqua}>{Aqua} ")
    while True:
        if enter == "1":
            moud.output_write_blake_2s()
            choose_end()
            break

        elif enter == "2":
            moud.hashing_blake_2s()
            choose_end()
            break

        elif enter == "0":
            des.print_blake_2s()
            choose_blake_2s()
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")    





def choose():
    start()
    print(f"{Aqua}Choose hash type{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}01{BYellow}]{Aqua}- MD5      {BYellow}[{Aqua}08{BYellow}]{Aqua}- SHA3-256")
    print(f"{BYellow}[{Aqua}02{BYellow}]{Aqua}- SHA-1    {BYellow}[{Aqua}09{BYellow}]{Aqua}- SHA3-384")
    print(f"{BYellow}[{Aqua}03{BYellow}]{Aqua}- SHA-224  {BYellow}[{Aqua}10{BYellow}]{Aqua}- SHA3-512")
    print(f"{BYellow}[{Aqua}04{BYellow}]{Aqua}- SHA-256  {BYellow}[{Aqua}11{BYellow}]{Aqua}- BLAKE-2B")
    print(f"{BYellow}[{Aqua}05{BYellow}]{Aqua}- SHA-384  {BYellow}[{Aqua}12{BYellow}]{Aqua}- BLAKE-2S")
    print(f"{BYellow}[{Aqua}06{BYellow}]{Aqua}- SHA-512  {BYellow}[{Aqua}13{BYellow}]{Aqua}- How to use?")
    print(f"{BYellow}[{Aqua}07{BYellow}]{Aqua}- SHA3-224 {BYellow}[{BRed}00{BYellow}]{BRed}- Exit")
    print(" ")
    
    enter = input(f"{BYellow}${Aqua}>{Aqua} ")

    while True:

        if enter == "1":
            des.print_md5()
            choose_md5()
            break

        elif enter == "2":
            des.print_sha1()
            choose_sha1()
            break 
        
        elif enter == "3":
            des.print_sha224()
            choose_sha224()
            break
            
        elif enter == "4":
            des.print_sha256()
            choose_sha256()
            break

        elif enter == "5":
            des.print_sha384()
            choose_sha384()
            break

        elif enter == "6":
            des.print_sha512()
            choose_sha512()
            break

        elif enter == "7":
            des.print_sha3_224()
            choose_sha3_224()
            break

        elif enter == "8":
            des.print_sha3_256()
            choose_sha3_256()
            break

        elif enter == "9":
            des.print_sha3_384()
            choose_sha3_384()
            break

        elif enter == "10":
            des.print_sha3_512()
            choose_sha3_512()
            break

        elif enter == "11":
            des.print_blake_2b()
            choose_blake_2b()
            break

        elif enter == "12":
            des.print_blake_2s()
            choose_blake_2s()
            break

        elif enter == "13":
            how_to_use()
            break

        elif enter == "01":
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Try 1")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")

        elif enter == "02":
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Try 2")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")

        elif enter == "03":
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Try 3")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")

        elif enter == "04":
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Try 4")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")
        
        elif enter == "05":
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Try 5")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")

        elif enter == "06":
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Try 6")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")

        elif enter == "07":
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Try 7")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")

        elif enter == "08":
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Try 8")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")

        elif enter == "09":
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Try 9")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")

        elif enter == "00":
            start()
            sleep(0.5)
            sys.exit()
            break

        else:
            print(f"{BYellow}[{BRed}!{BYellow}]{BRed} Wrong choose")
            enter = input(f"{BYellow}${Aqua}>{Aqua} ")


def how_to_use():
    start()
    h = f'''
{BYellow}Use{Aqua}:

    Include your words inside words.txt 
    and choose from the main menu the types of hashes you want.


{BYellow}Options{Aqua}:

    {BYellow}List{Aqua}:
	This option enables you to choose how your hashes are saved.


    {BYellow}hash:word{Aqua}:
	   save word and hash (word:hash).

    {BYellow}hash{Aqua}:
	save the hashs only.


    {BYellow}single word{Aqua}:
	It enables you to enter a word and 
        get a hash without returning to a specific list.
    '''

    print(h)

    choose_end()


choose()

        