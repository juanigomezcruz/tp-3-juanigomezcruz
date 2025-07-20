def slice_advanced():
    texto = input("Ingresa un texto: ")
    if len(texto) >= 5:
        resultado = texto[4::2]
        print("Resultado:", resultado)
        
slice_advanced()
