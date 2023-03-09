##grafico a dispersone metodo mat plot lib scatter
import matplotlib.pyplot as plt
import csv
mesi_n = []
temperature = []
giorni_con_giacca = []
giorni_con_videogiochi=[]
giorni_di_scuola=[]
data_file = open("./dati.csv")
data_reader = csv.reader(data_file, delimiter=',')
next(data_reader)
for row in data_reader:
    mesi_n.append(float(row[0]))
    temperature.append(float(row[1]))
    giorni_con_giacca.append(float(row[2]))
    giorni_con_videogiochi.append(float(row[3]))
    giorni_di_scuola.append(float(row[4]))
fig, (ax1) = plt.subplots(1, 1)
fig.suptitle('Andamento giorni con giacca in base al mese')
ax1.plot(mesi_n, giorni_con_giacca, 'o-g',label="giorni con giacca")##o -g o-r definiscono stile della linea
ax1.set_xlabel('Mese')
ax1.set_ylabel('Giorni con giacca')

ax1.plot(mesi_n, temperature, 'o-r',label="temperatura")
ax1.set_xlabel('Mese')
ax1.set_ylabel('temperature (°)')

ax1.plot(mesi_n, giorni_con_videogiochi, 'o-b',label="giorni videogiochi")
ax1.set_xlabel('Mese')
ax1.set_ylabel('giorni con videogiochi')

ax1.plot(mesi_n, giorni_di_scuola, 'o-y',label="giorni di scuola")
ax1.set_xlabel('Mese')
ax1.set_ylabel('temperature giorni di scuola')
ax1.legend()
plt.show()