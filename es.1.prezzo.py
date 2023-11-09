prodotti=(
    ("Mais", "Lunedi", 1.0),
    ("Mela", "Martedi", 1.2),
    ("Mela", "Mercoledi", 1.1),
    ("Banana", "Lunedi", 0.8),
    ("Banana", "Martedi", 0.9),
    ("Banana", "Mercoledi", 0.7),
)

def prezzo_medio(prodotti, prodotto, giorno):
    somma=0
    i=0
   
    for p,g,c in prodotti:
        if(p==prodotto and g==giorno):
            somma+=c
            i+=1
    if(i>0):
        return (f"il prezzo di {prodotto} nel giorno {giorno} è {somma/i}")
    else:
        return ("Prodotto inesistente")



prodotto=str(input("inserisci prodotto "))
giorno=str(input("inserisci giorno "))
print(prezzo_medio(prodotti, prodotto, giorno))
