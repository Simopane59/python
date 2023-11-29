tupla_partite = (
    ("SquadraA", "SquadraB", 3, 2),
    ("SquadraC", "SquadraD", 1, 1),
    ("SquadraB", "SquadraC", 2, 4),
    ("SquadraD", "SquadraA", 0, 3),
    ("SquadraB", "SquadraD", 1, 2),
)

def media_goal_partite(tupla_partite):
    somma=[]
    for _,_,gC,gO in tupla_partite:
        somma.append(gC+gO)
    return sum(somma)/len(somma)

def media_goal_squadra(nome, tupla_partite):
    somma=[]
    for casa,ospite,gC,gO in tupla_partite:
        if(casa==nome):
            somma.append(gC)
        if(ospite==nome):
            somma.append(gO)
    return sum(somma)/len(somma)

def partita_con_piu_goal(tupla_partite):
    somma;punteggi=[];max=tupla_partite[2]+tupla_partite[3]
    for casa,ospite,gC,gO in tupla_partite:
        somma=gC+gO
        if somma>=max:
            max=gC+gO
            punteggi.append(gC,":",gO)
        else:
            punteggi.clear
    return (max, punteggi)

def partita_con_meno_goal(tupla_partite):
    somma;punteggi=[];min=tupla_partite[2]+tupla_partite[3]
    for casa,ospite,gC,gO in tupla_partite:
        somma=gC+gO
        if somma<=min:
            min=gC+gO
            punteggi.append(gC,":",gO)
        else:
            punteggi.clear
    return (min, punteggi)

def percentuale_vittorie_squadra(tupla_partite,nome):
    somma=[]
    for casa,ospite,gC,gO in tupla_partite:
        if(casa==nome and gC>gO):
            somma.append(1)
        elif(casa==nome and gO>=gC):
            somma.append(0)
        if(ospite==nome and gO>gC):
            somma.append(1)
        elif(casa==nome and gC>=gO):
            somma.append(0)
    return sum(somma)/len(somma)*100

print("la media dei goal è ",media_goal_partite(tupla_partite))
nome=str(input("inserisci la squadra da cercare "))
print("la media dei goal è ",media_goal_squadra(nome,tupla_partite))
print(partita_con_piu_goal(tupla_partite))
print(partita_con_meno_goal(tupla_partite))
nome=str(input("inserisci la squadra da cercare "))
print(percentuale_vittorie_squadra(tupla_partite,nome),"%")