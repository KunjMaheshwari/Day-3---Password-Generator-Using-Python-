#Password Generator using Python 
# Day 3

import random

Letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
Symbols = ["!","@","#","$","%","^","&","*","(",")","_","+","-","=","{","}","[","]","|",";",":","<",">","?","/"]
Numbers = [ "1","2","3","4","5","6","7","8","9","0"]

print ("Welcome to the PyPassword Generator!")
int_Letters = int (input("How many letters you want in your password? "))
int_Symbol = int (input("How many symbol you want in your Password? "))
int_Numbers = int (input("How many numbers you want to add in your password?"))

password = ""

for i in range(1,int_Letters+1):
    password = password + random.choice(Letter)
 
for i in range(1,int_Symbol+1):
    password = password + random.choice(Symbols)

for i in range(1,int_Numbers+1):
    password = password + random.choice(Numbers)
    
print(f"Here is your password: {password}")
    

