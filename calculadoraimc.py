# Pide la cantidad de personas a las que se le calculara su IMC
personas = int(input( "Cuantas personas calcularan su IMC: "))

# Comenzamos un ciclo que se repetira hasta que queden 0 personas por calcular
while personas > 0:
    # Le asignamos el valor de texto vacio a la variable "nombre" para poder entrar al ciclo
    nombre = ""
    # Comenzamos un ciclo que se repetira hasta que se introduzca un valor a la variable "nombre"
    while nombre == "":
        # Le pedimos al usuario que introduzca su nombre
        nombre = input("Escriba su nombre: ")
        # Se realiza una condicion para comprobar si el usuario no dejo vacio el campo
        if nombre == "":
            # Si el campo quedo vacio, se imprime "Introduzca un nombre valido" y se repite el ciclo
            print("Introduzca un nombre valido")
    # Le asignamos el valor de texto vacio a la variable "apellidop" para poder entrar al ciclo
    apellidop = ""
    # Comenzamos un ciclo que se repetira hasta que se introduzca un valor a la variable "apellidop"
    while apellidop == "":
        # Le pedimos al usuario que introduzca su apellido paterno
        apellidop = input("Escriba su apellido paterno: ")
        # Se realiza una condicion para comprobar si el usuario no dejo vacio el campo
        if apellidop == "":
            # Si el campo quedo vacio, se imprime "Introduzca un apellido paterno valido" y se repite el ciclo
            print("Introduzca un apellido paterno valido")
    # Le asignamos el valor de texto vacio a la variable "apellidom" para poder entrar al ciclo
    apellidom = ""
    # Comenzamos un ciclo que se repetira hasta que se introduzca un valor a la variable "apellidom"
    while apellidom == "":
        # Le pedimos al usuario que introduzca su apellido materno
        apellidom = input("Escriba su apellido materno: ")
        # Se realiza una condicion para comprobar si el usuario no dejo vacio el campo
        if apellidom == "":
            # Si el campo quedo vacio, se imprime "Introduzca un apellido materno valido" y se repite el ciclo
            print("Introduzca un apellido materno valido")
    # Le asignamos el valor de texto vacio a la variable "edad" para poder entrar al ciclo
    edad = ""
    # Comenzamos un ciclo que se repetira hasta que se introduzca un valor a la variable "edad"
    while edad == "":
        # Le pedimos al usuario que introduzca su edad en años
        edad = (input("Escriba su edad en años: "))
        #Se realiza una condicion para comprobar que lo que se inserto en el campo sean solo digitos mediante la funcion "isdigit()""
        if not edad.isdigit():
            # Si la condicion se cumple (es decir, no son solo digitos), manda el mensaje "Introduzca una edad valida"
            print("Introduzca una edad valida")
            # Se reasigna el valor de texto vacio a la variable "edad" para volver al ciclo
            edad = ""
        # Si la condicion no se cumple (es decir, si son solo digitos), sale de la condicion if
        else:
            # Cambiamos el valor del tipo de la variable "edad" de datos de cadena de texto a datos de numero entero
            edad = int(edad)
    # Le asignamos el valor de texto vacio a la variable "estatura" para poder entrar al ciclo
    estatura = ""
    # Comenzamos un ciclo que se repetira hasta que se introduzca un valor a la variable "estatura"
    while estatura == "":
        # Le pedimos al usuario que introduzca su estatura en metros
        estatura = (input ("Escriba su estatura en metros: "))
        # Creamos una nueva variable llama "nestatura" que contendra los datos de la variable "estatura", pero remplazando todos los puntos (".") que contenga por texto vacio ("") con la funcion ".replace()"
        nestatura = estatura.replace(".", "")
        #Se realiza una condicion para comprobar que lo que se inserto en el campo (sin puntos, y haciendo la comprobacion con la nueva variable "nestatura") sean solo digitos mediante la funcion "isdigit()""
        if not nestatura.isdigit():
            # Si la condicion se cumple (es decir, no son solo digitos), manda el mensaje "Introduzca una edad valida"
            print("Introduzca una estatura valida")
            # Se reasigna el valor de texto vacio a la variable "estatura" para volver al ciclo
            estatura = ""
        # Si la condicion no se cumple (es decir, si son solo digitos), sale de la condicion if
        else:
            # Cambiamos el valor del tipo de la variable "estatura" de datos de cadena de texto a datos de numero flotante
            estatura = float(estatura)
            #Se realiza una condicion para comprobar que la variable "estatura" no sea mayor a 3, para evitar cantidades superiores a 3 metros por error al no poner el punto decimal
            if estatura >= 3:
                # Si la condicion se cumple, manda el mensaje "Introduzca una edad valida"
                print("Introduzca una estatura valida")
                # Se reasigna el valor de texto vacio a la variable "edad" para volver al ciclo
                estatura = ""
    # Le asignamos el valor de texto vacio a la variable "peso" para poder entrar al ciclo
    peso = ""
    # Comenzamos un ciclo que se repetira hasta que se introduzca un valor a la variable "peso"
    while peso == "":
        # Le pedimos al usuario que introduzca su peso en kilogramos
        peso = (input("Escriba su peso en kilogramos: "))
        # Creamos una nueva variable llama "npeso" que contendra los datos de la variable "peso", pero remplazando todos los puntos (".") que contenga por texto vacio ("") con la funcion ".replace()"
        npeso = peso.replace(".", "")
        #Se realiza una condicion para comprobar que lo que se inserto en el campo (sin puntos, y haciendo la comprobacion con la nueva variable "npeso") sean solo digitos mediante la funcion "isdigit()""
        if not npeso.isdigit():
            # Si la condicion se cumple (es decir, no son solo digitos), manda el mensaje "Introduzca un peso valida"
            print("Introduzca un peso valido")
            # Se reasigna el valor de texto vacio a la variable "peso" para volver al ciclo
            peso = ""
        # Si la condicion no se cumple (es decir, si son solo digitos), sale de la condicion if
        else:
            # Cambiamos el valor del tipo de la variable "peso" de datos de cadena de texto a datos de numero flotante
            peso = float(peso)
    
    # Se realiza el calculo del IMC con el peso sobre la estatura al cuadrado
    IMC = peso / estatura**2

    # Se imprimen los datos de manera presentable integrando diferentes funciones y formatos como:
    # ".title()": para que las primeras letras del texto sean mayusculas (en la variable "nombre"), esto porque la persona puede tener dos nombres
    # ".capitalize()": para que la primera letra de la primera palabra sea mayuscula (en las variables "apellidop" y "apellidom"), ya que cada apellido va por separado
    # ":.2f": para asignarle solo 2 decimales al numero (en este caso las variables "estatura" y "peso")
    # Y las dos impresiones van en cadenas de formato "f-strings" para poder integrar variables en la cadena de texto
    print(f"Hola, {nombre.title()} {apellidop.capitalize()} {apellidom.capitalize()}")
    print(f"De acuerdo a tus  {edad} años de edad, tus {estatura:.2f} metros de altura y {peso:.2f} kilos de peso")

    # Se realiza una condicion para comprobar que la variable "edad" sea menor a 18
    if(edad < 18):
        # Si la condicion se cumple, manda el mensaje "Y que eres menor de edad"
        print("Y que eres menor de edad")
    # Si la condicion no se cumple, sale de la condicion if
    else:
        # Si la condicion no se cumple, manda el mensaje "Y que eres mayor de edad"
        print("Y que eres mayor de edad")
    
    # imprime "Calculamos tu IMC en " concatenando el valor de la variable IMC en formato de cadena de texto
    print("Calculamos tu IMC en " + str(IMC) )

    # Se realiza una condicion para imprmir la categoria de peso en la que se encuentra la persona dependiendo del calculo del IMC
    if IMC >= 0 and IMC <= 15.99 :
        print ("Delgadez severa")
    elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Delgadez moderada")
    elif IMC >= 17.00 and IMC <= 18.49:
        print ("Delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Normal")
    elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print ("Obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.00:
        print ("Obesidad media")
    elif IMC >= 40.00:
        print ("Obesidad morbida")

    # Se hace un contador regresivo para ir restando las personas que ya han realizado su calculo hasta llegar a 0 y terminar el ciclo restandole a la variable "personas" uno y reasignando el valor a la misma variable
    personas = personas - 1

# Si la variable "personas" llega a 0 manda a un mensaje de despedida y sale del ciclo para finalizar el proceso
if personas == 0:
    print("Que tengas buen dia")