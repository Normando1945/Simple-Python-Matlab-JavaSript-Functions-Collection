import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def fun_B_Newmark_2023(TG, SG, M, T, xo, xvo, zi):
    ti  = TG        
    dt = ti[1] - ti[0]
    K = (2 * np.pi / T) ** 2 * M
    
    xn1 = np.zeros((len(SG), 1))
    xvn1 = np.zeros((len(SG), 1))
    xan1 = np.zeros((len(SG), 1))
    at = np.zeros((len(SG), 1))
    
    xn1[0, 0] = xo
    xvn1[0, 0] = xvo
    xan1[0, 0] = ((-SG[0] * M) - 2 * zi * (2*np.pi / T) * M * xvo - (np.pi / T) ** 2 * xo) * 1 / M
    
    for i in range(1, len(SG)):
        xn1[i, 0] = xn1[i - 1, 0] + (dt * xvn1[i - 1, 0]) + (dt ** 2 / 2 * xan1[i - 1, 0])
        xan1[i, 0] = 1 / (M + (1 / 2) * (2 * zi * (2*np.pi / T) * M * dt)) * ((-SG[i] * M) - K * xn1[i] - 2 * zi * (2*np.pi / T) * M * (xvn1[i - 1] + dt * (1 - (1 / 2)) * xan1[i - 1]))
        xvn1[i, 0] = xvn1[i - 1, 0] + dt * ((1 - (1 / 2)) * xan1[i - 1, 0] + (1 / 2) * xan1[i, 0])
        at[i, 0] = xan1[i, 0] + SG[i][0]
    
    Xn1 = list(xn1)
    Xvn1 = list(xvn1)
    Xan1 = list(xan1)
    At =  list(at)
    ti =  list(TG)
    Sgg = list(SG)
    
    fs  = 1.15 
    fig1, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1, figsize=((16/fs)/1.5, (16/fs)/1.5))

    ax1.plot(ti, Sgg, color=(0, 0, 0), marker='+', markersize=0, markerfacecolor='w',
            markeredgewidth=0, linewidth=0.5, alpha=1.0, label='Seismic Record')
    ax1.set_xlim([0, (max(ti))])
    ax1.set_title('Seismic Record', fontsize=7, color=(0, 0, 1))
    ax1.set_xlabel('Time [s]', rotation=0, fontsize=7, color=(0, 0, 0))
    ax1.set_ylabel('Amplitude [g]', rotation=90, fontsize=7, color=(0, 0, 0))
    legend = ax1.legend(fontsize=7)
    legend.get_frame().set_edgecolor('none')
    ax1.grid(which='both', axis='x', alpha=0.5)

    ax2.plot(ti, xn1, color=(0, 0, 1), marker='+', markersize=0, markerfacecolor='w',
            markeredgewidth=0, linewidth=1, alpha=0.5, label='Displacement')
    ax2.set_xlim([0, (max(ti))])
    ax2.set_title('Displacement', fontsize=7, color=(0, 0, 1))
    ax2.set_xlabel('Time [s]', rotation=0, fontsize=7, color=(0, 0, 0))
    ax2.set_ylabel('Amplitude [X]', rotation=90, fontsize=7, color=(0, 0, 0))
    legend = ax2.legend(fontsize=7)
    legend.get_frame().set_edgecolor('none')
    ax2.grid(which='both', axis='x', alpha=0.5)

    ax3.plot(ti, xvn1, color=(1, 0, 0), marker='+', markersize=0, markerfacecolor='w',
            markeredgewidth=0, linewidth=1, alpha=0.5, label='Velocity')
    ax3.set_xlim([0, (max(ti))])
    ax3.set_title('Velocity', fontsize=7, color=(0, 0, 1))
    ax3.set_xlabel('Time [s]', rotation=0, fontsize=7, color=(0, 0, 0))
    ax3.set_ylabel('Amplitude [V]', rotation=90, fontsize=7, color=(0, 0, 0))
    legend = ax3.legend(fontsize=7)
    legend.get_frame().set_edgecolor('none')
    ax3.grid(which='both', axis='x', alpha=0.5)
        
    ax4.plot(ti, Sgg, color=(0, 0, 0), marker='+', markersize=0, markerfacecolor='w',                                
            markeredgewidth=0, linewidth=0.5, alpha=1.0,label= f'Seismic Record')
    ax4.plot(ti, Xan1, color=(0, 0, 1), marker='+', markersize=0, markerfacecolor='w',                               
            markeredgewidth=0, linewidth=0.5, alpha=0.5,label= f'Acceleration Response [B-Newmark]')
    ax4.plot(ti, At, color=(1, 0, 0), marker='+', linestyle = '--', markersize=0, markerfacecolor='w',               
            markeredgewidth=0, linewidth=0.5, alpha=0.5,label= f'Total Acceleration Response [B-Newmark]')
    ax4.set_xlim([0, (max(ti))])                                                                                     
    ax4.set_title('Acceleration', fontsize=7, color=(0, 0, 1))                                                         
    ax4.set_xlabel('Time [s]', rotation=0, fontsize=7, color=(0, 0, 0))                                                
    ax4.set_ylabel('Acceleration [g]', rotation=90, fontsize=7, color=(0, 0, 0))                                          
    ax4.grid(which='both', axis='x', alpha=0.5)   

    legend1 = ax4.legend(fontsize=7, loc='lower center', ncol=3)
    legend1.get_frame().set_edgecolor('none')                                                                      

    plt.tight_layout()  

    return Xn1, Xvn1, Xan1, At, ti, Sgg, dt, fig1