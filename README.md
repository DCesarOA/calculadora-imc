# Proyecto Calculadora de IMC

## *Pasos realizados para crear el Proyecto de Calculadora de IMC*

El primer paso para realizar el programa fue revisar el contenido del primer mes del Bootcamp.
Revisar las clases semanales para ver como se habian resuelto las dudas.
Tome como referencia el ejemplo mencionado en los pasos a seguir.
Avance lo mas que pude mediante lo recordado en las clases grabadas y las clases en vivo.
Volvi a revisar las clases para ver si alguna informacion ya mencionada me servia para solucionar algunas complicaciones que se me presentaron.
Use informacion de Internet para solucionar algunos problemas.
Le di formato a la informacion de salida con informacion del curso.

## *Mi programa tiene la siguiente estructura*


1.- Pide la cantidad de personas a las que se le calculara su IMC

2.- Comienza un ciclo que se repetira hasta que queden 0 personas por calcular

3.- Asigna el valor de texto vacio a la variable "nombre" para poder entrar al ciclo

4.- Comienza un ciclo que se repetira hasta que se introduzca un valor a la variable "nombre"

5.- Pide al usuario que introduzca su nombre

6.- Realiza una comprobacion para ver si el usuario no dejo vacio el campo

7.- Si el campo quedo vacio, se imprime "Introduzca un nombre valido" y se repite el ciclo

8.- Asigna el valor de texto vacio a la variable "apellidop" para poder entrar al ciclo

9.- Comienza un ciclo que se repetira hasta que se introduzca un valor a la variable "apellidop"

10.- Pide al usuario que introduzca su apellido paterno

11.- Realiza una comprobacion para ver si el usuario no dejo vacio el campo

12.- Si el campo quedo vacio, se imprime "Introduzca un apellido paterno valido" y se repite el ciclo

13.- Asigna el valor de texto vacio a la variable "apellidom" para poder entrar al ciclo

14.- Comienza un ciclo que se repetira hasta que se introduzca un valor a la variable "apellidom"

15.- Pide al usuario que introduzca su apellido materno

16.- Realiza una comprobacion para ver si el usuario no dejo vacio el campo

17.- Si el campo quedo vacio, se imprime "Introduzca un apellido materno valido" y se repite el ciclo

18.- Asigna el valor de texto vacio a la variable "edad" para poder entrar al ciclo

19.- Comienza un ciclo que se repetira hasta que se introduzca un valor a la variable "edad"

20.- Pide al usuario que introduzca su edad en años

21.- Realiza una comprobacion para ver que lo que se inserto en el campo sean solo digitos mediante la funcion "isdigit()"

22.- Si la condicion se cumple (es decir, no son solo digitos), manda el mensaje "Introduzca una edad valida"

23.- Reasigna el valor de texto vacio a la variable "edad" para volver al ciclo

24.- Si la condicion no se cumple (es decir, si son solo digitos), sale de la condicion if

25.- Cambia el valor del tipo de la variable "edad" de datos de cadena de texto a datos de numero entero

26.- Asigna el valor de texto vacio a la variable "estatura" para poder entrar al ciclo

27.- Comienza un ciclo que se repetira hasta que se introduzca un valor a la variable "estatura"

28.- Pide al usuario que introduzca su estatura en metros

29.- Crea una nueva variable llama "nestatura" que contendra los datos de la variable "estatura", pero remplazando todos los puntos (".") que contenga por texto vacio ("") con la funcion ".replace()"

30.- Realiza una comprobacion para ver que lo que se inserto en el campo (sin puntos, y haciendo la comprobacion con la nueva variable "nestatura") sean solo digitos mediante la funcion "isdigit()""

31.- Si la condicion se cumple (es decir, no son solo digitos), manda el mensaje "Introduzca una edad valida"

32.- Reasigna el valor de texto vacio a la variable "estatura" para volver al ciclo

33.- Si la condicion no se cumple (es decir, si son solo digitos), sale de la condicion if

34.- Cambia el valor del tipo de la variable "estatura" de datos de cadena de texto a datos de numero flotante

35.- Realiza una comprobacion para ver que la variable "estatura" no sea mayor a 3, para evitar cantidades superiores a 3 metros por error al no poner el punto decimal

36.- Si la condicion se cumple, manda el mensaje "Introduzca una edad valida"

37.- Reasigna el valor de texto vacio a la variable "edad" para volver al ciclo

38.- Asigna el valor de texto vacio a la variable "peso" para poder entrar al ciclo

39.- Comienza un ciclo que se repetira hasta que se introduzca un valor a la variable "peso"

40.- Pide al usuario que introduzca su peso en kilogramos

41.- Crea una nueva variable llama "npeso" que contendra los datos de la variable "peso", pero remplazando todos los puntos (".") que contenga por texto vacio ("") con la funcion ".replace()"

42.- Realiza una comprobacion para ver que lo que se inserto en el campo (sin puntos, y haciendo la comprobacion con la nueva variable "npeso") sean solo digitos mediante la funcion "isdigit()""

43.- Si la condicion se cumple (es decir, no son solo digitos), manda el mensaje "Introduzca un peso valida"

44.- Reasigna el valor de texto vacio a la variable "peso" para volver al ciclo

45.- Si la condicion no se cumple (es decir, si son solo digitos), sale de la condicion if

46.- Cambia el valor del tipo de la variable "peso" de datos de cadena de texto a datos de numero flotante

47.- Realiza el calculo del IMC con el peso sobre la estatura al cuadrado

48.- Imprimen los datos de manera presentable integrando diferentes funciones y formatos como:
* ".title()": para que las primeras letras del texto sean mayusculas (en la variable "nombre"), esto porque la persona puede tener dos nombres
* ".capitalize()": para que la primera letra de la primera palabra sea mayuscula (en las variables "apellidop" y "apellidom"), ya que cada apellido va por separado
* ":.2f": para asignarle solo 2 decimales al numero (en este caso las variables "estatura" y "peso")
Y las dos impresiones van en cadenas de formato "f-strings" para poder integrar variables en la cadena de texto

49.- Realiza una comprobacion para ver que la variable "edad" sea menor a 18

50.- Si la condicion se cumple, manda el mensaje "Y que eres menor de edad"

51.- Si la condicion no se cumple, sale de la condicion if

52.- Si la condicion no se cumple, manda el mensaje "Y que eres mayor de edad"

53.- Imprime "Calculamos tu IMC en " concatenando el valor de la variable IMC en formato de cadena de texto

54.- Realiza una condicion para imprimir la categoria de peso en la que se encuentra la persona dependiendo del calculo del IMC

55.- Se hace un contador regresivo para ir restando las personas que ya han realizado su calculo hasta llegar a 0 y terminar el ciclo restandole a la variable "personas" uno y reasignando el valor a la misma variable

56.- Si la variable "personas" llega a 0 manda a un mensaje de despedida y sale del ciclo para finalizar el proceso

## *Reflexiones sobre el Bootcamp*

* Me gusta el formato del Bootcamp, y te deja una ventana para el investigar y resolver problemas, pero sabiendo que tienes acompañamiento.
* Aunque no he podido estar en las clases en vivo, me gusta la forma en como lleva las clases el coach Ariel, explicando mediante la pantalla de uno de los alumnos, ya que con eso vemos las posibles trabas reales que podemos pasar al momento de realizar las tareas, y se van resolviendo en el proceso.
* En Python existen diferentes formas para llegar al mismo resultado y esto te da una ventana de oportunidad muy grande.