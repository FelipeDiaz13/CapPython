class Animales:
    """  def __init__(self, nombre, edad, color) -> None:
        self.nombre = nombre
        self.edad = edad
        self.color = color"""

    def gatos(self,nombre, edad, color):
        print(f"El nombre es: {nombre}")
        print(f"La edad es: {edad}")
        print(f"El color es: {color}")

    def perros(nombre, edad, color):
        print(f"El nombre es: {nombre}")
        print(f"La edad es: {edad}")
        print(f"El color es: {color}")   



Dolly = Animales.perros(
    nombre="Dolly",
    edad="5 Años",
    color="Pimienta"
)

Michi = Animales()
Michi.gatos(
    nombre="Michi",
    edad="4 Años",
    color="Naranja"
)

