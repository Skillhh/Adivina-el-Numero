## Importar Libreria
import random

##Funcion Jugar
def Jugar():

    intentos = 0
    oportunidades = 5
    vidas = 0
    dificultad = 0
  
    ##Crea un numero aleatoriamente
    numero_aleatorio = random.randint( 1, 10)
    ##Menu
    print("\n ********** Adivina el Número ***********\n")   
  
    print("""\tSeleccione su nivel de Dificultad
        Facil = 1, Medio = 2, Dificil = 3.
    """)
    try:
        dificultad = int(input("Eliga opción: "))
    except ValueError:
        print("\n********** La opción no es valido **********\n")
    else:
        if dificultad == 1:
            print(f"""\n\tEstoy pensando un numero del 1 al 10\n
          ******* ¿adivina cuál es? ******    
            """)
            print(f"\n\t****** Tienes {oportunidades} oportunidades ******")
        elif dificultad == 2:
            oportunidades = 4
            numero_aleatorio = random.randint( 1, 20)
            print(f"""\n\tEstoy pensando un numero del 1 al 20 ******\n
          ******* ¿adivina cuál es? ******    
            """)
            print(f"\n\t****** Tienes {oportunidades} oportunidades ******\n")
        elif dificultad == 3:            
            oportunidades = 3
            numero_aleatorio = random.randint( 1, 40)
            print(f"""\n\tEstoy pensando un numero del 1 al 40\n
          ******* ¿adivina cuál es? ******    
            """)
            print(f"\n\t****** Tienes {oportunidades} oportunidades ******\n")
    
    ##Intentos para adivinar el numero
    while intentos < oportunidades:        

        try:
            adivinanza = int( input("\nEl número es: ") )
        except ValueError:
            print("\n********** La opción no es valido **********\n")
        else:        
            intentos += 1
            
            if adivinanza == numero_aleatorio:
                print("\n********** Adivinastes **********\n")
                break
            else:
                vidas = oportunidades - intentos
                if numero_aleatorio > adivinanza:
                    print("\nFallaste, el numero es mayor, intentalo de nuevo.\n")
                    print(f"\n********* Te quedan {vidas} / {oportunidades} oportunidades *********\n")
                else:
                    print("\nFallaste, el numero es menor, intentalo de nuevo.\n")
                    print(f"\n ********* Te quedan {vidas} / {oportunidades} oportunidades. *********\n")

      
    else:
        print("***** Se te acabaron los intentos *****\n")
               

##LLamando Funcion
Jugar()

jugar_nuevamente = input("¿Deseas Jugar de nuevo? si/no: ")

if jugar_nuevamente.lower() == "si":
    Jugar()

print("\n********* Gracias por Jugar *********\n")
