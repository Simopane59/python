from multiprocessing import Process #per creare processi

"""
multiprocessing è una libreria per la creazione, la comunicazione e la sincronizzazione
tra processi nella programmazione parallela e concorrente
Process è una classe per creare processi eseguendo una funzione(o metodo) specificata da target
"""

def process_function(data): #funzione che moltiplica per 2 i dati
    result=data*2
    print(result)

if __name__ =="__main__":
    data_list=[1,2,3,4]
    processes=[]

    for data in data_list:
        p=Process(target=process_function, args=(data,)) #assegna al nuovo processo un dato e la funzione da eseguire
        processes.append(p) #aggiunto a lista dei processi
        p.start() #avvio
    
    for p in processes:
        p.join() #blocca processo principale fino al termine del processo separato
