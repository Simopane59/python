tupla_pluviometrica = (
                      (("Vittuone","Milano"),(2022, ("gennaio",20))),
                      (("Vittuone","Milano"),(2023, ("marzo",80))),
                      (("Vittuone","Milano"),(2023, ("aprile",60))),
                      (("Vittuone","Milano"),(2023, ("maggio",80))),
                      (("Vittuone","Milano"),(2023, ("luglio",30))),
                      (("Vittuone","Milano"),(2023, ("agosto","N/D"))),
                      (("Varenna","Lecco"),(2023, ("luglio",150))),
                      (("Morbegno","Sondrio"),(2023, ("luglio",165)))
                      )

def media_globale(tupla_pluviometrica):
    somma=0;c=0
    for _, anno_mesePioggia in tupla_pluviometrica:
        for anno, mese_pioggia in anno_mesePioggia:
            mese,pioggia=mese_pioggia
            if anno==2023:
                c+=1
                somma+=pioggia
    return (somma/c)

def media_provincia(tupla_pluviometrica, provincia,mese):
    somma=0;c=0
    for citta_provincia, anno_mesePioggia in tupla_pluviometrica:
        _,prov=citta_provincia
        if provincia==prov:
            for _, mese_pioggia in anno_mesePioggia:
                m,pioggia=mese_pioggia
                if mese==m:
                    somma+=pioggia
                    c+=1
    media=somma/c
    return f"la media di pioggia per {provincia} è {media:.2f}"

def pioggia_max(tupla_pluviometrica, provincia):
    max=[]; maxV=tupla_pluviometrica[0][1][1][1]
    for citta_provincia, anno_mesePioggia in tupla_pluviometrica:
        _,prov=citta_provincia
        if provincia==prov:
            for _, mese_pioggia in anno_mesePioggia:
                m,pioggia=mese_pioggia
                if maxV<pioggia:
                    maxV=pioggia

    for citta_provincia, anno_mesePioggia in tupla_pluviometrica:
        citta,prov=citta_provincia
        if provincia==prov:
            for _, mese_pioggia in anno_mesePioggia:
                _,pioggia=mese_pioggia
                if maxV==pioggia:
                    max.append(mese)
                    city=citta
    return f" la citta più piovosa è {city} con {maxV} mm nei mesi {max}"
                
def pioggia_min(tupla_pluviometrica):
    min=[]; minV=tupla_pluviometrica[0][1][1][1]
    for citta_provincia, anno_mesePioggia in tupla_pluviometrica:
        _,prov=citta_provincia
        for _, mese_pioggia in anno_mesePioggia:
            _,pioggia=mese_pioggia
            if minV>pioggia:
                minV=pioggia

    for citta_provincia, anno_mesePioggia in tupla_pluviometrica:
        _,prov=citta_provincia
        if provincia==prov:
            for _, mese_pioggia in anno_mesePioggia:
                _,pioggia=mese_pioggia
                if minV==pioggia:
                    min.append(mese)

    return f" mese/i con minori precipitazioni {min}"
    
def provinciaPer(tupla_pluviometrica):
    somma=0; c=0
    for _, anno_mesePioggia in tupla_pluviometrica:
        for anno, mese_pioggia in anno_mesePioggia:
            mese,pioggia=mese_pioggia
            c+=1
            somma+=pioggia
    mediaT=somma/c

risp=0
print("\n1) media globale della pioggia\n2) media pioggia per mese e provincia\n3) città con mesi più piovosi\n4) città con mesi meno piovosi\n5) percentuale di pioggia della provincia rispetto al totale\n9) uscita")
while(risp==9):
    print("\n1) media globale della pioggia\n2) media pioggia per mese e provincia\n3) città con mesi più piovosi\n4) città con mesi meno piovosi\n5) percentuale di pioggia della provincia rispetto al totale\n9) uscita")
    risp=int(input("inserisci punto"))
    if(risp==1):
        media=media_globale(tupla_pluviometrica)
        print(f"la media di pioggia globale è {media:.2f} mm")
    elif(risp==2):
        provincia=str(input("inserisci la provincia "))
        mese=str(input("inserisci il mese "))
        print(media_provincia(tupla_pluviometrica, provincia,mese))
    elif(risp==3):
        print(pioggia_max(tupla_pluviometrica, "Milano"))
    elif(risp==4):
        print(pioggia_max(tupla_pluviometrica))
    #elif(risp==5):
