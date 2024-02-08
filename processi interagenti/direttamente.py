import os #il modulo fornisce funzionalità per interagire con il sistema operativo
from multiprocessing import Process,current_process,Pipe

def process_id():
    print(f"Server PID: {os.getpid()}, Process name: {current_process().name}, Process PID: {current_process().pid}") #nome e pid del processo

def process_function(conn):
    process_id()
    print("Elabora il dato ricevuto ed invio del risultato")
    data_received=conn.recv() #riceve connessione
    result=data_received*2
    conn.send(result) #manda connessione
    conn.close() #chiude connessione

if __name__=="__main__":
    process_id()
    print("Creo una connessione e un processo figlio")
    parent_conn,child_conn=Pipe() #crea connessione tra genitore e figlia
    data=5
    p=Process(target=process_function,args=(child_conn,))
    p.start()
    parent_conn.send(data) #genitore invia
    result=parent_conn.recv() # genitore riceve
    p.join()
    process_id()
    print("Stampo il risultato ricevuto")
    print(result)