import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
import matplotlib
from IPython.display import display



def SHM_animation(R, phi, w, T):
    
    matplotlib.rcParams['animation.embed_limit'] = 50  # Establece el límite en 50 MB

    w2 = 2*w
    T2 = 2*T
    R2 = 2*R
    phi2 = phi

    fig = plt.figure(figsize=(30, 7))
    
    ax1 = fig.add_subplot(1, 3, 1)
    ax1.set_xlim(-1.1, 1.1)
    ax1.set_ylim(-1.1, 1.1)
    ax1.set_aspect('equal', 'box')
    ax1.axis('off')
    ax1.grid(False)
    ax1.axhline(y=0, color=(0, 0, 0), marker='+', linestyle = '--', markersize=0, markerfacecolor='w', markeredgewidth=0, linewidth=1, alpha=1)
    ax1.axvline(x=0, color=(0, 0, 0), marker='+', linestyle = '--', markersize=0, markerfacecolor='w', markeredgewidth=0, linewidth=1, alpha=1)
    ax1.set_title(f'Simple Harmonic System, $ \omega_n $  = {w:.2f}, f = {w/np.pi:.2f} [Hz], T = {np.pi/w:.2f} [s]', fontsize=10, color=(0, 0, 1))
    text_label = ax1.text(0, 0, "", ha='left', va='bottom', rotation=0, weight='bold')
    circle = plt.Circle((0, 0), R, fill=False, color=(0, 0, 0), linewidth=3, alpha=1,label= f'SHM, **$ \omega $**  = {w:.2f} %')       
    ax1.add_artist(circle)
    
    
    ax2 = fig.add_subplot(1, 3, 2)
    ax2.set_xlim(-1.1, 1.1)
    ax2.set_ylim(-1.1, 1.1)
    ax2.set_aspect('equal', 'box')
    ax2.axis('off')
    ax2.grid(False)
    ax2.axhline(y=0, color=(0, 0, 0), marker='+', linestyle = '--', markersize=0, markerfacecolor='w', markeredgewidth=0, linewidth=1, alpha=1)
    ax2.axvline(x=0, color=(0, 0, 0), marker='+', linestyle = '--', markersize=0, markerfacecolor='w', markeredgewidth=0, linewidth=1, alpha=1)
    ax2.set_title(f'Simple Harmonic System, $ \omega_n $  = {w2:.2f}, f = {w2/np.pi:.2f} [Hz], T = {np.pi/w2:.2f} [s]', fontsize=10, color=(0, 0, 1))
    text_label22 = ax2.text(0, 0, "", ha='left', va='bottom', rotation=0, weight='bold')
    circle2 = plt.Circle((0, 0), R2, fill=False, color=(0, 0, 0), linewidth=3, alpha=1,label= f'SHM, **$ \omega $**  = {w2:.2f} %')       
    ax2.add_artist(circle2)


    ax3 = fig.add_subplot(1, 3, 3)
    ax3.set_box_aspect(9/20)
    ax3.set_xlim(0, 2*np.pi/w)
    ax3.set_ylim(-R2, R2)
    ax3.axhline(y=0, color=(0, 0, 0), marker='+', linestyle = '--', markersize=0, markerfacecolor='w', markeredgewidth=0, linewidth=1, alpha=1)
    ax3.set_ylabel('Amplitude [X]', rotation=90, fontsize=10, color=(0, 0, 0))
    ax3.set_xticks(np.arange(0, 100, 1))
    ax3.grid(which='both', axis='x', alpha=0.5)
    ax3.set_title(f'Displacement Response (SHM)', fontsize=10, color=(0, 0, 1))
    text2_label = ax3.text(0, 0, "", ha='left', va='bottom', rotation=0, weight='bold')
    text21_label = ax3.text(0, 0, "", ha='left', va='bottom', rotation=0, weight='bold')
    

    line, = ax1.plot([], [], color=(0, 0, 1), marker='+', linestyle = '-', markersize=0, markerfacecolor='w', markeredgewidth=0, linewidth=1, alpha=1)
    dot, = ax1.plot([], [], color=(0, 0, 1), marker='o', linestyle = '-', markersize=10, markerfacecolor=(1,0,0), markeredgecolor=(0,0,0),markeredgewidth=1,linewidth=1, alpha=1)
    textx, = ax1.plot([], [], color=(0, 0, 1), marker='o', linestyle = '-', markersize=5, markerfacecolor=(0,0,0), markeredgecolor=(0,0,0),markeredgewidth=1,linewidth=1, alpha=1)
    
    line22, = ax2.plot([], [], color=(0.3, 0.3, 0.3), marker='+', linestyle = '-', markersize=0, markerfacecolor='w', markeredgewidth=0, linewidth=1, alpha=1)
    dot22, = ax2.plot([], [], color=(0, 0, 1), marker='o', linestyle = '-', markersize=10, markerfacecolor=(1,0,0), markeredgecolor=(0,0,0),markeredgewidth=1,linewidth=1, alpha=1)
    textx22, = ax2.plot([], [], color=(0, 0, 1), marker='o', linestyle = '-', markersize=5, markerfacecolor=(0,0,0), markeredgecolor=(0,0,0),markeredgewidth=1,linewidth=1, alpha=1)

    hline, = ax1.plot([], [], color=(0, 0, 1), marker='+', linestyle = '--', markersize=0, markerfacecolor='w', markeredgewidth=0, linewidth=1, alpha=0.5)                                 
    vline, = ax1.plot([], [], color=(0, 0, 0), marker='+', linestyle = '--', markersize=0, markerfacecolor='w', markeredgewidth=0, linewidth=1, alpha=0)
    hline22, = ax2.plot([], [], color=(0, 0, 0), marker='+', linestyle = '--', markersize=0, markerfacecolor='w', markeredgewidth=0, linewidth=1, alpha=0.5)                                 
    vline22, = ax2.plot([], [], color=(0, 0, 0), marker='+', linestyle = '--', markersize=0, markerfacecolor='w', markeredgewidth=0, linewidth=1, alpha=0)

    time_data = []
    amplitude_data = []
    amplitude_data2 = []
    line2, = ax3.plot([], [], color=(0, 0, 1), marker='+', linestyle = '-', markersize=0, markerfacecolor='w', markeredgewidth=0, linewidth=1, alpha=0.5)
    dot2, = ax3.plot([], [], color=(0, 0, 1), marker='o', linestyle = '-', markersize=5, markerfacecolor=(0,0,0), markeredgecolor=(0,0,0),markeredgewidth=1,linewidth=1, alpha=1)
    line21, = ax3.plot([], [], color=(0.3, 0.3, 0.3), marker='+', linestyle = '-', markersize=0, markerfacecolor='w', markeredgewidth=0, linewidth=1, alpha=1)
    dot21, = ax3.plot([], [], color=(0, 0, 1), marker='o', linestyle = '-', markersize=5, markerfacecolor=(0,0,0), markeredgecolor=(0,0,0),markeredgewidth=1,linewidth=1, alpha=1)
    line3, = ax3.plot([], [], color=(0, 0, 0), marker='+', linestyle = '--', markersize=0, markerfacecolor='w', markeredgewidth=0, linewidth=1, alpha=0.5)
    line31, = ax3.plot([], [], color=(0, 0, 0), marker='+', linestyle = '--', markersize=0, markerfacecolor='w', markeredgewidth=0, linewidth=1, alpha=0.5)

    def init():
        line.set_data([], [])
        dot.set_data([], [])
        textx.set_data([],[])
        hline.set_data([], [])
        vline.set_data([], [])
        
        line22.set_data([], [])
        dot22.set_data([], [])
        textx22.set_data([],[])
        hline22.set_data([], [])
        vline22.set_data([], [])
        
        line2.set_data([], [])
        dot2.set_data([],[])
        line21.set_data([], [])
        dot21.set_data([],[])
        line3.set_data([], [])
        line31.set_data([], [])
        return line, dot, hline, vline, textx, line2, dot2, hline22, vline22, textx22, line2, dot2, line21, dot21, line3, line31

    def update(t):
        for collection in ax1.collections:
            collection.remove()
            
        for collection in ax2.collections:
            collection.remove()  
              
        x = R * np.cos(w * t + phi)
        y = R * np.sin(w * t + phi)
        line.set_data([0, x], [0, y])
        dot.set_data(x, y)
        
        x2 = R2 * np.cos(w2 * t + phi2)
        y2 = R2 * np.sin(w2 * t + phi2)
        line22.set_data([0, x2], [0, y2])
        dot22.set_data(x2, y2)
        
        hline.set_data([x, x], [0, y])
        vline.set_data([0, x], [y, y])
        textx.set_data([x, x ],[0,0])
        
        hline22.set_data([x2, x2], [0, y2])
        vline22.set_data([0, x2], [y2, y2])
        textx22.set_data([x2, x2 ],[0,0])
        
        ax1.fill_between([0, x], [0, 0], [0, y], color=(0, 0, 1), alpha=0.1)
        ax2.fill_between([0, x2], [0, 0], [0, y2], color=(0.3, 0.3, 0.3), alpha=0.2)
        
        text_label.set_position((x*1.05, 0))
        text_label.set_text(f"X(t) = {x:.2f}")
        
        text_label22.set_position((x2*1.05, 0))
        text_label22.set_text(f"X(t) = {x2:.2f}")
        
        if x >= 0:
            text2_label.set_position((t, x*1.10))
            text21_label.set_position((t, x2*1.10))
        else:
            text2_label.set_position((t, x*0.90))
            text21_label.set_position((t, x2*0.90))
            
        text2_label.set_text(f"X(t) = {x:.2f}")
        text21_label.set_text(f"X(t) = {x2:.2f}")
        
        time_data.append(t)
        amplitude_data.append(x)
        amplitude_data2.append(x2)
        line2.set_data(time_data, amplitude_data)
        dot2.set_data(t, x)
        line21.set_data(time_data, amplitude_data2)
        dot21.set_data(t, x2)
        line3.set_data([t, t], [0, x])
        line31.set_data([t, t], [0, x2])
        ax3.set_xlim(min(time_data), max(time_data) + 0.1)
        ax3.set_xlabel(f'Time [s], t = {t:.2f} [s]', rotation=0, fontsize=10, color=(0, 0, 0), weight='bold')
        
        return line, dot, hline, vline, textx, text_label, line2, dot2, hline22, vline22, textx22, text_label22 ,line2, dot2, line21, dot21, line3
    
    ani = FuncAnimation(fig, update, frames=np.linspace(0, 3*T, 180), init_func=init, blit=True, interval=75)

    return ani