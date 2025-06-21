from personaje import Personaje
import random


print("¡Bienvenido a Gran Fantasía!")
nombre = input("Por favor indique nombre de su personaje:")

personaje = Personaje(nombre)

print(personaje.estado)

npc = Personaje()
prob = personaje.probabilidad(npc)
opcion = Personaje.mostrar_dialogo(prob)


while opcion == 1:
    resultado = "G" if random.uniform(0, 100) < prob else "P"
    if resultado == "G":
        print("""
¡Le has ganado al orco, felicidades!
¡Recibirás 50 puntos de experiencia!
""")
        personaje.estado = 50
        npc.estado = -30
    else:
        print("""
¡Oh no! ¡El orco te ha ganado!
¡Has perdido 30 puntos de experiencia!
""")
        personaje.estado = -30
        npc.estado = 50

    print(personaje.estado)
    print(npc.estado)


    prob = personaje.probabilidad(npc)
    opcion = Personaje.mostrar_dialogo(prob)


print("has huido del Orco!!!!")


        
        


