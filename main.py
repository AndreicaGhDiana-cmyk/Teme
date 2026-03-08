def diferenta_max_min(a,b,c):
    mare = max(a,b,c)
    mic = min(a,b,c)
    return mare - mic


def numar_cifre_impare(n):
    numar = 0
    if n%2==1:
        numar += 1
    if n//10%2==1:
        numar += 1
    if n//100%2==1:
        numar += 1
    return numar


def numar_maxim_cutii(a,b,c,h):
    cutie = min(a,b,c)
    h = h * 100
    numar_cutii = h // cutie
    return numar_cutii


def nume_luna(n):
    luni =  ["", "Ianuarie", "Februarie", "Martie", "Aprilie",
        "Mai", "Iunie", "Iulie", "August",
        "Septembrie", "Octombrie", "Noiembrie", "Decembrie"]
    return luni[n]


def afiseaza_paralelogram(n, c):

    for i in range(1,n+1):
        print (c*i)
    for i in range(n,0,-1):
        print (" "*(n+1-i)+c*i)


def afiseaza_piramida(n):
    for i in range(1,n+1):
       for j in range(1,i+1):
           print(j, end=" ")
       print()


print(afiseaza_piramida(3))