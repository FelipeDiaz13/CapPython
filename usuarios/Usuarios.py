from RolesUsuarios import TipoUsuario

# Clase usuario con herencia de tipo usuario
class Usuario(TipoUsuario):
    # Funcion que muestra el nombre
    def mostrar_nombre(self,in_nombre):
        out_nombre = in_nombre
        return in_nombre
    # Funcion que muestra el apellido paterno
    def mostrar_app(self, in_app):
        """Almacena variables de entrada hacia la de la salida """
        out_app = in_app
        return in_app
    # Funcion que muestra la edad
    def mostrar_edad(self, in_edad):
        out_edad = in_edad
        return in_edad
    
    def mostrar_rol(sef,in_roll):
        out_roll = in_roll
        return out_roll




"""Felipe = Usuario()
Oscar = Usuario()

print(Felipe.mostrar_nombre(in_nombre="Felipe"))
print(Oscar.mostrar_nombre(in_nombre="Oscar"))"""


