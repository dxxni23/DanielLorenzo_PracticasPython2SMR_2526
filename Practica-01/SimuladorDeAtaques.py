############ PRACTICA 01 ############

#---Explicación---#

# Eres parte del equipo de ciberseguridad de una empresa. 
# Tu misión es simular un ataque de fuerza bruta muy básico para 
# comprobar si las contraseñas de los usuarios son seguras o no. 

#---Cosas Que Hacer---#

# 1. Crea una lista de usuarios, donde cada usuario es una lista con 
#   el nombre y su contraseña (ambos str). Ejemplo:["ana", "abc123"] 
#   Esta lista la pedirás por teclado al usuario. Cada vez que complete 
#   de poner un nombre y una contraseña le preguntarás:  ¿Quieres añadir 
#   un nuevo usuario? Si dice que si, le vuelves a pedir un nuevo usuario 
#   y una nueva contraseña. Si dice que no, para de pedirle usuarios. 
# 2. Genera una lista de contraseñas comunes (por ejemplo, ["1234", "password", 
#   "qwerty", "abc123", "hola"]). Esta lista ya la tienes en tu programa, es decir, 
#   la creas ya rellena, no hace falta que la pidas por teclado. 
# 3. Usa la librería random y un bucle while para simular varios intentos de 
#   ataque: o En cada intento, elige un usuario aleatorio. o Comprueba si la 
#   contraseña del usuario elegido aleatoriamente coincide con alguna de las 
#   contraseñas de las lista de contraseñas inseguras. o Si alguna contraseña 
#   coincide con la del usuario, muestra un mensaje indicando que el usuario fue 
#   vulnerado. Por ejemplo: El usuario Pepe fue vulnerado. Contraseña débil. 
# 4. El bucle while parará cuando el usuario diga que ya no quiere hacer más ataques 
#   aleatorios 
# 5. Dentro del while, usa un bucle for para comprobar las coincidencias. 
# 6. Usa lower() para comparar contraseñas sin importar mayúsculas o minúsculas.
# 7. Muestra al final un resumen con los usuarios vulnerados y los que resistieron 
#   el ataque. 

#---Solución---#

import random 
        #Listas#
Lista_de_usuario_y_contraseñas = []
Lista_de_contraseñas_comunes = ["1234", "password","qwerty", "abc123", "hola"]
usuarios_vulnerados = []
usuario_no_vulnerado = []
        #Variables#
usuario = ""
contraseña = ""
continuar = "si"
simulacion = "no"
usuariobueno = ""
usuariomalo = ""

        #Ejercicios#
print("---Pon tu Usuario y Contraseña---")

while  continuar== "si":
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    continuar = input("¿Quieres Poner Mas Usuarios? // si o no: ")
    Lista_de_usuario_y_contraseñas.append ([usuario,contraseña])

print("Número de Usuarios Guardados:", len(Lista_de_usuario_y_contraseñas))

simulacion = input("Quieres Hacer la simulación // si o no: ") 
while  simulacion == "si":
    usuarioconcontraseña_random = random.choice(Lista_de_usuario_y_contraseñas)
    print("usuario:", usuarioconcontraseña_random[0] , "/// contraseña:" , usuarioconcontraseña_random[1])
    contrasena_actual = usuarioconcontraseña_random[1].lower()
    vulnerado = False
    for contraseña_comun in Lista_de_contraseñas_comunes:
        if contrasena_actual == contraseña_comun:
            vulnerado = True
            break
    if vulnerado:
        print("La Contraseña es Vulnerable")
        usuarios_vulnerados.append(usuarioconcontraseña_random[0])
    else:
        print("La contraseña no es Vulnerable")
        usuario_no_vulnerado.append(usuarioconcontraseña_random[0])
    simulacion = input("Quieres Hacer otra simulación // si o no: ")
    
print("-----------RESUMEN-----------")
print("Usuarios Vulnerables: ",usuarios_vulnerados)
print("Usuarios No Vulnerables: ",usuario_no_vulnerado)