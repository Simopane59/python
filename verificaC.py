tupla_consumi_energetici = [
    ("Milano", [
        ("gennaio", ("elettrico", 300)),
        ("febbraio", ("elettrico", 280)),
        ("gennaio", ("elettrico", 310)),
        ("febbraio", ("benzina", 250)),
        ("marzo", ("elettrico", 350)),
        ("febbraio", ("benzina", 280)),
    ]),
    ("Brescia", [
        ("gennaio", ("elettrico", 280)),
        ("febbraio", ("benzina", 260)),
        ("gennaio", ("elettrico", 300)),
        ("febbraio", ("elettrico", 270)),
    ]),

    ("Roma", [
        ("gennaio", ("benzina", 320)),
        ("febbraio", ("elettrico", 300)),
        ("gennaio", ("elettrico", 200)),
        ("febbraio", ("elettrico", 400)),
    ]),
]

def analizza_consumi_energetici(citta, risorsa):
    c=0;max=tupla_consumi_energetici[1][1][1];month=" ";somma=0
    for city, mesi in tupla_consumi_energetici:
        for mese, risorsa_consumo in mesi:
            resource,consumo=risorsa_consumo
            if citta==city and risorsa==resource:
                somma+=consumo
                c+=1
            if max<consumo:
                max=consumo
                month=mese
                      
    return (somma/c,(max,month))

citta=str(input("inserisci città "))
risorsa=str(input("inserisci consumo "))
risultato_analisi = analizza_consumi_energetici(citta, risorsa)
if risultato_analisi[0]>0:
    print(risultato_analisi)
else:
    print("nessun risultato, inesistente")