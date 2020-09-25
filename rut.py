print ("Adivinando el dígito verificador\n")
print ("*"*15, "\n")
uno = input ("Ingrese el primer dígito de su rut\n(Si su rut es menor a 10 millones, escriba 0)...\n")
dos = input ("Ingrese el segundo dígito de su rut...\n")
tres = input ("Ingrese el tercer dígito de su rut...\n")
cuatro = input ("Ingrese el cuarto dígito de su rut...\n")
cinco = input ("Ingrese el quinto dígito de su rut...\n")
seis = input ("Ingrese el sexto dígito de su rut...\n")
siete = input ("Ingrese el séptimo dígito de su rut...\n")
ocho = input ("Ingrese el octavo dígito de su rut...\n")
uno = int(uno)
dos = int(dos)
tres = int(tres)
cuatro = int(cuatro)
cinco = int(cinco)
seis = int(seis)
siete = int(siete)
ocho = int(ocho)
sumatotal= ((ocho)*2 + (siete)*3 + (seis)*4 + (cinco)*5 + (cuatro)*6 + (tres)* 7 + (dos)*2 + (uno)*3)#Suma de izq. a der. 
resto = sumatotal%11 
verificador = 11 - resto
print ("*"*15, "\n")
print ("El dígito verificador de su rut es:", verificador)

