from Usuarios import Usuario

"""
    Seccionar todo el codigo (Diferentes clases)
"""
#Seccion de Variables
list_Usuarios = []
objeto_usuario = Usuario()

while True:
    print("Plataforma de usuarios")
    print("1.- Agrega Usuarios")
    print("2.- Elimina Usuarios")
    print("3.- Actualiza Usuarios")
    print("4.- Salir")

    opciones_menu = input(" Introduce una opción ")

    if int(opciones_menu) == 1:
        print("Agregar Usuarios")
        in_usuario =input("Intoduce El Nombre")
        list_Usuarios.append(objeto_usuario.mostrar_nombre(in_nombre = in_usuario))
        print(list_Usuarios)
    elif int(opciones_menu) == 2:
        print("Eliminar Usuarios")

    elif int(opciones_menu) == 3:
        print("Actualizar Usuarios")

    else:
        print("Gracias")


    inp = '1'
    match inp:
        case '1':
            print("Elejiste La Opcion 1")
        case '2':
            print("Elejiste La Opcion ")