

ciudad_origen = input("origen: ")
ciudad_destino = input("destino: ")
edad = int(input("edad: "))




if ciudad_origen == "medellin" and ciudad_destino == "bogota":
    medellin_bogota = 200000
    if edad < 60:
        recargo = 10000
        precio_final = medellin_bogota + recargo
        print("el valor del tiquete es de ", precio_final)
    else:
        print(medellin_bogota)

elif ciudad_origen == "medellin" and ciudad_destino == "cali":
    medellin_cali = 250000
    descuento = edad * 0.1 * 1000
    precio_final = medellin_cali - descuento
    print("el valor del tiquete es de ", precio_final)

elif ciudad_origen == "medellin" and ciudad_destino == "barranquilla":
    medellin_barranquilla= 300000
    costo_adicional = edad * 1000
    precio_final = medellin_barranquilla + costo_adicional
    print("el valor del tiquete es de ", precio_final)

elif ciudad_origen == "bogota" and ciudad_destino == "medellin":
    bogota_medellin =  200000
    if edad > 80:
        print("el tiquete es gratis")
    else:
        print("el valor del tiquete es de ", bogota_medellin)

elif ciudad_origen == "bogota" and ciudad_destino == "cali":
    bogota_cali = 200000
    if edad < 60:
        diferencia_de_edad = 60 - edad
        precio_adicional = diferencia_de_edad * 1000
        if precio_adicional > 20000:
            precio_adicional = 20000
            precio_final = bogota_cali + precio_adicional
            print("el valor del tiquete es de ", precio_final)
        else:
            precio_adicional <= 20000
            precio_final = bogota_cali + precio_adicional
            print("el valor del tiquete es de ", precio_final)
    else:
        print("el valor del tiquete es de ", bogota_cali)

elif ciudad_origen == "bogota" and ciudad_destino == "barranquilla":
    bogota_barranquilla = 400000
    if edad > 60:
        precio_adicional = edad * 0.05 * 10000
        precio_final = bogota_barranquilla + precio_adicional
        print("el valor del tiquete es de ", precio_final)
    else:
        print("el valor del tiquete es de ", bogota_barranquilla)

elif ciudad_origen == "cali" and ciudad_destino == "medellin":
    cali_medellin = 350000
    print("el valor del tiquete es de ", cali_medellin)

elif ciudad_origen == "cali" and ciudad_destino == "bogota":
    cali_bogota = 280000
    if edad < 60:
        precio_adicional = 20000
        precio_final = cali_bogota + precio_adicional
        print("el valor del tiquete es de ", precio_final)
    else:
        print("el valor del tiquete es de ", cali_bogota)

elif ciudad_origen == "cali" and ciudad_destino == "barranquilla":
    cali_barranquilla = 190000
    if edad < 60:
        precio_adicional = 10000
        precio_final = cali_barranquilla + precio_adicional
        print("el valor del tiquete es de ", precio_final)
    else:
        print("el valor del tiquete es de ", cali_barranquilla)

elif ciudad_origen == "barranquilla" and ciudad_destino == "cali":
    barranquilla_cali = 350000
    if edad > 60:
        diferencia_de_edad = edad - 60
        precio_adicional = diferencia_de_edad * 10000
        precio_final = barranquilla_cali + precio_adicional
        print("el valor del tiquete es de ", precio_final)
    else:
        print("el valor del tiquete es de ", barranquilla_cali)

elif ciudad_origen == "barranquilla" and ciudad_destino == "bogota":
    barranquilla_bogota = 210000
    if edad < 30:
        precio_adicional = 30000
        precio_final = barranquilla_bogota + precio_adicional
        print("el valor del tiquete es de ", precio_final)
    else:
        print("el valor del tiquete es de ", barranquilla_bogota)

elif ciudad_origen == "barranquilla" and ciudad_destino == "medellin":
    if edad >= 10:
        barranquilla_medellin = 500000
        print("el valor del tiquete es de ", barranquilla_medellin)
    else:
        barranquilla_medellin = 250000
        print("el valor del tiquete para niños menores de 10 años es de ", barranquilla_medellin)

else:
    ciudad_origen == "miami" or ciudad_destino == "miami"
    miami = 980000
    print("el valor del tiquete internacional es de ", miami)