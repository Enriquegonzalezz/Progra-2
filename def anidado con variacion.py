
#hacer una funcion dentro de otra funcion  
#hacemos la primera funcion 
def funcionenvolvente():
    haisa = 85 # le damos un valor 
    def funcioninterior(): # llamamos a la segunda
        nonlocal haisa   #para agregar un cambio a la variable utilizamos nonlocal 
        haisa = haisa + 5  #agregamos el cambio
        return haisa #imrprimimos
    return funcioninterior() #retornamos la funcion secundaria

print(funcionenvolvente()) #llamamos a la funcion original
    

    


    
