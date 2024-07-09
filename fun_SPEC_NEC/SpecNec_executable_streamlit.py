import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define input parameters
# Ratio entre ordenadas espectrales Sa(T = 0.1 s) y el PGA para el periodo de retorno seleccionado
n = 2.48
# Aceleración máxima esperada en el estrato competente para el evento sísmico de diseño, expresada como fracción de la aceleración de la gravedad
z = 0.4
I = 1                                   # Coeficiente de Importancia
# fa, fd, fs =  Coeficiente de amplificación de suelo. Amplifica las ordenadas del espectro elástico de respuesta considerando los efectos de sitio
fads = [1.2, 1.11, 1.11]
r = 1                                   # Amplificación según ubicación geografica
R = 6                                   # Factor de Reducción de respuesta sísmica
# Coeficiente de castigo por irregularidad en planta
fip = 1
# Coeficiente de castigo por irregularidad en elevación
fie = 1

To = 0.10 * fads[2] * fads[1] / fads[0]
Tc = 0.55 * fads[2] * fads[1] / fads[0]

Sae = []
Sai = []
Tie = []

for T in np.arange(0, 4, 0.005):
    if T <= To:
        Sae.append([z * fads[0] * (1 + (n - 1) * T / To) * I])
        Sai.append([n * z * fads[0] / (R * fip * fie) * I])
        Tie.append([T])
    else:
        if T <= Tc:
            Sae.append([n * z * fads[0] * I])
            Sai.append([n * z * fads[0] / (R * fip * fie) * I])
            Tie.append([T])
        else:
            Sae.append([I * n * z * fads[0] * (Tc / T) ** r])
            Sai.append([I * n * z * fads[0] * (Tc / T) ** r / (R * fip * fie)])
            Tie.append([T])

Resul = pd.DataFrame({ 'Period [s]': Tie,'Sae [g]': Sae,'Sai [g]': Sai})
    
Tie = np.array(Tie)
Sae = np.array(Sae)
Sai = np.array(Sai)
Tie = Tie[:, 0]
Sae = Sae[:, 0]
Sai = Sai[:, 0]
    
    
fig1, ax1 = plt.subplots(figsize=(16/1.5, 9/1.5))                                                                

ax1.plot(Tie, Sae, color=(0, 0, 1), marker='+', markersize=0, markerfacecolor='w',                             
markeredgewidth=0, linewidth=1.0, alpha=0.5,linestyle = '-',label= f'Sa_elastic')
ax1.plot(Tie, Sai, color=(0, 0, 0), marker='+', markersize=0, markerfacecolor='w',                              
markeredgewidth=0, linewidth=1.5, alpha=0.7,linestyle = '--',label= f'Sa_inelastic')
ax1.set_xlim([Tie[0], (max(Tie))])                                                                               
ax1.set_ylim([0, (max(Sae)*1.05)])                                                                              
plt.title('UHS [NEC-SE-DS-2015]', fontsize=10, color=(0, 0, 1))                                                      
plt.xlabel('Period (T) [s]', rotation=0, fontsize=10, color=(0, 0, 0))                                          
plt.ylabel('Max Response Acceleration (Sa) [g]', rotation=90, fontsize=10, color=(0, 0, 0))                     
legend = plt.legend(fontsize=10)                                                                               
legend.get_frame().set_edgecolor('none')                                                                       
ax1.grid(which='both', axis='x', alpha=0.5)                                                                      
plt.show()   

    
    # return Resul, fig1, folder_path
