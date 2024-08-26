from usuarios.Usuarios import Usuario

"""
    Seccionar todo el codigo (Diferentes clases)
"""
#Seccion de Variables
list_Usuarios = ['Oscar', 'Raul', 2,4]
try:
    objeto_usuario = Usuario()
    list_Usuarios.append(objeto_usuario)
except Exception as NoSeEncontro:
    print("La clase no se encontro")

while True:
    print("Plataforma de usuarios")
    print("1.- Agrega Usuarios")
    print("2.- Elimina Usuarios")
    print("3.- Actualiza Usuarios")
    print("4.- Mostrar Datos ")
    print("5.- Salir")

    opciones_menu = input(" Introduce una opción ")


    if int(opciones_menu) == 1:
        print("Agregar Usuarios")
        in_usuario =input("Intoduce El Nombre")
        list_Usuarios.append(objeto_usuario.mostrar_nombre(in_nombre = in_usuario))
        print(list_Usuarios)


    elif int(opciones_menu) == 2:
        print("Eliminar Usuarios")
        print(list_Usuarios)
        try:
            nombre = input('¿Que usuario deseas eliminar?')
            list_Usuarios.remove(nombre)
            list_Usuarios.sort()
            print(list_Usuarios)
        except Exception as Usuario_no_encontrado:
            print("Este usuario no se encontro")

    elif int(opciones_menu) == 3:
        print("Actualizar Usuarios")
        print(list_Usuarios)
        valor_id = input("¿Que valor deseas actualizar?")
        valor_id_index = list_Usuarios.index(valor_id)
        nombre_actualizado = input("Cual es el nuevo nombre?")
        list_Usuarios.insert(valor_id_index, nombre_actualizado)
        list_Usuarios.remove(valor_id)
        


    elif int(opciones_menu) == 4:
        print("Mostrar Datos ")
        print(list_Usuarios)
        print(list_Usuarios.sort())


    else:
        print("Gracias")


"""  inp = '1'
    match inp:
        case '1':
            print("Elejiste La Opcion 1")
        case '2':
            print("Elejiste La Opcion ")"""

