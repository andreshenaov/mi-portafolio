from Funcionesahorcao import *
otraVez= 'y'
while otraVez == 'y':
    printIntro("intro.txt")
    printIntro("InstruccionesJuego.txt")
    print('SELECCION MODO DE JUEGO')
    modo_juego=int(input('1. Ingresar palabra secreta 2. Seleccionar palabra aleatoria '))
    if modo_juego == 1:
        palabra=inputSecret()
    else: 
        palabra= loadWords('superHeroes.txt')
    palabra_guiones = cadenapalabra(palabra)
    print(palabra_guiones)
    parteadivinada(palabra_guiones, palabra)
    otraVez=input('Desea jugar de nuevo? -->  Ingrese "y" en caso de que si, caso contrario, ingrese "n" si desea terminar de jugar: ')
    