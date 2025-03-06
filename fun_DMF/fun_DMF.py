from scipy.signal import butter, lfilter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def DMF(REC, at2_file_name, lowcut, highcut, order, parts, percentage, scale_down, Tedificio, zimenor, zimayor, partes):

    ########################  Filtering the signal ########################################
    if isinstance(REC, pd.DataFrame):                                                                                               # Check if REC is a pandas DataFrame
        REC = REC.to_numpy()                                                                                                        # Convert REC to a numpy array
    if REC.shape[0] < 2:                                                                                                            # Check if REC has less than 2 rows
        raise ValueError("REC no tiene suficientes filas para calcular DT_value")                                                   # Raise an error if REC has insufficient rows
    DT_value = float(REC[1, 0]) - float(REC[0, 0])                                                                                  # Calculate the time difference between the first two rows
    sample_rate = 1 / float(DT_value)                                                                                               # Calculate the sample rate
    nyquist = 0.5 * sample_rate                                                                                                     # Calculate the Nyquist frequency
    low = lowcut / nyquist                                                                                                          # Normalize the lowcut frequency
    high = highcut / nyquist                                                                                                        # Normalize the highcut frequency
    b, a = butter(order, [low, high], btype='band')                                                                                 # Design a bandpass filter
    filtered_signal = lfilter(b, a, REC[:, 1])                                                                                      # Apply the filter to the signal
    time = np.arange(0, len(filtered_signal)*float(DT_value), float(DT_value))                                                      # Generate the time array
    rec1 = np.column_stack((time, filtered_signal))                                                                                 # Combine the time and filtered signal into one array

    ######################## Max Acceleration ########################################
    max_index = np.argmax(abs(rec1[:, 1]))                                                                                          # Find the index of the maximum acceleration value
    max_acceleration = rec1[max_index, 1]                                                                                           # Get the maximum acceleration value
    max_time = rec1[max_index, 0]                                                                                                   # Find the time corresponding to the maximum acceleration value

    ###################################################################################################################################################################################################
    ###################################################################################################################################################################################################
    ############################################################################## Perform the FFT ####################################################################################################
    ###################################################################################################################################################################################################
    ###################################################################################################################################################################################################
    signal = rec1[:, 1]                                                                                                             # Extract the filtered signal
    fft = np.fft.fft(signal)                                                                                                        # Perform the FFT on the signal
    frequencies = np.fft.fftfreq(signal.size, time[1]-time[0])                                                                      # Get the frequency values for each component
    idx = np.argsort(frequencies)                                                                                                   # Sort the frequencies and FFT values in ascending order
    frequencies = frequencies[idx]                                                                                                  # Sort the frequencies
    fft = fft[idx]                                                                                                                  # Sort the FFT values

    mask = frequencies > 0                                                                                                          # Create a mask for positive frequencies
    positive_frequencies = frequencies[mask]                                                                                        # Apply the mask to get positive frequencies
    positive_amplitudes = fft[len(positive_frequencies)+1:len(fft)]                                                                 # Get the corresponding FFT values for positive frequencies

    frequencies = positive_frequencies                                                                                              # Update frequencies to positive frequencies
    fft = positive_amplitudes[0:len(frequencies)]                                                                                   # Update FFT values to positive amplitudes

    ###################################################################################################################################################################################################
    ###################################################################################################################################################################################################
    ######################################################################### Function Plot ###########################################################################################################
    ###################################################################################################################################################################################################
    ###################################################################################################################################################################################################

    ################################################## Function to update the plot using the input of the slider ##################################################
    numadf = parts                                                                                                                  # Number of frequencies to plot
    ########### number of frequencies to plot ###########
    frequenciess = frequencies[0:int(numadf)]                                                                                       # Select the first 'numadf' frequencies

    ########### number of amplitudes of each frequency to plot ###########
    ffts = fft[0:numadf]                                                                                                            # Select the first 'numadf' FFT values

    ################################################# Create a figure and an Axes3D object ##################################################
    fig = plt.figure(figsize=(9, 9))                                                                                                # Create a figure
    ax = fig.add_subplot(111, projection='3d')                                                                                      # Add a 3D subplot
    ax.set_aspect('auto')                                                                                                           # Set the aspect ratio to auto

    ax.plot(time, 0 * np.ones(time.shape), signal, color=(0, 0, 1), marker='+', markersize=0, markerfacecolor='w', 
            markeredgewidth=1, linewidth=0.9, alpha=0.3, label='Original Signal')                                                   # Plot the original signal

    # Plot each frequency component individually
    for f, c in zip(frequenciess, ffts):
        if f > 0:                                                                                                                   # Only plot positive frequencies
            ax.plot(time, (f * np.ones(time.shape)), scale_down * c.real * np.exp(-2j * np.pi * f * time), 
                    color=(0, 0, 0), marker='+', markersize=0, markerfacecolor='w', markeredgewidth=1, 
                    linewidth=1, alpha=0.2, label=f'{f:.2f} Hz')                                                                    # Plot the frequency component

    ax.set_title(f'Frequencies of a Signal in Time Domain [FFT]  ({at2_file_name})', fontsize=10, color=(0, 0, 1))                  # Set the title of the plot to the name of the AT2 file
    ax.set_xlabel('Time [s]', rotation=0, fontsize=7)                                                                               # Set the x-axis label
    ax.set_ylabel('Frequency [Hz]', rotation=0, fontsize=7)                                                                         # Set the y-axis label
    ax.set_zlabel('Amplitude', rotation=0, fontsize=7)                                                                              # Set the z-axis label
    ax.view_init(elev=16, azim=-35)                                                                                                 # Set the view angle
    ax.grid(False)                                                                                                                  # Disable the grid
    ax.xaxis.pane.fill = False                                                                                                      # Disable the x-axis pane fill
    ax.yaxis.pane.fill = False                                                                                                      # Disable the y-axis pane fill
    ax.zaxis.pane.fill = False                                                                                                      # Disable the z-axis pane fill

    plt.tight_layout()                                                                                                              # Adjust the layout
    plt.show()                                                                                                                      # Show the plot


    ###################################################################################################################################################################################################
    ###################################################################################################################################################################################################
    ######################################################################### Predominat Frecuencies ##################################################################################################
    ###################################################################################################################################################################################################
    ###################################################################################################################################################################################################
    maxAmp = []                                                                                                                     # Initialize an empty list to store the maximum amplitudes
    kk = 1                                                                                                                          # Initialize a counter variable
    for i in range(1, len(frequencies), len(frequencies)//(parts)):                                                                 # Loop through the frequencies in steps of len(frequencies)//parts
        maxAmp.append(max(np.abs(fft[kk:kk+len(frequencies)//(parts)])))                                                            # Append the maximum amplitude in the current segment to maxAmp
        kk = kk+len(frequencies)//parts                                                                                             # Update the counter variable
    maxAmp = np.array(maxAmp)                                                                                                       # Convert maxAmp to a numpy array

    fft_amp = []                                                                                                                    # Initialize an empty list to store the indices of the maximum amplitudes
    for amp in maxAmp:                                                                                                              # Loop through the maximum amplitudes
        fft_amp.append(np.where(np.abs(fft) == amp)[0][0])                                                                          # Find the index of the current amplitude in the fft array and append it to fft_amp
    fft_amp = np.array(fft_amp)                                                                                                     # Convert fft_amp to a numpy array

    frequencies_amp = frequencies[fft_amp]                                                                                          # Get the frequencies corresponding to the maximum amplitudes
    frequencies_amp = np.array(frequencies_amp)                                                                                     # Convert frequencies_amp to a numpy array

    ratio = np.zeros(len(maxAmp))                                                                                                   # Initialize an array to store the ratio between predominant frequencies and pulse energy
    for i in range(len(maxAmp)):                                                                                                    # Loop through the maximum amplitudes
        ratio[i] = maxAmp[i] * 100 / sum(maxAmp)                                                                                    # Calculate the ratio for the current amplitude

    ################################# Plot the frequency and amplitude on a semi-log x-axis #######################################

    #### SemiLogX #####
    fig, ax = plt.subplots(figsize=(16/1.5, 9/1.5))                                                                                 # Create a figure and an axis

    plt.semilogx(frequencies, np.abs(fft), color=(0, 0, 1), marker='+', markersize=0,                                               # Plot the FFT on a semi-log x-axis
                    markerfacecolor='w', markeredgewidth=1, linewidth=1, alpha=0.3)                                                 # Set the plot parameters

    for i in range(len(maxAmp)):                                                                                                    # Loop through the maximum amplitudes
        plt.semilogx(frequencies_amp[i], maxAmp[i], color=(                                                                         # Plot the maximum amplitudes on the semi-log x-axis
            0, 0, 0), marker='o', markersize=3, markerfacecolor='k', markeredgewidth=1, linewidth=1, alpha=0.9)                     # Set the plot parameters

    for i in range(len(maxAmp)):                                                                                                    # Loop through the maximum amplitudes
        ax.axvline(x=frequencies_amp[i], color='k',                                                                                 # Plot a vertical line at the current frequency value
                    linestyle='--', alpha=0.5, linewidth=0.5)                                                                       # Set the plot parameters
        ax.text(frequencies_amp[i]*1.05, maxAmp[i], f'{frequencies_amp[i]:.2f} Hz',                                                 # Add a text label at the current frequency value
                rotation=45, verticalalignment='bottom', alpha=1, fontsize=7)                                                       # Set the plot parameters

    plt.title(f'Frequency and Amplitude [FFT]  ({at2_file_name})', fontsize=10, color=(0, 0, 1))                                    # Set the title of the plot to the name of the AT2 file
    plt.xlabel('Frequency [Hz]', rotation=0, fontsize=7)                                                                            # Set the x-axis label
    plt.ylabel('Amplitude', rotation=90, fontsize=7)                                                                                # Set the y-axis label
    plt.xlim([min(frequencies), max(frequencies)])                                                                                  # Set the x-axis limits
    plt.show()                                                                                                                      # Show the plot
    plt.yticks([])                                                                                                                  # Remove the y-axis ticks
    plt.tight_layout()                                                                                                              # Adjust the layout

    ################################# Plot the frequency and pulse ###########################################

    bar_x_coords = range(len(frequencies_amp))                                                                                      # Set the x-coordinates for the bars
    fig, ax = plt.subplots(figsize=(16/1.5, 9/1.5))                                                                                 # Create a figure and an axis

    ax.bar(bar_x_coords, ratio, 0.4, color=(0, 0, 1), alpha=0.5)                                                                    # Plot the ratio as a bar plot
    ax.bar(bar_x_coords, frequencies_amp, 0.4,                                                                                      # Plot the frequencies as a bar plot
            bottom=ratio, color=(0, 0, 0), alpha=0.5)                                                                               # Set the plot parameters

    label_x_coords = [x + 0.45 for x in bar_x_coords]                                                                               # Set the x-coordinates for the labels
    label_y_coords = [ratio[i]*0.8 for i in range(len(frequencies_amp))]                                                            # Set the y-coordinates for the labels
    label_y2_coords = [(ratio[i] + frequencies_amp[i])                                                                              # Set the y-coordinates for the second set of labels
                        for i in range(len(frequencies_amp))]                                                                       # Loop through the frequencies

    # Add the labels to the plot
    for x, y, label in zip(label_x_coords, label_y_coords, ratio):                                                                  # Loop through the labels
        ax.text(x, y, str(round(label, 2)) + ' %', ha='center',                                                                     # Add the label to the plot
                va='center', rotation=90, fontsize=7, color=(0, 0, 1))                                                              # Set the plot parameters

    for x, y, label in zip(label_x_coords, label_y2_coords, frequencies_amp):                                                       # Loop through the second set of labels
        ax.text(x+0.3, y, str(round(label, 2)) +                                                                                    # Add the label to the plot
                ' [Hz]', ha='center', va='center', rotation=0, fontsize=7, color=(0, 0, 0))                                         # Set the plot parameters

    accumulated_ratio = np.cumsum(ratio)                                                                                            # Calculate the accumulated ratio

    indices = np.where(accumulated_ratio >= percentage)[0]                                                                          # Find the indices of the bars that contain at least the specified percentage of the accumulated ratio
    indices = indices[0]                                                                                                            # Get the first index
    ax.axvline(x=label_x_coords[indices] + 0.1,                                                                                     # Plot a vertical line at the specified index
                color='red', linestyle='dashed', linewidth=0.5)                                                                     # Set the plot parameters
    ax.text(label_x_coords[indices]+0.2, max(frequencies), f"Energy/Pulse >=: {percentage:.2f} [%]", ha='left',                     # Add a label to the plot to indicate the specified percentage of the ratio
            va='top', rotation=90, color=(1, 0, 0), alpha=0.9, fontsize=7)                                                          # Set the plot parameters

    plt.title(f'Relationship Between Predominant Frequencies and Energy / Pulse  ({at2_file_name})', fontsize=10, color=(0, 0, 1))  # Set the title of the plot to the name of the AT2 file
    plt.xlabel('number of secction of time = {}'.format(parts), rotation=0, fontsize=7)                                             # Set the x-axis label
    plt.xticks([])                                                                                                                  # Remove the x-axis ticks
    plt.yticks([])                                                                                                                  # Remove the y-axis ticks

    plt.tight_layout()                                                                                                              # Adjust the layout
    plt.show()                                                                                                                      # Show the plot

    useable_frecuencies = frequencies_amp[0:indices+1]                                                                              # Get the usable frequencies

    ###################################################################################################################################################################################################
    ###################################################################################################################################################################################################
    ######################################################################### Dynamic Magnification ###################################################################################################
    ###################################################################################################################################################################################################
    ###################################################################################################################################################################################################

    for j in range(len(useable_frecuencies)):                                                                                       # Loop through the usable frequencies
        fsignal = useable_frecuencies[j]                                                                                            # Get the current frequency
        w = 2*np.pi*fsignal                                                                                                         # Angular Frequency of the signal
        fedificio = 1/Tedificio                                                                                                     # Frequency of the building
        wn = 2*np.pi*fedificio                                                                                                      # Angular Frequency of the building
        alfa = 1                                                                                                                    # Initial line transparency
        linewid = 1.3                                                                                                               # Initial line thickness
        zI = np.linspace(zimenor, zimayor, num=partes)                                                                              # Generate a range of damping ratios

        fig, ax = plt.subplots(figsize=(16/1.5, 9/1.5))                                                                             # Create a figure and an axis
        find = []                                                                                                                   # Initialize an empty list to store indices
        for y in range(len(zI)):                                                                                                    # Loop through the damping ratios
            zi = zI[y]                                                                                                              # Get the current damping ratio
            incr = 0.005                                                                                                            # Increment for the ratio
            if w/wn <= 2:                                                                                                           # Check if the ratio is less than or equal to 2
                Fincr = 2                                                                                                           # Set the final increment value
            else:                                                                                                                   # If the ratio is greater than 2
                Fincr = w/wn + 0.2                                                                                                  # Set the final increment value
            ratio = np.zeros(int(Fincr/incr)+1)                                                                                     # Initialize an array to store the ratios
            Si = np.zeros(int(Fincr/incr)+1)                                                                                        # Initialize an array to store the magnification factors
            Siamort = np.zeros(int(Fincr/incr)+1)                                                                                   # Initialize an array to store the damped magnification factors
            for i in range(len(ratio)):                                                                                             # Loop through the ratios
                ratio[i] = i*incr                                                                                                   # Calculate the current ratio
                Si[i] = 1 / np.sqrt(((1 - (ratio[i])**2)) ** 2 + (2*zi*ratio[i])**2)                                                # Calculate the magnification factor
                Siamort[i] = ((1 + (2*zi*ratio[i])**2) / (((1 - (ratio[i])**2))**2 + (2*zi*ratio[i])**2))**0.5                      # Calculate the damped magnification factor
                if zi == zI[0]:                                                                                                     # Check if the current damping ratio is the first one
                    maxi = max(Si)                                                                                                  # Get the maximum magnification factor
            diff = np.abs(ratio - (w/wn))                                                                                           # Calculate the difference between the ratios and the current ratio
            index = np.where(diff == diff.min())[0]                                                                                 # Find the index of the minimum difference
            find = index                                                                                                            # Store the index
        
        ################################# Plot the frequency and amplitude on a semi-log x-axis #######################################

            ax.plot(w/wn, Si[find], color=(0, 0, 0), marker='+', markersize=1,                                                      # Plot the magnification factor
                    markerfacecolor='w', markeredgewidth=1, linewidth=linewid, alpha=alfa)                                          # Set the plot parameters
            ax.plot(w/wn, Siamort[find], color=(0, 0, 0), marker='*', markersize=2,                                                 # Plot the damped magnification factor
                    markerfacecolor='w', markeredgewidth=1, linewidth=linewid, alpha=alfa)                                          # Set the plot parameters
            if zi == 0.05:                                                                                                          # Check if the current damping ratio is 0.05
                ax.plot(ratio, Si, color=(0, 0, 1), marker='o',                                                                     # Plot the magnification factor
                        markersize=0, markerfacecolor='w', markeredgewidth=1, linewidth=linewid, alpha=alfa,                        # Set the plot parameters
                        label='$ \zeta $ ' + str(zi*100) + '% =' + str(Si[find]))                                                   # Set the label
                ax.plot(ratio, Siamort, color=(0, 0.5, 1), marker='o',                                                              # Plot the damped magnification factor
                        markersize=0, markerfacecolor='w', markeredgewidth=1, linewidth=linewid, alpha=alfa,                        # Set the plot parameters
                        label='$ \S $ ' + str(zi*100) + '% =' + str(Siamort[find]))                                                 # Set the label
            else:                                                                                                                   # If the current damping ratio is not 0.05
                ax.plot(ratio, Si, color=(0, 0, 0), marker='o', markersize=0, markerfacecolor='w', markeredgewidth=1, 
                        linewidth=linewid, alpha=alfa,                                                                              # Plot the magnification factor
                        label='$ \zeta $ ' + str(np.float16(zi*100)) + '% =' + str(Si[find]))                                       # Set the label
                ax.plot(ratio, Siamort, color=(1, 0.4, 0.6), marker='o', markersize=0, markerfacecolor='w', markeredgewidth=1, 
                        linewidth=linewid, alpha=alfa,                                                                              # Plot the damped magnification factor
                        label='$ \S $ ' + str(np.float16(zi*100)) + '% =' + str(Siamort[find]))                                     # Set the label

            plt.title(f'Dinamic Magnification $ \Psi $  ({at2_file_name})]', fontsize=10, color=(0, 0, 1))                          # Set the title of the plot
            plt.xlabel('$\omega / \omega_n $', rotation=0, fontsize=7)                                                              # Set the x-axis label
            plt.ylabel('$ \Psi $', rotation=360, fontsize=7)                                                                        # Set the y-axis label

            legend = plt.legend(fontsize=7)                                                                                         # Add a legend to the plot
            legend.get_frame().set_edgecolor('none')                                                                                # Set the legend frame edge color
            plt.xticks(np.arange(0, max(ratio), step=0.2), fontsize=7, rotation=0)                                                  # Set the x-axis ticks
            plt.yticks(fontsize=7, rotation=0)                                                                                      # Set the y-axis ticks
            if alfa >= 0.3:                                                                                                         # Check if the transparency is greater than or equal to 0.3
                alfa = abs(alfa - 1/partes)                                                                                         # Update the transparency
                linewid = abs(linewid - 3/partes)                                                                                   # Update the line width
            else:                                                                                                                   # If the transparency is less than 0.3
                alfa = 0.3                                                                                                          # Set the transparency to 0.3
                linewid = 0.3                                                                                                       # Set the line width to 0.3

        ax.axvline(x=w/wn, color='red', linestyle='dashed', linewidth=0.5)                                                          # Plot a vertical line at the current ratio
        ax.text(w/wn + 0.05, 10, f"Dinamic Magnification, f = {fsignal:2f} Hz", ha='left', va='top', rotation=90, color=(           # Add a text label to the plot
            1, 0, 0), alpha=0.9, fontsize=7)                                                                                        # Set the plot parameters
    plt.show()                                                                                                                      # Show the plot
