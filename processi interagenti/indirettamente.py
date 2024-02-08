from multiprocessing import Queue, Process, current_process
import os
"""
--Queue: classe che rappresenta una coda condivisa tra processi.
è utilizzata per consentire la comunicazione tra processi,
consentendo loro di scambiarsi dati in modo sicuro.
put(item):Aggiunge un elemento alla coda.
get(): Rimuove e restituisce un elemento dalla coda.
empty(): Restituisce True se la coda è vuota, altrimenti restituosce False.
full()Restituisce True se la coda è piena , altrimenti restituisce False.
qsize():restituisce il numero di elementi presenti nella coda.
close(): chiude la coda.
-- current_process: funzione che restituisce un oggetto Process
che rappresenta il processo in esecuzione
"""

def process_id():
    print(f"Server PID: {os.getpid()}, Process name: {current_process().name}, Process PID: {current_process().pid}") #nome e pid del processo

def process_function(data, result_queue):
    process_id()
    print("Elabora: ",data)
    result=data*2
    result_queue.put(result)

if __name__=="__main__":
    data_list=[1,2,3,4]
    result_queue=Queue() #inizializza coda
    processes=[]

    for data in data_list:
        p=Process(target=process_function, args=(data, result_queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Il main stampa i risultati")
    while not result_queue.empty(): #finche non è vuota la lista toglie e stampa
        result = result_queue.get()
        print(result)