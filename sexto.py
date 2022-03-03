#imprime uma lista de forma organizada, com itens e valores


lanchonete = {"Salgado" : 4.5, "Lanche" : 6.5, "Suco" : 3, "Refrigerante" : 3.5, "Doce" : 1}
for item in lanchonete:
    print("{0:20} {1:6.2f}".format(item, lanchonete[item]))
print(f"Suco: {(lanchonete['Suco'])}")


#Resultado
Salgado                4.50
Lanche                 6.50
Suco                   3.00
Refrigerante           3.50
Doce                   1.00
Suco: 3
