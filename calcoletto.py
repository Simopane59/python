import threading

def calcola(operazione):
    global risultato
    ris=operazione
    risultato*=ris
    
#((3 + 4) * (5 + 2) * (3 * 3)) / 2
if __name__ == "__main__":
    risultato=1
    threads=[]
    operazioni=[(3 + 4) , (5 + 2) , (3 * 3)]
    for operazione in operazioni:
        t = threading.Thread(target=calcola(operazione))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("il risultato è ", risultato/2)