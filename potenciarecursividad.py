def potencia(base,exp):
  if exp==0:
    return 0
  if exp==1:
    return base
  else: 
    return base * potencia(base,exp-1)
b=int(input("Introduzca la base: "))
e=int(input("Introduzca el exponente: "))
print(potencia(b,e))