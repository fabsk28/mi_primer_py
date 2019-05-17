
adivina_numero = 2
numero_oportunidades = 1

numero_usuario = int(input("adivina el numero del 1 al 10, escribelo: "))


if numero_oportunidades == 5:
    print("Se terminaron tus oportunidades, FALLASTE")
else:

    if numero_usuario == adivina_numero:
        print("Correcto, el numero es 2")
    else:
        print("NO, haz fallado")
        numero_oportunidades = numero_oportunidades + 1
        numero_usuario = int(input("adivina el numero del 1 al 10, intentalo de nuevo: "))

        if numero_usuario == adivina_numero:
            print("Correcto, el numero es 2")
        else:
            print("NO, haz fallado")
            numero_oportunidades = numero_oportunidades + 1
            numero_usuario = int(input("adivina el numero del 1 al 10, intentalo de nuevo: "))

            if numero_usuario == adivina_numero:
                print("Correcto, el numero es 2")
            else:
                print("NO, haz fallado")
                numero_oportunidades = numero_oportunidades + 1
                numero_usuario = int(input("adivina el numero del 1 al 10, intentalo de nuevo: "))

                if numero_usuario == adivina_numero:
                    print("Correcto, el numero es 2")
                else:
                    print("NO, haz fallado")
                    numero_oportunidades = numero_oportunidades + 1
                    numero_usuario = int(input("adivina el numero del 1 al 10, intentalo de nuevo: "))
                    print("Se terminaron tus oportunidades, FALLASTE")
