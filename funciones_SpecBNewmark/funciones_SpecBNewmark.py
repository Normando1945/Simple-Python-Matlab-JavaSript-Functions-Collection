import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpld3
from mpld3 import plugins
from IPython.display import HTML
import os


def fun_Spec_B_Newmark_2023(To, Tf, dT, zi, xo, xvo, TG, SG, record):
        
        Sa = []                                                                 # Initialize array of max response acceleration 
        Sv =[]                                                                  # Initialize array of max response velocity 
        Sd = []                                                                 # Initialize array of max response displacement
        Period = []                                                             # Initialize array of Structural's Periods
        for T in np.arange(To, Tf, dT):    
                M = 1                                                           # Unit mass
                ti = TG                                                         # Change of variable
                dt = ti[1] - ti[0]                                              # Interval of time
                K = (2 * np.pi / T) ** 2 * M                                    # Calculate the stiffness
                xn1 = np.zeros((len(SG), 1))                                    # Initialize array of response displacement 
                xvn1 = np.zeros((len(SG), 1))                                   # Initialize array of response velocity 
                xan1 = np.zeros((len(SG), 1))                                   # Initialize array of response acceleration
                at = np.zeros((len(SG), 1))                                     # Initialize array of response displacement 
                xn1[0, 0] = xo                                                  # Set initial conditions of response displacement
                xvn1[0, 0] = xvo                                                # Set initial conditions of response velocity
                w = 2*np.pi/T                                    
                xan1[0, 0] = ((-SG[0] * M) - 2 * zi * w* xvo - (w) ** 2 * xo) * 1 / M
                # Calculate response B- Nwemark
                for i in range(1, len(SG)):
                        xn1[i, 0] = xn1[i - 1, 0] + (dt * xvn1[i - 1, 0]) + (dt ** 2 / 2 * xan1[i - 1, 0])
                        xan1[i, 0] = 1 / (M + (1 / 2) * (   2 * zi * (w) * M * dt)) * ((-SG[i] * M) - K * xn1[i] - 2 * zi * (w) * M * (xvn1[i - 1] + dt * (1 - (1 / 2)) * xan1[i - 1]))
                        xvn1[i, 0] = xvn1[i - 1, 0] + dt * ((1 - (1 / 2)) * xan1[i - 1, 0] + (1 / 2) * xan1[i, 0])
                        at[i, 0] = xan1[i, 0] + SG[i][0]

                Sa.append(np.max(np.abs(at)))
                Sv.append(np.max(np.abs(xvn1)))
                Sd.append(np.max(np.abs(xn1)))
                Period.append(T)
        Sa = list(Sa)
        Sv = list(Sv)
        Sd = list(Sd)
        Period =  list(Period)
        #Resul = pd.DataFrame({ 'Period (T) [s]': Period.flatten(),'Max Acceleration Response (Sa) [g]': Sa.flatten(),'Max Velocity Response (Sv) [A]': Sv.flatten(), 'Max Displacement Resmponse (Sd) [A]': Sd.flatten()})
        SPEC_e = 1
        
 
        ti =  list(TG)
        Sgg = list(SG)

        Sgabs = abs(np.array(Sgg))
        mindi = np.argmax(abs(Sgabs)) 
        maxTime = ti[mindi]
        maxAccel = Sgg[mindi]
        fs  = 1 # scale factor for plot's
        fig2, ax2 = plt.subplots(figsize=(16/1.5, 9/1.5))
        # Figure 2 - Seismic Record
        ax2.plot(ti, Sgg, color=(0, 0, 1), marker='+', markersize=0, markerfacecolor='w',
                markeredgewidth=0, linewidth=0.5, alpha=0.5, label='Seismic Record')
        ax2.plot(maxTime, maxAccel, color=(0, 0, 0), marker='o', markersize=4, markerfacecolor='b',
                markeredgewidth=1, linewidth=1, alpha=0.5, label='PGA')
        ax2.set_xlim([0, (max(ti))])
        ax2.set_title(f'Seismic Record  ({record})', fontsize=10, color=(0, 0, 1))
        ax2.set_xlabel('Time [s]', rotation=0, fontsize=10, color=(0, 0, 0))
        ax2.set_ylabel('Amplitude [g]', rotation=90, fontsize=10, color=(0, 0, 0))
        legend = ax2.legend(fontsize=10)
        legend.get_frame().set_edgecolor('none')
        ax2.grid(which='both', axis='x', alpha=0.5)
        ax2.axvline(x=maxTime, color=(1, 0, 0), alpha=0.5,                                          
                linewidth=0.8, linestyle='dashed')  
        ax2.text(maxTime*1.05, maxAccel.item(),                                                        
                f"Max acceleration (PGA): {maxAccel.item():.2f} g", ha='left', va='bottom', rotation=0, color=(0, 0, 0), alpha=1)
        plt.show()
        
        
        fig1, ax1 = plt.subplots(figsize=(16/1.5, 9/1.5))                                                                       # Create a figure and an axes object

        line, = ax1.plot(Period, Sa, color=(0, 0, 1), marker='+', markersize=0, markerfacecolor='w',                            # Plot the Acceleration Response Spectra
        markeredgewidth=0, linewidth=1.0, alpha=0.5,label= f'Sa_e')
        ax1.fill_between(Period, Sa, color=(0, 0, 1), alpha=0.3, hatch='///', edgecolor='k', facecolor='w')                     # Add a fill between the curve and the x-axis with a diagonal line patter

        ax1.set_xlim([Period[0], (max(Period))])                                                                                        # Set the x-axis limits from 0 to the maximum value in Period
        Sa_clean = np.nanmax([value for value in Sa if np.isfinite(value)])
        ax1.set_ylim([0, Sa_clean*1.05])                                                                                        # Set the x-axis limits from 0 to the maximum value in Period
        plt.title(f'Acceleration Response Spectra  ({record})', fontsize=10, color=(0, 0, 1))                                   # Set the title of the plot to 'Acceleration Response Spectra'
        plt.xlabel('Period (T) [s]', rotation=0, fontsize=10, color=(0, 0, 0))                                                  # Set the x-axis label to 'Period (T) [s]'
        plt.ylabel('Max Response Acceleration (Sa) [g]', rotation=90, fontsize=10, color=(0, 0, 0))                             # Set the y-axis label to 'Max Response Acceleration (Sa) [g]'
        legend = plt.legend(fontsize=10)                                                                                        # Add a legend to the plot with a font size of 10
        legend.get_frame().set_edgecolor('none')                                                                                # Remove the frame from the legend
        ax1.grid(which='both', axis='x', alpha=0.5)                                                                             # Add gridlines to both the x and y axis

        # Add a draggable vertical line and a text box to display Sa at the current position
        linepos = ax1.axvline(x=Period[0], color=(1, 0, 0), linestyle='--',linewidth=0.9, alpha=0.7) # Create a vertical line at the first period value
        textbox = ax1.text(0.75, 0.5, '', transform=ax1.transAxes, fontsize=10, color='black', ha='left', va='top', bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=0.5))
        point, = ax1.plot([], [], color=(0, 0, 0), marker='o', markersize=6, markerfacecolor='w',                               # Plot the Acceleration Response Spectra
        markeredgewidth=1, linewidth=1.0, alpha=1)

        def update_annotation(pos):
                index = np.argmin(np.abs(Period - pos))
                linepos.set_xdata(pos)
                textbox.set_text(f'T = {Period[index]:.2f} [s], Sa = {Sa[index]:.2f} [g]')
                textbox.set_position((0.75, 0.5))
                point.set_data([Period[index]], [Sa[index]])

        def on_click(event):
                if event.inaxes != ax1:
                        return
                update_annotation(event.xdata)
                fig1.canvas.draw_idle()
        
        def on_motion(event):
                if event.inaxes != ax1:
                        return
                update_annotation(event.xdata)
                fig1.canvas.draw_idle()

        fig1.canvas.mpl_connect('button_press_event', on_click)
        fig1.canvas.mpl_connect('motion_notify_event', on_motion)
        
          
        plt.show()
        
        SpecE = np.column_stack((Period, Sa))
        rec = np.column_stack((TG,SG))
        
        current_directory = os.getcwd()
        folder_name = 'Results_' + record
        folder_path = os.path.join(current_directory, folder_name)

        if not os.path.exists(folder_path):
                os.makedirs(folder_path)

        file_path1 = os.path.join(folder_path, 'rec_' + record + '.AT2')
        file_path2 = os.path.join(folder_path, 'rec_' + record + '_SPECe_ORD_' + '.AT2')

        np.savetxt(file_path1, rec, delimiter='\t', fmt='%.6f')
        np.savetxt(file_path2, SpecE, delimiter='\t', fmt='%.6f')
        print('\x1b[1;34m  Folder Path =', folder_path)
        
   
        return Period, Sa, Sd, Sv, fig2, fig1, ax2, ax1, line, linepos, textbox, point, folder_path