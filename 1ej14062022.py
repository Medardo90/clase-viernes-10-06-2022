# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:59:32 2022

@author: Patricio Haro
"""
#conjuncion operador logico and

print("conjuncion (and)")
num1=int(input("esctiba un numero mayor que a 2 y menor a 5: "))
if num1>2 and num1<5:
    print("el numero ", num1, "cumple con la condicion \n")
else:
   print("el numero ", num1, "no cumple con la condicion\n")
   
   
   #opeerador logico or 
print("disyuncion (or)") 
palabra=input("para cumplir con la condicioon escribe 'si' o 'yes': ")
if palabra == "si" or palabra == "yes":
    print("la condicion se ha cumplido\n:")
else:
    print("la condicion no se ha cumplido: ")
    
    #negacion not
print("negacion (not)")
num1= int(input("introduce un muemro igual a 5:"))
if not num1==5:
    print("\n el numero es diferente a 5 y si cumple la condicon")
else:
    print("\n el numero es igual a 5y no cumple la condicion")
    
