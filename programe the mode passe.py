def NBCMin(pas):
    c=0
    for i in pas:
        if i.islower() :
          c=c+1
    return c
def NBCMaj(pas):
    c=0
    for i in pas:
        if i.isupper() :
          c=c+1
    return c
def nbcalpha(pas):
    c=0
    for i in pas:
        if ( i  != NBCMin(pas) and i != NBCMaj(pas)):
            c=c+1
    return c-(NBCMin(pas)+NBCMaj(pas))
def longMAJ(pas):
        c = 0
        c1 = 0

        for i in pas:
            if i.isupper():
                c1+= 1
                if c1 > c:
                    c= c1
            else:
                c1= 0

        return c


def longMIN(pas):
    c = 0
    c1 = 0

    for i in pas:
        if i.islower():
            c1 += 1
            if c1 > c:
                c = c1
        else:
            c1 = 0

    return c
def score(pas):
    a= NBCMin(pas)
    b=NBCMaj(pas)
    c=nbcalpha(pas)
    d=longMAJ(pas)
    e=longMIN(pas)
    f=len(pas)
    somme=f*4+(f-b)*2+(f-a)*3+c*5
    sommedesmalus=e*5+d*2
    scorefinal=somme-sommedesmalus
    return scorefinal

n=input("done le pas")
print("les min",NBCMin(n))
print("lesmaj",NBCMaj(n))
print("caracter non alphabetiques",nbcalpha(n))
print("LONGUE SEQUENCElongMAJ",longMAJ(n))
print("LONGUE SEQUENCElongMAJ",longMIN(n))
print( "lescore",score(n))
if score(n)<=20:
    print("le mot de passe est tres faible")
elif 20<=score(n)<40:
    print("le mot de passe est  faible")
elif 40<=score(n)<80:
    print("le mot de passe est  fort")
elif score(n)>80:
    print("le mot de passe est tres fort")