import os, sys

name = raw_input(" nama lu :")
password = raw_input(" berapa kali lu coli: ")
if name == "Mr.3M0N27" and password == "bahagia":
   print " WELCOME "
   print " ini adalah untuk senang senang/ mengisi gabut:v"
   print " jawablah pertanyaan ini, untuk menghibur hatimu:v"
else:
   print "Salah kamvank, cobalagi tod:v"

def restart():
           ngulang = sys. executable
           os.execl(ngulang, ngulang, *sys.argv)
name = raw_input("Berapakah pacar saya?: ")
if name == "3":
   print "yaps betul" 
   print " apakah anda masih gabut?"
name = raw_input("jika masih gabut ketik (y)")
if name == "y":
   print "yuhuuuu, okehh jika anda masih gabut  ayo kita main permainan janda perawan, gadis bukan perawan"
   print " silahkan bermain"
else:
   print "salah kamvank , coba lagi..!"
   restart()

import random
import os, sys

#warna
G = "\033[32m";
O = "\033[33m";
B = "\033[36m";
R = "\033[31m";
W = "\033[0m";
P = "\033[35m";
print W+"created by Mr.3M0N27"
print P+"game gabut:v"
print B+"contatc me : 081779585663"
print R+"Pilihan :"
print G+"permainan janda, tapi jngn permainin perawan ea:) karena di mainin itu sakit vroh:v"
print O+"1. gadis bukan perawan"
print P+"2. perawan"
print R"3. janda"
def restart():
        ngulang = sys.executable
        os.execl(ngulang, ngulang, *sys.argv)
def permainan():
    kamu = int(input("Masukan Pilihanmu: " ))
    kom = random.choice(["gadis bukan perawan", "perawan" , "janda"])
    if kamu == 1:
        print G+"kamu    : gadis bukan perawan"
        print("komputer  :", kom)
        if kom =="gadis bukan perawan":
            print B+"\tDraw"
        if kom =="perawan":
            print G+"\tlu menang"
        if kom =="janda":
            print R+"\tlu kalah goblok:v"
    if kamu == 2:
        print R+"kamu     : perawan"
        print("komputer   :", kom)
        if kom =="gadis bukan perawan":
            print R+"\tlu kalah goblok:v"
        if kom =="perawan":
            print B+"\tDraw"
        if kom =="janda":
            print G+"\tlu menang"
    if kamu == 3:
        print G+"kamu      : janda"
        print("komputer   :", kom)
        if kom =="gadis bukan perawan":
            print G+"\tlu menang"
        if kom =="perawan":
            print R+"\tlu kalah goblok:v"
        if kom =="janda":
            print R+"\tDraw"
    if kamu >=4:
        print R+"Pilihamu salah kamvank:v"
        restart()
permainan()
restart()
try:
         permainan()
except KeyboardInterrupt:
       os.system ('clear')
