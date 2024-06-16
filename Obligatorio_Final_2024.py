#Obligatorio 2024 - Introducción a la Programación I / Dorrego,Rivas

from os import system
system("cls")

from datetime import datetime,date

import pickle as pickle

#Definición de estructuras
lista_clientes = [
    {"codigo": "1234","nombre": "Juan Gomez","direccion": "Av Brasil",
     "email": "juan.gomez@gmail.com","telefono": "099123456",
     "fecha_registro": date(2021, 2, 12)},
    {"codigo": "5678","nombre": "Ana Pérez","direccion": "Av Italia 5678",
     "email": "ana.perez@gmail.com","telefono": "099654321",
     "fecha_registro": date(2023, 5, 10)}
    ]
lista_menus = [
    {"codigo": "3333","tipo": "Premium","nombre": "Menú 1","platos": 
     [{"nombre": "Lasaña", "descripcion": "Carne y verduras", "precio": 350},{"nombre": "Ravioles", "descripcion": "Ricota", "precio": 290}],"precio_total": 900},
    {"codigo": "4444","tipo": "Regular","nombre": "Menú 2","platos": 
     [{"nombre": "Pollo", "descripcion": "Con papas", "precio": 200},{"nombre": "Ensalada", "descripcion": "Mixta", "precio": 100}],"precio_total": 300}
    ]
lista_eventos = [
    {"codigo": "9977", "cliente": lista_clientes[0], "menu": lista_menus[0], 
     "cantidad_invitados": 40, "fecha_evento": date(2024, 9, 23), 
     "hora_inicio": "19:00", "hora_fin": "23:00", "ubicacion": "Salón A1"},
    {"codigo": "9988", "cliente": lista_clientes[1], "menu": lista_menus[1], 
     "cantidad_invitados": 60, "fecha_evento": date(2024, 10, 12), 
     "hora_inicio": "20:00", "hora_fin": "22:30", "ubicacion": "Salón A2"}
    ]

#Persistencia de datos mediante serialización binaria
datos = [lista_clientes, lista_menus, lista_eventos]
archivo_salida = open("datos.bin", "wb")
pickle.dump(datos, archivo_salida)

archivo_salida.close()
archivo_entrante = open("datos.bin", "rb")
datos = pickle.load(archivo_entrante)
archivo_entrante.close()

def mostrar_menu():
        #Despliega el menú de opciones
        print("Menú")
        print("1. Registrar cliente")
        print("2. Registrar evento")
        print("3. Registrar menú")
        print("4. Mostrar cliente con más eventos")
        print("5. Total facturado por rango de fechas")
        print("6. Obtener menús con un platillo")
        print("7. Obtener eventos con un platillo")
        print("8. Mostrar eventos con menús Premium por asistentes")
        print("0. Salir")

def seleccionar_opcion():
    #Permite seleccionar una opción en el menú
    opcion = int(input("Ingrese una opción: "))
    while opcion not in [0,1,2,3,4,5,6,7,8]: #Mientras no se digite una opción dentro la lista no sigue el proceso
        print("La opción ingresada no es válida.")
        opcion = int(input("Seleccione otra opción: "))
    return opcion

def validar_codigo(codigo, longitud):
    #Hasta que el usuario no ingrese la cantidad adecuada de dígitos que el programa pide, no seguirá corriendo
    while len(codigo) != longitud:
        print(f"Error. Usted ingresó un número que no contiene {longitud} dígitos.")
        codigo = input(f"Ingrese un código identificador válido de {longitud} dígitos: ")
    return codigo

def solicitar_fecha(titulo):
    print(titulo)
    #Solicita al usuario ingresar el día, el mes y el año
    dia = int(input("Ingrese el día (1-31): "))
    mes = int(input("Ingrese el mes (1-12): "))
    anio = int(input("Ingrese el año (ej. 2024): "))
    fecha = date(anio,mes,dia)
    return fecha

def mostrar_cliente():
    print("Lista de clientes registrados")
    #Imprime los clientes que se encuentran en la lista
    for cliente in lista_clientes:
        print("Código identificador:",cliente["codigo"],"--- Nombre:",cliente["nombre"],"--- Dirección:",cliente["direccion"],"--- Correo electrónico:",cliente["email"],"--- Número de teléfono:",cliente["telefono"],"--- Fecha de registro:",cliente["fecha_registro"])

def buscar_cliente(codigo_identificador):
    #Compara el código identificador del cliente con el código que tenemos en nuestra base
    for cliente in lista_clientes:
        if cliente["codigo"] == codigo_identificador:
            return cliente #Si encuentra una coincidencia, retorna el diccionario del cliente (toda su información)
    return None #Si no encuentra ninguna coincidencia, retorna None y podremos registrar al cliente adecuadamente

def registrar_cliente():
    while True:
        codigo_identificador = validar_codigo(input("Ingrese el código identificador del cliente (4 dígitos): "), 4)
        #Comprueba si existe algún cliente con el código identificador ingresado por el usuario
        if buscar_cliente(codigo_identificador) is not None: #Si la función buscar_cliente no es None, ya existe un cliente con ese código identificador
            print("Error. Ya existe un cliente registrado con ese código identificador.")
        else:
            nombre_completo = input("Ingrese nombre y apellido del cliente: ") #No se utiliza str.capitalize dado que son dos parámetros que recibe la variable con un espacio en medio
            direccion = str.capitalize(input("Ingrese la dirección del cliente: "))
            correo = input("Ingrese el correo electrónico del cliente: ")
            while "@" not in correo:
                print("Correo electrónico inválido. Por favor, ingrese un correo válido que contenga @" )
                correo = input("Ingrese el correo electrónico del cliente: ")
            numero_telefono = input("Ingrese el numero de teléfono del cliente: ")
            fecha_registro = date.today()
            nuevo_cliente = {"codigo": codigo_identificador, "nombre": nombre_completo, "direccion": direccion, "email": correo, "telefono": numero_telefono, "fecha_registro": fecha_registro}
            lista_clientes.append(nuevo_cliente) #Se agrega al nuevo cliente dentro de lista_clientes en el último lugar
            print("El cliente se agregó a la lista de manera exitosa.")
            mostrar_cliente()
            break #Finaliza el bucle while, terminando el proceso de registro del cliente

def mostrar_evento():
    print("Lista de eventos registrados")
    #Imprime los eventos que se encuentran en la lista
    for evento in lista_eventos:
        print("Código identificador:",evento["codigo"],"--- Cliente:",evento["cliente"]["nombre"],"--- Menú:",evento["menu"]["nombre"],"--- Cantidad de personas:",evento["cantidad_invitados"],"--- Fecha del evento:",evento["fecha_evento"],"--- Hora de inicio:",evento["hora_inicio"], "--- Hora de finalización:",evento["hora_fin"],"--- Ubicación:",evento["ubicacion"])

def buscar_evento(codigo_evento):
    #Compara el código identificador del evento con el código que tenemos en nuestra base
    for evento in lista_eventos:
        if evento["codigo"] == codigo_evento:
            return evento #Si encuentra una coincidencia, retorna el diccionario del evento (toda su información)
    return None #Si no encuentra ninguna coincidencia, retorna None

def buscar_menu(codigo_menu):
    #Compara el código identificador del menú con el código que tenemos en nuestra base
    for menu in lista_menus:
        if menu["codigo"] == codigo_menu:
            return menu #Si encuentra una coincidencia, retorna el diccionario del menú (toda su información)
    return None #Si no encuentra ninguna coincidencia, retorna None

def registrar_evento():
    while True:
        codigo_evento = validar_codigo(input("Ingrese el código identificador del evento (4 dígitos): "), 4)
        #Comprueba si existe algún evento con el código identificador ingresado por el usuario
        if buscar_evento(codigo_evento) is not None: #Si la función buscar_evento no es None, ya existe un evento con ese código identificador
            print("Error. Ya existe un evento registrado con ese código identificador.")
        else:
            codigo_cliente = input("Ingrese el código identificador del cliente: ")
            cliente = buscar_cliente(codigo_cliente)
            if cliente is None:
                print("Error. No existe un cliente con ese código identificador.")
                continue #Reinicia el bucle para intentar nuevamente con otro cliente
            print("El cliente se encuentra en nuestra base de datos.")
            codigo_menu = input("Ingrese el código identificador del menú: ")
            menu = buscar_menu(codigo_menu) #Comprueba si existe algún menú con el código identificador proporcionado por el usuario
            if menu is None:
                 print("Error. No existe un menú con ese código identificador.")
                 continue #Reinicia el bucle para intentar nuevamente con otro menú
            print("El menú se encuentra en nuestra base de datos.")
            cantidad_personas = int(input("Ingrese la cantidad de personas que asistirán al evento: "))
            fecha_evento = solicitar_fecha("Ingrese la fecha del evento: ")
            fecha_evento_sin_segundos = fecha_evento.strftime('%Y-%m-%d') #strftime sirve para que no me imprima los segundos en la consola (ChatGPT)
            hora_inicio = input("Ingrese la hora de inicio del evento (hh:mm): ")
            hora_fin = input("Ingrese la hora de finalización del evento (hh:mm): ")
            ubicacion = input("Ingrese la ubicación del evento: ")
            fecha_registro_cliente = cliente["fecha_registro"]  
            diferencia_dias = (date.today() - fecha_registro_cliente).days #Calcula la diferencia en días
            precio = menu["precio_total"] * cantidad_personas
            descuento = 0 #Inicializamos nuestra variable descuento
            if diferencia_dias > 730: #Si la diferencia de días es mayor a 730 días (2 años) se aplica el descuento del 10%
                descuento = precio * 0.1
                precio = precio - descuento
                print("Usted accedió a un descuento del 10% por su antigüedad.")
            nuevo_evento = {"codigo": codigo_evento, "cliente": cliente, "menu": menu, "cantidad_invitados": cantidad_personas, "fecha_evento": fecha_evento_sin_segundos, "hora_inicio": hora_inicio, "hora_fin": hora_fin, "ubicacion": ubicacion}
            lista_eventos.append(nuevo_evento) #Se agrega el nuevo evento dentro de lista_eventos en el último lugar
            print("El evento se agregó a la lista de manera exitosa.")
            mostrar_evento()
            break #Finaliza el bucle while, terminando el proceso de registro del evento

def mostrar_menus():
    print("Lista de menús registrados")
    # Imprime los menús que se encuentran en la lista
    for menu in lista_menus:
        print(f"Código identificador: {menu['codigo']} --- Tipo del cliente: {menu['tipo']} --- Nombre del menú: {menu['nombre']} --- Lista de platillos:")
        for plato in menu['platos']:
            print(f"  - Nombre del platillo: {plato['nombre']}, Descripción: {plato['descripcion']}, Precio: {plato['precio']}")
        print(f"--- Precio total: {menu['precio_total']}")

def registrar_menu():
    while True:
        # Comprueba si existe algún menú con el código identificador ingresado por el usuario
        codigo_menu = validar_codigo(input("Ingrese el código identificador del menú (4 dígitos): "), 4)
        if buscar_menu(codigo_menu) is not None:  # Si la función buscar_menu no es None, ya existe un menú con ese código identificador
            print("Error. Ya existe un menú registrado con ese código identificador.")
            continue  # Reinicia el bucle para intentar nuevamente con otro código de menú
        else:
            tipo_cliente = input("Ingrese el tipo de cliente (Premium / Regular): ")
            nombre_menu = input("Ingrese el nombre del menú: ")
            lista_platillos = []  # Inicializamos nueva lista de platillos
            while True:
                nombre_platillo = input("Ingrese el nombre del platillo: ")
                descripcion_platillo = input("Ingrese la descripción del platillo: ")
                precio_platillo = float(input("Ingrese el precio del platillo: "))
                lista_platillos.append({"nombre": nombre_platillo, "descripcion": descripcion_platillo, "precio": precio_platillo})
                agregar_otro = input("¿Desea agregar otro platillo? (s/n): ")
                if agregar_otro != 's':
                    break  # Si no se desea agregar otro platillo, se sale del bucle while
            precio_por_persona = float(input("Ingrese el precio por persona: "))
            nuevo_menu = {"codigo": codigo_menu, "tipo": tipo_cliente, "nombre": nombre_menu, "platos": lista_platillos, "precio_total": precio_por_persona}
            lista_menus.append(nuevo_menu)  # Se agrega el nuevo menú dentro de lista_menu en el último lugar
            print("El menú se agregó a la lista de manera exitosa.")
            mostrar_menus()
            break  # Finaliza el bucle while, terminando el proceso de registro del menú

def cliente_con_mas_eventos():
    suma_eventos = {} #Inicializamos la variable que va a contabilizar los eventos por cliente
    for evento in lista_eventos:
        cliente = evento["cliente"]  #Accedemos a la información del cliente desde el evento
        codigo_cliente = cliente["codigo"] #Traemos el código identificador del cliente
        if codigo_cliente in suma_eventos:
            suma_eventos[codigo_cliente] = suma_eventos[codigo_cliente] + 1 #Sumamos uno si el cliente se encuentra en el diccionario
        else:
            suma_eventos[codigo_cliente] = 1 #Si el cliente no se encuentra en el diccionario, le inicializamos
    max_eventos = 0
    clientes_con_mas_eventos = None
    #Recorre la lista para encontrar al cliente con más eventos
    for codigo_cliente in suma_eventos:
        if suma_eventos[codigo_cliente] > max_eventos:
            max_eventos = suma_eventos[codigo_cliente]
            clientes_con_mas_eventos = codigo_cliente
    #Buscamos el cliente en lista_clientes
    cliente = buscar_cliente(clientes_con_mas_eventos)
    print(f"El cliente con más eventos es: {cliente['nombre']}")
    print(f"Código identificador: {cliente['codigo']} --- Dirección: {cliente['direccion']} --- Correo electrónico: {cliente['email']} --- Número de teléfono: {cliente['telefono']} --- Fecha de registro: {cliente['fecha_registro']}")
    print(f"La cantidad de eventos que acumula son: {max_eventos}")

def total_facturado_por_rango_fecha():
    fecha_inicio = solicitar_fecha("Ingrese la fecha inicial del periodo a revisar: ")
    fecha_termino = solicitar_fecha("Ingrese la fecha final del periodo a revisar: ")
    if fecha_inicio <= fecha_termino:
        costo_total = 0
        for evento in lista_eventos:
            fecha_evento = evento["fecha_evento"]
            # Verifica si la fecha del evento se encuentra dentro del rango especificado
            if fecha_inicio <= fecha_evento <= fecha_termino:
                # Calcula el costo del evento
                menu_precio = evento["menu"]["precio_total"]
                invitados = evento["cantidad_invitados"]
                costo_evento = menu_precio * invitados
                costo_total += costo_evento
        print(f"El total facturado en el periodo indicado es de: ${costo_total}")  # Imprime el total facturado en el período que el usuario indicó
    else:
        print("Fecha de término es previa a fecha de inicio")  # Muestra un mensaje de error si la fecha de término es anterior a la fecha de inicio
 
def menu_con_un_platillo():
    platillo = input("Ingrese el nombre del platillo: ")
    menus_platillo = []  # Lista para almacenar los nombres de los menús que contienen el platillo
    for menu in lista_menus:
        for plato in menu["platos"]:
            # Si el nombre del platillo coincide con el que el usuario ingresó, agrega el nombre del menú a la lista
            if plato["nombre"] == platillo:
                menus_platillo.append(menu["nombre"])
                break
    # Verifica si existen menús con el platillo
    if not menus_platillo:
        print("El platillo que ingresaste no existe en ningún menú registrado.")
    else:
        print("El platillo que ingresaste se encuentra en los siguientes menús:")
        #Recorremos menus_platillo para que la salida sea mas legible y sin corchetes
        for nombre_menu in menus_platillo:
            print(nombre_menu)

def evento_con_un_platillo():
    platillo = input("Ingrese el nombre del platillo: ")
    menus_platillo = []  #Lista para almacenar los nombres de los menús que contienen el platillo
    for menu in lista_menus:
        for plato in menu["platos"]:
            # Si el nombre del platillo coincide con el que el usuario ingresó, agrega el nombre del menú a la lista
            if plato["nombre"] == platillo:
                menus_platillo.append(menu["nombre"])
                break
    # Verifica si existen menús con el platillo
    if not menus_platillo:
        print("El platillo que ingresaste no existe en ningún evento registrado.")
    else:
        lista_eventos_platillo = []  # Esta lista nos almacenará los códigos de los eventos que contienen el platillo
        for evento in lista_eventos:
            # Verifica si el menú del evento está en la lista de menús con el platillo
            if evento["menu"]["nombre"] in menus_platillo:
                lista_eventos_platillo.append(evento["codigo"])
        # Verifica si se encontraron eventos con el platillo
        if not lista_eventos_platillo:
            print("No hay eventos con ese platillo en alguno de sus menús.")
        else:
            print("El platillo solicitado se encuentra en los menús de los siguientes eventos:")
            #Recorremos lista_eventos_platillo para que la salida sea mas legible y sin corchetes
            for codigo_evento in lista_eventos_platillo:
                print(codigo_evento)

def menu_premium_por_asistente():
    cantidad_personas = int(input("Ingrese la cantidad de personas que asistirán al evento: "))
    lista_eventos_personas = []  # Esta lista nos almacenará los códigos de los eventos
    for evento in lista_eventos:
        # Verifica si el menú es premium y la cantidad de invitados es mayor a la dada
        if evento["menu"]["tipo"] == "Premium":
            if evento["cantidad_invitados"] > cantidad_personas:
                lista_eventos_personas.append(evento["codigo"])
    # Verifica si se encontraron eventos que cumplen con los criterios    
    if not lista_eventos_personas:
        print("No existen eventos con menús Premium registrados que la cantidad de personas sea mayor que la dada.")
    else:
        print("Los siguientes eventos cuentan con menús Premium y con una cantidad de asistentes que superó a la cantidad dada:")
        #Recorremos lista_eventos_personas para que la salida sea mas legible y sin corchetes
        for codigo_evento in lista_eventos_personas:
            print(codigo_evento)    

mostrar_menu()
opcion = seleccionar_opcion()

while opcion != 0:
    if opcion == 1:
        registrar_cliente()

    elif opcion == 2:
        registrar_evento()

    elif opcion == 3:
        registrar_menu()

    elif opcion == 4:
        cliente_con_mas_eventos()

    elif opcion == 5:
        total_facturado_por_rango_fecha()

    elif opcion == 6:
        menu_con_un_platillo()

    elif opcion == 7:
        evento_con_un_platillo()

    elif opcion == 8:
        menu_premium_por_asistente()

    input("Presione enter para continuar...")
    mostrar_menu()
    opcion = int(input("Ingrese una opción: "))