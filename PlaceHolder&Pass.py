valor = False

if valor:
#pode usar pass ou ...
    pass
    ...
else:
    print("Bye")
 
#ou dessa forma
    
valor = True

if valor: #se o valor fosse false ele ignoraria o if e iria ao else
    print("Olá")
    pass
else:
    print("Tchau")
