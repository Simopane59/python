prenotazioni=[]

def aggiungi_prenotazione(prenotazioni,nome,data,nPers,nTav):
        p=(nome, data, nPers, nTav)
        prenotazioni.append(p)

def rimuovi_prenotazione(prenotazioni,nome,data):
    for elem in prenotazioni:
        for n,d,p,t in elem:
            if nome==n and data ==d:
                prenotazioni.remove(elem)
    
def tavoli_liberi(prenotazioni,data):
    tavoli=(
    ("04-10-2023",[1,2,3,4,5,6,7,8,9,10]),
    ("05-10-2023",[1,2,3,4,5,6,7,8,9,10]),
    ("06-10-2023",[1,2,3,4,5,6,7,8,9,10]),
    )

    for n, da, pe, t in prenotazioni:
        for g,p in tavoli:
            if data==g:
                p.remove(t)
                return p

def prenotazioni_cliente(prenotazioni,nome):
    pre=[]
    for n, da, pe, t in prenotazioni:
        if n==nome:
            p=(da, pe, t)
            pre.append(p)
    return pre

def conto_totale(prenotazioni, data):
    c=0
    for n, d, p, t in prenotazioni:
        if d==data:
            c+=1
    return c

aggiungi_prenotazione(prenotazioni, "Maria", "04-10-2023", 4, 3)
aggiungi_prenotazione(prenotazioni, "Pietro", "04-10-2023", 2, 2)
aggiungi_prenotazione(prenotazioni, "Carlo", "04-10-2023", 5, 5)
print("Tavoli disponibili per il 04-10-2023:", tavoli_liberi(prenotazioni, "04-10-2023"))
print("Prenotazioni di Maria:", prenotazioni_cliente(prenotazioni, "Maria"))
print("Conto totale per il 04-10-2023:", conto_totale(prenotazioni, "04-10-2023"))
