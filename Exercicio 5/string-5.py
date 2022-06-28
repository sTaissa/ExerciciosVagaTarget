#inverte uma string informada
def inverteString(s):
    newS = []
    i = len(s)

    #atribui a string da última para a primeira posição à lista, pois listas são mais simples de manipular
    while(i>0):
        newS += s[i - 1]
        i -= 1

    #transforma a lista modificada em string novamente
    s = "".join(newS)

    return s

#solicita a string
str = input("Digite a string: ")

#chama a função que retornará a string invertida
strInverso = inverteString(str)

print(strInverso)