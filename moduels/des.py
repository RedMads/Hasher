import hashlib,os,time,sys
from time import sleep
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



def print_md5():
    start()
    print(f"{BYellow}[{Aqua}MD5{BYellow}]")
    print(" ")
    print(f"{Aqua}Chooose The process{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- List   {BYellow}[{Aqua}2{BYellow}]{Aqua}- Single word")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_sha1():
    start()
    print(f"{BYellow}[{Aqua}SHA-1{BYellow}]")
    print(" ")
    print(f"{Aqua}Chooose The process{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- List   {BYellow}[{Aqua}2{BYellow}]{Aqua}- Single word")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_sha224():
    start()
    print(f"{BYellow}[{Aqua}SHA-224{BYellow}]")
    print(" ")
    print(f"{Aqua}Chooose The process{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- List   {BYellow}[{Aqua}2{BYellow}]{Aqua}- Single word")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")




def print_sha256():
    start()
    print(f"{BYellow}[{Aqua}SHA-256{BYellow}]")
    print(" ")
    print(f"{Aqua}Chooose The process{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- List   {BYellow}[{Aqua}2{BYellow}]{Aqua}- Single word")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_sha384():
    start()
    print(f"{BYellow}[{Aqua}SHA-384{BYellow}]")
    print(" ")
    print(f"{Aqua}Chooose The process{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- List   {BYellow}[{Aqua}2{BYellow}]{Aqua}- Single word")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_sha512():
    start()
    print(f"{BYellow}[{Aqua}SHA-512{BYellow}]")
    print(" ")
    print(f"{Aqua}Chooose The process{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- List   {BYellow}[{Aqua}2{BYellow}]{Aqua}- Single word")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_sha3_224():
    start()
    print(f"{BYellow}[{Aqua}SHA3-224{BYellow}]")
    print(" ")
    print(f"{Aqua}Chooose The process{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- List   {BYellow}[{Aqua}2{BYellow}]{Aqua}- Single word")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_sha3_256():
    start()
    print(f"{BYellow}[{Aqua}SHA3-256{BYellow}]")
    print(" ")
    print(f"{Aqua}Chooose The process{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- List   {BYellow}[{Aqua}2{BYellow}]{Aqua}- Single word")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_sha3_384():
    start()
    print(f"{BYellow}[{Aqua}SHA3-384{BYellow}]")
    print(" ")
    print(f"{Aqua}Chooose The process{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- List   {BYellow}[{Aqua}2{BYellow}]{Aqua}- Single word")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_sha3_512():
    start()
    print(f"{BYellow}[{Aqua}SHA3-512{BYellow}]")
    print(" ")
    print(f"{Aqua}Chooose The process{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- List   {BYellow}[{Aqua}2{BYellow}]{Aqua}- Single word")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_blake_2b():
    start()
    print(f"{BYellow}[{Aqua}BLAKE-2B{BYellow}]")
    print(" ")
    print(f"{Aqua}Chooose The process{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- List   {BYellow}[{Aqua}2{BYellow}]{Aqua}- Single word")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_blake_2s():
    start()
    print(f"{BYellow}[{Aqua}BLAKE-2S{BYellow}]")
    print(" ")
    print(f"{Aqua}Chooose The process{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- List   {BYellow}[{Aqua}2{BYellow}]{Aqua}- Single word")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_type_write_md5():
    start()
    print(f"{BYellow}[{Aqua}MD5{BYellow}/{Aqua}List{BYellow}]")
    print(" ")
    print(f"{Aqua}Choose type of write in list{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- word:hash   {BYellow}[{Aqua}2{BYellow}]{Aqua}- hash only")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_type_write_sha1():
    start()
    print(f"{BYellow}[{Aqua}SHA-1{BYellow}/{Aqua}List{BYellow}]")
    print(" ")
    print(f"{Aqua}Choose type of write in list{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- word:hash   {BYellow}[{Aqua}2{BYellow}]{Aqua}- hash only")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_type_write_sha224():
    start()
    print(f"{BYellow}[{Aqua}SHA-224{BYellow}/{Aqua}List{BYellow}]")
    print(" ")
    print(f"{Aqua}Choose type of write in list{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- word:hash   {BYellow}[{Aqua}2{BYellow}]{Aqua}- hash only")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_type_write_sha256():
    start()
    print(f"{BYellow}[{Aqua}SHA-256{BYellow}/{Aqua}List{BYellow}]")
    print(" ")
    print(f"{Aqua}Choose type of write in list{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- word:hash   {BYellow}[{Aqua}2{BYellow}]{Aqua}- hash only")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_type_write_sha384():
    start()
    print(f"{BYellow}[{Aqua}SHA-384{BYellow}/{Aqua}List{BYellow}]")
    print(" ")
    print(f"{Aqua}Choose type of write in list{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- word:hash   {BYellow}[{Aqua}2{BYellow}]{Aqua}- hash only")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_type_write_sha512():
    start()
    print(f"{BYellow}[{Aqua}SHA-512{BYellow}/{Aqua}List{BYellow}]")
    print(" ")
    print(f"{Aqua}Choose type of write in list{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- word:hash   {BYellow}[{Aqua}2{BYellow}]{Aqua}- hash only")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_type_write_sha3_224():
    start()
    print(f"{BYellow}[{Aqua}SHA3-224{BYellow}/{Aqua}List{BYellow}]")
    print(" ")
    print(f"{Aqua}Choose type of write in list{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- word:hash   {BYellow}[{Aqua}2{BYellow}]{Aqua}- hash only")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_type_write_sha3_256():
    start()
    print(f"{BYellow}[{Aqua}SHA3-256{BYellow}/{Aqua}List{BYellow}]")
    print(" ")
    print(f"{Aqua}Choose type of write in list{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- word:hash   {BYellow}[{Aqua}2{BYellow}]{Aqua}- hash only")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_type_write_sha3_384():
    start()
    print(f"{BYellow}[{Aqua}SHA3-384{BYellow}/{Aqua}List{BYellow}]")
    print(" ")
    print(f"{Aqua}Choose type of write in list{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- word:hash   {BYellow}[{Aqua}2{BYellow}]{Aqua}- hash only")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_type_write_sha3_512():
    start()
    print(f"{BYellow}[{Aqua}SHA3-512{BYellow}/{Aqua}List{BYellow}]")
    print(" ")
    print(f"{Aqua}Choose type of write in list{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- word:hash   {BYellow}[{Aqua}2{BYellow}]{Aqua}- hash only")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_type_write_blake_2b():
    start()
    print(f"{BYellow}[{Aqua}BLAKE-2B{BYellow}/{Aqua}List{BYellow}]")
    print(" ")
    print(f"{Aqua}Choose type of write in list{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- word:hash   {BYellow}[{Aqua}2{BYellow}]{Aqua}- hash only")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")



def print_type_write_blake_2s():
    start()
    print(f"{BYellow}[{Aqua}BLAKE-2S{BYellow}/{Aqua}List{BYellow}]")
    print(" ")
    print(f"{Aqua}Choose type of write in list{BYellow}:")
    print(" ")
    print(f"{BYellow}[{Aqua}1{BYellow}]{Aqua}- word:hash   {BYellow}[{Aqua}2{BYellow}]{Aqua}- hash only")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back")
    print(" ")




def print_choose_end_again():
    print(" ")
    print(f"{BYellow}[{Aqua}0{BYellow}]{Aqua}- Back main menu  {BYellow}[{Aqua}1{BYellow}]{Aqua}- Again")
    print(" ")