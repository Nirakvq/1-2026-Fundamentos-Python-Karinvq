from Seleccion import Seleccion 

pais = input("Ingrese el nombre del pais: ")
confederacion = input("Ingrese la confederación ")
selecion = Seleccion(pais, confederacion)
Argentina = Seleccion("Argentina", "CONMEBOL")
Brasil = Seleccion("Brasil", "CONMEBOL")
España = Seleccion("España", "UEFA")        

Argentina.agregar_jugador("Lionel Messi")
Brasil.agregar_jugador("Neymar")
España.agregar_jugador("Lamine Yamal")
Argentina.agregar_jugador("Angel Di Maria")
Argentina.eliminar_jugador("Angel Di Maria")
print(Argentina.jugadores)
print(Brasil.jugadores)
print(España.jugadores)

jugador = input("Ingrese el nombre del jugador a eliminar: ")
selecion:agregar_jugador(jugador)