prodotti=(
    ("Mela"("Lunedi", 1.0),("Martedi", 1.0),("Mercoledi", 1.3),("Giovedi", 1.2),("Venerdi", 1.1),("Sabato", 0.9)),
    ("Banana"("Lunedi", 1.0),("Martedi", 1.2),("Mercoledi", 1.4),("Giovedi", 1.3),("Venerdi", 1.0),("Sabato", 0.5)),
)

def prezzo_medio(prodotti, prodotto):
    somma=0
    i=0
   
    for p,*giorni_prezzi in prodotti:
        for gio, pre in giorni_prezzi:
            if(p==prodotto):
                somma+=pre
                i+=1
    if(i>0):
        return (f"il prezzo medio di {prodotto} è {somma/i}")
    else:
        return ("Prodotto inesistente")

def media(prodotti):
    somma=0
    i=0
   
    for p,*giorni_prezzi in prodotti:
        for gio, pre in giorni_prezzi:
            somma+=pre
            i+=1
    return (f"il prezzo medio di {prodotto} è {somma/i}")

def max_prex(prodotti,prodotto):
    giorni=[]
    max=0
   
    for p,*giorni_prezzi in prodotti:
        for gio, pre in giorni_prezzi:
            if(p==prodotto and max<pre):
                max=pre
    for p,*giorni_prezzi in prodotti:
        for gio, pre in giorni_prezzi:
            if(prodotto==p and max==pre):
                giorni.append(gio)
    return(f"ilprezzo massimo di {prodotto} è {max} nei giorni {giorni}")


def prex_min(prodotti):
    giorniM=[];giorniB=[]
    minM=99;minB=99
    for p,*giorni_prezzi in prodotti:
        for gio, pre in giorni_prezzi:
            if(minM>pre and p=="Mela"):
                minM=pre
            if(minB>pre and p=="Banana"):
                minB=pre

    for p,*giorni_prezzi in prodotti:
        for gio, pre in giorni_prezzi:
            if(minM==pre and p=="Mela"):
                giorniM.append(gio)
            if(minB==pre and p=="Banana"):
                giorniB.append(gio)
    return (f"il prezzo minimo delle mele è {minM} nei giorni {giorniM} \nil prezzo minimo delle mele è {minB} nei giorni {giorniB}")
    


prodotto=str(input("inserisci prodotto "))
giorno=str(input("inserisci giorno "))
print(prezzo_medio(prodotti, prodotto))
print(media(prodotti))
print(max_prex(prodotti,prodotto))
print(prex_min(prodotti))