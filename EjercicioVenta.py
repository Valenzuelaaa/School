def add_values_in_dict(sample_dict, key, list_of_values):
    """Append multiple values to a key in the given dictionary"""
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict


repositorio = {
    'clave' : [1111,1112,1113,1114,1115],
    'producto' : ['Manzana','Frituras','Refresco','Agua','Chocolate'],
    'precio' : [5,15,19,10,12],
    'descripcion' : ['Alimento','Alimento','Bebida','Bebida','Alimento']
    
}



for key in repositorio:
    print (key, ":" , repositorio[key]) 



print("Bienvenido, Seleccione una Opcion")
print("A. Agregar articulo")
print("B. Imprimir articulos")
print("C. Iniciar punto de venta")
opcion = input()

def sistema(opcion):
    if opcion == "A":
        print("Cuantos productos desea agregar? : ")
        a1 = int(input())
        for x in  range(a1):
            print("Ingrese la clave del articulo")
            clave = input()
            print("Ingrese el nombre del articulo")
            producto = input()
            print("Ingrese el precio del articulo")
            precio = input()
            print("Ingrese la descripcion del articulo")
            descripcion = input()
            add_values_in_dict(repositorio, 'clave', [clave])
            add_values_in_dict(repositorio, 'producto', [producto])
            add_values_in_dict(repositorio, 'precio', [precio])
            add_values_in_dict(repositorio, 'descripcion', [descripcion])
            for key in repositorio:
                print (key, ":" , repositorio[key])
                print ()
        print("Desea iniciar un punto de venta? Responda: Si/No")
        a3 = input()
        if a3 == "Si":
            print("Punto de venta iniciado")
            conta = 0
            print("Cuantos productos desea comprar: ?")
            answer = int(input())
            for x in range(answer):
                print("Ingrese el codigo de barras de su producto")
                clave = int(input())
                for keys,values in repositorio.items():
                    for item in values:
                        if item == clave:
                            index = values.index(item)
                            venta = {'Venta':[]}
                            venta['Venta'] = repositorio['precio'][index]
                            for key in venta:
                                conta += venta[key]
                                print("Desea ver la venta actual? : Si o No")
                                a2 = input()
                                if a2 == "Si":
                                    print("La venta actual es de: " , conta)
                                else:
                                    continue



    elif opcion == "B":
        for key in repositorio:
            print (key, ":" , repositorio[key]) 

    elif opcion == "C":
            print("Punto de venta iniciado")
            conta = 0
            print("Cuantos productos desea comprar: ?")
            answer = int(input())
            for x in range(answer):
                print("Ingrese el codigo de barras de su producto")
                clave = int(input())
                for keys,values in repositorio.items():
                    for item in values:
                        if item == clave:
                            index = values.index(item)
                            venta = {'Venta':[]}
                            venta['Venta'] = repositorio['precio'][index]
                            for key in venta:
                                conta += venta[key]
                                print("Desea ver la venta actual? : Si o No")
                                a2 = input()
                                if a2 == "Si":
                                    print("La venta actual es de: " , conta)
                                else:
                                    continue


sistema(opcion)