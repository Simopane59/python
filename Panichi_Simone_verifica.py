vendite=(
    ("Lampada", [("Gennaio", 50),("Febbraio", 30),("Marzo", 120),("Aprile", "N/D"),("Maggio", 200),("Giugno", 20),("Luglio", 25),("Agosto", 400),("Settembre", 205),("Ottobre", 30),("Novembre", 200),("Dicembre", 310)]),
    ("Letto", [("Gennaio", 200),("Febbraio", 310),("Marzo", 100),("Aprile", 110),("Maggio", 400),("Giugno", 300),("Luglio", "N/D"),("Agosto", 330),("Settembre", 260),("Ottobre", 40),("Novembre", 20),("Dicembre", 400)]),
    ("Comodino", [("Gennaio", 220),("Febbraio", 300),("Marzo", 260),("Aprile", 500),("Maggio", 270),("Giugno", 390),("Luglio", 230),("Agosto", 340),("Settembre", 240),("Ottobre", 400),("Novembre", 20),("Dicembre", 300)]),
)

def media(vendite, nomeR):
    maxV=vendite[0][1][1][1]; minV=vendite[0][1][1][1];max=[];min=[];somma=0;c=0

    for reparto,*m_v in vendite:
        for elem in m_v:
            for mese_vendita in elem:
                mese,vendita=mese_vendita
                if nomeR==reparto and vendita!="N/D":
                    c+=1
                    somma+=vendita
                    if maxV<vendita:
                        maxV=vendita
                    if minV>vendita:
                        minV=vendita
                elif(nomeR==reparto and vendita=="N/D"):
                    c-=1
    for reparto,*m_v in vendite:
        for elem in m_v:
            for mese_vendita in elem:
                mese,vendita=mese_vendita
                if nomeR==reparto and vendita!="N/D":
                    if(vendita==maxV):
                        max.append(mese)
                    if(vendita==minV):
                        min.append(mese)
    
    return (somma/c,(maxV, max),(minV,min))

nomeR=str(input("inserisci il nome del reparto "))
ris=media(vendite, nomeR)
print(f"le vendite medie di {nomeR} è {ris[0]:.2f}, vendita massima {ris[1]}, vendita minima {ris[2]}  ")