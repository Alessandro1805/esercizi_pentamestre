##grafico a dispersone metodo mat plot lib scatter
import matplotlib.pyplot as plt
import csv
anni = []
anomalie = []
data_file = open("./Temperature_Anomaly.csv")
data_reader = csv.reader(data_file, delimiter=',')
next(data_reader)
next(data_reader)
next(data_reader)
next(data_reader)
next(data_reader)
for row in data_reader:
    anni.append(float(row[0]))
    anomalie.append(float(row[1]))
fig,(ax1) = plt.subplots(1, 1)
fig.suptitle('grafici coi dati del file csv')
ax1.plot(anni, anomalie, 'o-g')##o -g o-r definiscono stile della linea
ax1.set_xlabel('anno')
ax1.set_ylabel('anomalia')
plt.show()