def printIntro(fileName):
    '''
    Función 1: encargada de mostrar por pantalla un archivo de texto
    Argumentos:
        fileName: nombre del archivo que se desea mostrar
    Entradas:
        None
    Salidas por pantalla:
        archivo.txt     (str)
    return:
        None
    '''
    print(open(fileName).read())
    return

def inputSecret():
    '''
    Función 2: encargada de leer una palabra secreta ingresada
    Argumentos:
        None
    Entradas:
        palabra secreta
    Salidas por pantalla:
        None
    return:
        palabra ingresada   (str)
    '''
    palabra = input("Ingresa la palabra secreta: ")
    return palabra

def loadWords(fileName):
    '''
    Función 3: que recibe un archivo de texto y lo convierte en una cadena de caracteres que será empleada más adelante
    Argumentos:
        fileName: nombre del archivo donde se encuentran las palabras a emplear en el programa
    Entradas:
        None
    Salidas por pantalla:
        None
    return: 
        palabra secreta seleccionada de forma aleatoria ->(str)
    Variables auxiliares:
        cargarpalabras: variable donde le asignaremos una cadena de texto de un archivo de texto que leeremos
        palabrasecre: variable donde asignamos el resultado de la invoación a la función 4
    '''
    import random #libreria con función últil para paso en la función
    def countWords(palabras,separador):
        '''
        Función 4: encargada de contar la cantidad de palabras del archivo cargado y leído
        Argumentos: 
            variable donde se almacena la cadena de palabras; separador: caracter que indica la separación entre caracteres
        Entradas:
            None
        Salidas por pantalla:
            None
        return:
            palabra aleatoria  -> (str)
        Variables auxiliares:
            palabraseparadas: De la cadena incial, se separan las palabras cada que se encuentra el separador, arroja como resultado una cadena como si fuese una lista
            contarpalabras: cantidad de palabras de la cadena una vez que han sido separadas
            palabraaleatoria: Variable donde se almacenará el resultado de la invocación a la función 5
        '''
        palabraseparadas = cargarpalabras.split(separador)
        contarpalabras = len(palabraseparadas)-1
        def pickWord(palabraseparadas,contarpalabras):
            '''
            Función 5: encargada de seleccionar una palabra de forma aleatoria de la cadena de palabras
            Argumentos:
                V. donde se encuentran los términos separados; cantidad total de términos
            Entradas:
                None
            Salidas por pantalla:
                None
            return:
                palabra seleccionada de forma aleatoria
            Variables auxiliares:
                pospalabrasecre: Número entero seleccionado de manera aleatoria que indicará la palabra seleccionada
                palabrasecre: palabra de la cadena separada que se encuentra en la posición pospalabrasecre
            '''
            pospalabrasecre = random.randint(0,contarpalabras) #.randint: función de la librería random: encargada de arrojar un número entero aleatorio desde la posición del primer argumento a la posición del segundo argumento
            palabrasecre = palabraseparadas[pospalabrasecre]
            palabrasecre = palabrasecre.lstrip()
            return palabrasecre
        palabraleatoria= pickWord(palabraseparadas, contarpalabras)
        return palabraleatoria
    cargarpalabras = (open(fileName).read())
    palabrasecre= countWords(cargarpalabras, ",") 
    return palabrasecre


def cadenapalabra(palabrasecre) :
    '''
    Función encargada de crear la cantidad de casillas en blanco de la palabra que se mostrarán más adelante en pantalla
    Argumentos:
        palabra secreta del juego
    Entradas:
        None
    Salidas por pantalla:
        None
    return:
        cadena de casillas en blanco -> (str)
    Ejm:
        palabra secreta = pollo
        cadenavacia = _ _ _ _ _
    '''
    cadenavacia = "" 
    for aux in palabrasecre:
        if (aux != " "):
            cadenavacia += "_ "
        else:
            cadenavacia += " "
    return cadenavacia

def obtenerLetrasDisponibles(abc,letra):
    '''
    Función 7: encargada de mostrar letras que no se han intentado y son los posibles caracteres a ingresar
    Argumentos:
        letras del abecedario / letras disponibles para el momento; letra ingresada por el usuario
    Entradas:
        None
    Salidas por pantalla:
        None
    return:
        letras que se disponen aún
    Variables auxiliares:
        longiabc: cantidad de letras que aún se disponen
        abc: letras del abecedario que aún se encuentran disponibles para ingresar
        letrasDisp: letras que aún se disponen
        s: variable contadora para el ciclo, esta se usa para evaluar la posición de una letra en abc
        letraabc: letra de abc en la posición s
    Ejm:
        letra = a
        letrasDisp= bcdefghijklmnopqrstuvwxyz
    '''
    longiabc = len(abc)-1
    letrasDisp=""
    s=0
    while s<=longiabc:
        letraabc= abc[s]
        if letra == letraabc:
            letrasDisp = letrasDisp
        else:
            letrasDisp += letraabc
        s+=1
    return letrasDisp


def verificarLetraIngresada(letra, LetrasIntentadas): 
    '''
    Función 8: encargada de determinar si la letra ingresada ya fue usada o no
    Argumentos:
        letra:letra ingresada por el usuario ; letrasIntentadas: letras / caracteres que fueron usadas para el momento
    Entradas:
        None
    Salidas por pantalla:
        En caso de que la letra ya haya sido usada: letra ya fue usada
    return:
        letrasIntenadas: letras que han sido empleadas para el momento -> (str)
    '''
    if letra in LetrasIntentadas: 
        print(letra, 'ya fue usada')
    else:
        LetrasIntentadas += letra
    return LetrasIntentadas

palabras_adivinadas=0
def parteadivinada (cadenavacia, palabrasecre):
    '''
    Función 6: encargada de mostrar por pantalla la parte que ha sido adivinada, esta va acompañada de las funciones 7 y 8
    Argumentos:
        cadenavacia: cadena con espacios en blanco; palabrasecre: palabra a adivinar durante la ejecución del juego
    Entradas:
        letra: letra para analizar si se encuentra en la palabra secreta
    Salidas por pantalla:
        letras disponibles al momento
        letras que se han intentado al momento
        cadena de caracteres vacios una vez que se ha reemplazado la letra en caso de que esta se encuentre en la palabra
    return:y
        None
    Variables auxiliares:
        longipalabsecre: cantidad de caracteres de la palabra secreta
        n: variable contadora que servirá para acceder a la posición n de la palabra secreta hasta llegar a su última casilla
        palabrasecreseparada: palabra secreta habiendo sido modificada para que posea igual longitud a la cadena vacía
        longipalabsecresep: longitud de caracteres de la palabra secreta una vez ha sido separada
        letras_disponibles: letras que se muestran como posibles entradas para el momento
        cadenareemplazada: V. donde se encuentra la cadena vacía una vez que ha sido reemplazada la letra ingresada
        i: V. contadora que va a evaluar desde la posición 0 hasta longipalabsecresep
        letrapalab:letra de palabsecresep en el índice i
    '''
    intentos=0
    cadenavacia = cadenavacia.rstrip()
    LetrasIntentadas =""
    palabrasecreseparada = "" 
    longipalabsecre = len(palabrasecre)-1
    n=0
    while n<=longipalabsecre:
        if palabrasecre[n]==" ":
            palabrasecreseparada += " "
        else:
            palabrasecreseparada += palabrasecre[n]+" "
        n +=1
    palabrasecreseparada = palabrasecreseparada.rstrip()
    longipalabsecresep = len(palabrasecreseparada)-1
    letras_disponibles = 'abcdefghijklmnopqrstuvwxyz'
    while cadenavacia != palabrasecreseparada:
        print()
        print('Las letras disponibles son', letras_disponibles)
        letra = input("Ingrese una letra a evaluar ") 
        letra= letra.lower()
        letras_disponibles=obtenerLetrasDisponibles(letras_disponibles,letra)
        i = 0
        cadenareemplazada = "" 
        while i<= longipalabsecresep:
            letrapalab = palabrasecreseparada[i] 
            if letra == letrapalab:
                cadenareemplazada += letra
            else:
                cadenareemplazada += cadenavacia[i]
            i+= 1
        if letra in LetrasIntentadas:
            pass
        elif cadenavacia == cadenareemplazada:
            intentos += 1
        else:
            pass
        LetrasIntentadas =  verificarLetraIngresada(letra,LetrasIntentadas)
        cadenavacia= cadenareemplazada
        print('las letras intentadas al momento son', LetrasIntentadas)
        print ('Haz fallado ', intentos, 'vez / veces')
        print (cadenareemplazada)
        global palabras_adivinadas
        if intentos == 8:
            print('Ya no tienes más intentos, haz fallado =(')
            print('la palabra era', palabrasecre)
            print('llevas', palabras_adivinadas, 'palabra(s) adivinadas')
            print()
            break
        elif cadenavacia ==palabrasecreseparada:
            palabras_adivinadas+=1
            print('Adivinaste la palabra correcta =P')
            print('llevas', palabras_adivinadas, 'palabra(s) adivinadas')
            print()
        else:
            pass
    return
