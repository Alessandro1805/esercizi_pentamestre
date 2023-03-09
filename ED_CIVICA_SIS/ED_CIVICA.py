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
fig, (ax1, ax2,ax3,ax4) = plt.subplots(4, 1)
fig.suptitle('grafici coi dati del file csv')
ax1.plot(mesi_n, giorni_con_giacca, 'o-g')##o -g o-r definiscono stile della linea
ax1.set_xlabel('Mese')
ax1.set_ylabel('Giorni con giacca')
ax2.plot(mesi_n, temperature, 'o-r')
ax2.set_xlabel('Mese')
ax2.set_ylabel('temperature (°)')

ax3.plot(mesi_n, giorni_con_videogiochi, 'o-b')
ax3.set_xlabel('Mese')
ax3.set_ylabel('giorni con videogiochi')

ax4.plot(mesi_n, giorni_di_scuola, 'o-y')
ax4.set_xlabel('Mese')
ax4.set_ylabel('temperature giorni di scuola')
plt.show()