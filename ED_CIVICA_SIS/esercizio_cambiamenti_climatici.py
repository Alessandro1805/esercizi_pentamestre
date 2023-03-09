##grafico a dispersone metodo mat plot lib scatter
##Year,Total,Gas Fuel,Liquid Fuel,Solid Fuel,Cement,Gas Flaring,Per Capita
import matplotlib.pyplot as plt
import csv
anni = []
emissioni_totali = []
emissioni_gas = []
emissioni_liquidi=[]
emissioni_solidi=[]
emissioni_cemento=[]
emissioni_gasflaring=[]
emissioni_procapiti=[]
data_file = open("./CO2_emissions.csv")
data_reader = csv.reader(data_file, delimiter=',')
next(data_reader)
for row in data_reader:
    anni.append(float(row[0]))
    emissioni_gas.append(float(row[1]))
    emissioni_liquidi.append(float(row[2]))
    emissioni_solidi.append(float(row[3]))
    emissioni_cemento.append(float(row[4]))
    emissioni_gasflaring.append(float(row[5]))
    emissioni_procapiti.append(float(row[6]))
fig, (ax1, ax2,ax3,ax4,ax5,ax6) = plt.subplots(6, 1)
fig.suptitle('grafici coi dati del file csv')
ax1.plot(anni, emissioni_gas, 'o-g')##o -g o-r definiscono stile della linea
ax1.set_xlabel('anno')
ax1.set_ylabel('emissioni gas')
ax2.plot(anni, emissioni_liquidi, 'o-r')
ax2.set_xlabel('anno')
ax2.set_ylabel('emissioni liquidi ')

ax3.plot(anni, emissioni_solidi, 'o-b')
ax3.set_xlabel('anno')
ax3.set_ylabel('emissioni solidi')

ax4.plot(anni, emissioni_gasflaring, 'o-y')
ax4.set_xlabel('anno')
ax4.set_ylabel('emissioni gasflaring')

ax5.plot(anni, emissioni_procapiti, 'o-g')
ax5.set_xlabel('anno')
ax5.set_ylabel('emissioni gasflaring')

ax6.plot(anni, emissioni_cemento, 'o-r')
ax6.set_xlabel('anno')
ax6.set_ylabel('emissioioni cemento')
plt.show()