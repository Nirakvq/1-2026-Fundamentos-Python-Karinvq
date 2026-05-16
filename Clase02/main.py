 #inicialisar variables
print("hola mundo")
nombre = "Ithan"

  #solicitar al usario su edad
edad = int(input("cual es tu edad"))
anno_de_nacimiento= 2026 - edad
print(anno_de_nacimiento)

 #calcular si es mayor de edad  
mayor_de_edad = edad >= 18
print(mayor_de_edad)

 #saber si soy yo 
no_soy_yo = not nombre == "Karin" and edad == 17
soy_yo = nombre == "Ithan" and edad == 16
quizas_soy_yo = nombre == "Ithan" or edad == 18
print(no_soy_yo)
print(soy_yo)
print(quizas_soy_yo) 