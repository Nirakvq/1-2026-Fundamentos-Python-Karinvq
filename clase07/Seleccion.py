class Seleccion:
    def __init__(self, pais, confederacion):
        self.pais = pais
        self.confederacion = confederacion
        self.jugadores = []     # los corchetes sirven para almacenar multiples lista con n jugadores

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)   # el append sirve para agregar un nuevo jugador a la lista de jugadores

    def eliminar_jugador(self, jugador):
        for jugador_en_lista in self.jugadores:
            if jugador_en_lista == jugador:
                self.jugadores.remove(jugador_en_lista)  
                break   

pais = input("Ingrese el nombre del pais: ")
confederacion = input("Ingrese la confederación : ")
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

print
