import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os


def fun_FFT_2024(at2_files, select_record, record):

    for i, at2_file in enumerate(at2_files[0:select_record]):
        with open(at2_file, 'r') as f:
            contents = f.read()
        lines = contents.split('\n')
        linex = lines[3]
        values = linex.split()
        indexx = values.index("DT=")
        DT_value = values[indexx + 1]
        accel = []
        for line in lines[4:]:
            values = line.split()
            if len(values) == 5:
                accel.extend(values)
        accel = [float(value) for value in accel]
        signal = accel
        time = np.arange(0, len(signal)*float(DT_value), float(DT_value))
        rec = np.column_stack((time, signal))

    REC = pd.DataFrame(rec, columns = ['Time', 'Acceleration'])
    
    
    fft = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(len(signal), time[1]-time[0])
    idx = np.argsort(frequencies)
    frequencies = frequencies[idx]
    fft = fft[idx]

    mask = frequencies > 0
    positive_frequencies = frequencies[mask]
    positive_amplitudes = fft[len(positive_frequencies)+1:len(fft)]

    frequencies = positive_frequencies
    fft = positive_amplitudes[0:len(frequencies)]

    max_amp_idx = np.argmax(np.abs(fft))
    corresponding_freq = frequencies[max_amp_idx]
    corresponding_amp = np.abs(fft[max_amp_idx])
    F = pd.DataFrame(frequencies, columns= ['Frequencies'])
    FFT = pd.DataFrame(np.abs(fft), columns= ['Amplitudes'])
    RESULT = pd.concat([F, FFT], axis=1, ignore_index=False)





##################################################################################################################################################################################################

    ti =  list(time)
    Sgg = list(accel)

    Sgabs = abs(np.array(Sgg))
    mindi = np.argmax(abs(Sgabs)) 
    maxTime = ti[mindi]
    maxAccel = Sgg[mindi]
            
    fig1, ax1 = plt.subplots(figsize=(16/1.5, 9/1.5))
    ax1.plot(ti, Sgg, color=(0, 0, 1), marker='+', markersize=0, markerfacecolor='w',
            markeredgewidth=0, linewidth=0.5, alpha=0.5, label='Seismic Record')
    ax1.plot(maxTime, maxAccel, color=(0, 0, 0), marker='o', markersize=4, markerfacecolor='b',
            markeredgewidth=1, linewidth=1, alpha=0.5, label='PGA')
    ax1.set_xlim([0, (max(ti))])
    ax1.set_title(f'Seismic Record, ({record})', fontsize=10, color=(0, 0, 1))
    ax1.set_xlabel('Time [s]', rotation=0, fontsize=10, color=(0, 0, 0))
    ax1.set_ylabel('Amplitude [g]', rotation=90, fontsize=10, color=(0, 0, 0))
    legend = ax1.legend(fontsize=10)
    legend.get_frame().set_edgecolor('none')
    ax1.grid(which='both', axis='x', alpha=0.5)
    ax1.axvline(x=maxTime, color=(1, 0, 0), alpha=0.5,                                          
            linewidth=0.8, linestyle='dashed')  
    ax1.text(maxTime*1.05, maxAccel,                                                        
            f"Max acceleration (PGA): {maxAccel:.2f} g", ha='left', va='bottom', rotation=0, color=(0, 0, 0), alpha=1)
    plt.show()
    
##################################################################################################################################################################################################

    fig2, ax2 = plt.subplots(figsize=(16/1.5, 9/1.5))                                                                 

    plt.semilogx(frequencies, np.abs(fft), color=(0, 0, 1), marker='o', markersize=0,                               
                markerfacecolor='w', markeredgewidth=1, linewidth=1, alpha=0.3)                                     
    plt.semilogx(corresponding_freq, corresponding_amp, color=(0, 0, 0), marker='o', markersize=5,                  
                markerfacecolor=(0, 0, 0), markeredgewidth=1, linewidth=1, alpha=1)                                 
    ax2.text(corresponding_freq*1.05, corresponding_amp, f'{corresponding_freq:.2f} [Hz]',                           
            fontsize=10, color=(0, 0, 0), verticalalignment='bottom')

    ax2.set_title(f'Frequency and Amplitude [FFT], ({record})', fontsize=10, color=(0, 0, 1))                                        
    ax2.set_xlabel('Frequency [Hz]', rotation=0, fontsize=7)                                                            
    ax2.set_ylabel('Amplitude', rotation=90, fontsize=7)                                                                
    ax2.set_xlim([min(frequencies), max(frequencies)])                                                                  
    ax2.grid(which='both', axis='x', linestyle='--', alpha=0.7)                                                     
    plt.show()                                                                                                      
    plt.yticks([])
    
    
    ##################################################################################################################################################################################################

    current_directory = os.getcwd()
    folder_name = 'Results_FFT_' + record + '.file'
    folder_path = os.path.join(current_directory, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    fig_path1 = os.path.join(folder_name, 'fig1_rec_' + record + '.png')
    fig_path2 = os.path.join(folder_name, 'fig2_FFT_' + record + '.png')
    fig1.savefig(fig_path1)
    fig2.savefig(fig_path2)

    
    # print('\x1b[1;34m  Directory of the function =', current_directory)
    # print('\x1b[1;34m  Folder Path =', folder_path)                                                                                                  
    
    return REC, time, accel, RESULT


        

 

  