# Valores

dollar_euro = 0.84
libra_euro = 1.18
mad_euro = 0.094
euro_libra = 0.85
euro_dollar = 1.19
euro_mad = 10.64

# Introduccion

print("")
print("██████╗ █████╗ ███╗   ███╗██████╗ ██╗ ██████╗     ██████╗ ██╗██╗   ██╗██╗███████╗ █████╗ ███████╗")
print("██╔════╝██╔══██╗████╗ ████║██╔══██╗██║██╔═══██╗    ██╔══██╗██║██║   ██║██║██╔════╝██╔══██╗██╔════╝")
print("██║     ███████║██╔████╔██║██████╔╝██║██║   ██║    ██║  ██║██║██║   ██║██║███████╗███████║███████╗")
print("██║     ██╔══██║██║╚██╔╝██║██╔══██╗██║██║   ██║    ██║  ██║██║╚██╗ ██╔╝██║╚════██║██╔══██║╚════██║")
print("╚██████╗██║  ██║██║ ╚═╝ ██║██████╔╝██║╚██████╔╝    ██████╔╝██║ ╚████╔╝ ██║███████║██║  ██║███████║")
print("╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝ ╚═════╝     ╚═════╝ ╚═╝  ╚═══╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝")
print("")                                                                                                 

opcion = str(input("Que operacion quieres realizar? \nOpciones:\n \nDE (Dollar a euro) \nLE (Libra a euro) \nMADE (MAD a euro) \nED (Euro a Dollar) \nEL (Euro a libra) \nEMAD (Euro to MAD)\n \n"))

# Cambios divisas

if opcion == "DE":
    print("Has elegido la opcion de cambiar de  Dollares (USD/$) a Euros (EUR/€) ")
    cantidad_cambio_DE = float(input("Cuantos Dollares Quieres pasar a Euros? "))
    euro_DE_final = cantidad_cambio_DE * 0.91
    print("Tus {} Dollares equivalen a {} Euros".format(cantidad_cambio_DE, euro_DE_final))

elif opcion == "LE":
    print("Has elegido la opcion de cambiar de  Libra (£/PND) a euro (€/EUR) ")
    cantidad_cambio_LE = float(input("Cuantas Libras Quieres pasar a Euros? "))
    euro_LE_final = cantidad_cambio_LE * 1.18
    print("Tus {} Libras equivalen a {} euros".format(cantidad_cambio_LE, euro_LE_final))

elif opcion == "MADE":
    print("Has elegido la opcion de cambiar de  Dirham Marroqui (د.م /MAD) a euro (€/EUR) ")
    cantidad_cambio_MADE = float(input("Cuantos Dirhams Marroquis quieres pasar a Euros? "))
    euro_MADE_final = cantidad_cambio_MADE * 0.094
    print("Tus {} Dirhams Equivalen a {} euros".format(cantidad_cambio_MADE, euro_MADE_final))

elif opcion == "ED":
    print("Has elegido la opcion de cambiar de Euros (EUR/€) a Dollares ($/USD) ")
    cantidad_cambio_ED = float(input("Cuantos Euros quieres pasar a Dollares "))
    euro_ED_final = cantidad_cambio_ED * 1.19
    print("Tus {} Euros equivalen a {} Dollares".format(cantidad_cambio_ED, euro_ED_final))

elif opcion == "EL":
    print("Has elegido la opcion de pasar de Euros (€/EUR) a Libras Esterlinas (£/PND) ")
    cantidad_cambio_EL = float(input("Cuantos Euros quieres pasar a Libras "))
    euro_EL_final = cantidad_cambio_EL * 0.85
    print("Tus {} Euros equivalen a {} Libras".format(cantidad_cambio_EL, euro_EL_final))

elif opcion == "EMAD":
    print("Has Elegido la opcion de pasar de Euros (€/EUR) a Dirhams Marroquis (د.م /MAD) ")
    cantidad_cambio_EMAD = float(input("Cuantos Euros quieres pasar a Dirhams Marroquies? "))
    euro_EMAD_final = cantidad_cambio_EMAD * 10.64
    print("Tus {} Euros Son {} Dirhams Marroquies ".format(cantidad_cambio_EMAD, euro_EMAD_final))

else:
    print("No has elegido una opcion valida..")
    exit()