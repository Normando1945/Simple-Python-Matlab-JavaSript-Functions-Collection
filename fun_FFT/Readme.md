<div align="center">
    <img src="https://github.com/Normando1945/Normando1945.github.io/assets/62081230/1ac0bf1d-67cd-43f6-87b0-141417a606db" alt="FFT Analysis">
</div>

>##### Author: [Msc. Ing. Carlos Andrés Celi Sánchez](https://www.researchgate.net/profile/Carlos-Celi). & [Phd(c). MSc. Ing. José Poveda](https://www.torrefuerte.com)

>##### Course: Structural Dynamics / Signal Processing


### **You can find me on**
[![Web Page](https://img.shields.io/badge/Web%20Page-caceli.net-blue)](http://caceli.net)
[![GitHub Carlos Celi](https://img.shields.io/github/followers/Normando1945?label=follow&style=social)](https://github.com/Normando1945)
[![ResearchGate](https://img.shields.io/badge/-ResearchGate-00CCBB?style=social&logo=researchgate)](https://www.researchgate.net/profile/Carlos-Celi)
[![Google Scholar](https://img.shields.io/badge/-Google%20Scholar-4285F4?style=social&logo=google)](https://scholar.google.com.ec/citations?hl=es&user=yR4Gz7kAAAAJ)
<a href="mailto:normando1945@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-normando1945@gmail.com-blue?style=flat&logo=gmail"></a>

### Function: fun_FFT_2024(at2_files, select_record, record)

This Python function processes AT2 seismic record files to extract the acceleration signal, compute the Fast Fourier Transform (FFT) to identify the dominant frequency and peak ground acceleration (PGA), and generate visualizations in both the time and frequency domains. The computed results, along with the plots, are saved in a dedicated folder.

<p align="center">
    <img src="https://github.com/Normando1945/Simple-Python-Matlab-JavaSript-Functions-Collection/assets/62081230/fft_visualization_example.png" alt="fun_FFT_2024" width="50%">
</p>

#### Parameters:
- `at2_files` (list of str): List of file paths for the AT2 seismic record files.
- `select_record` (int): Number of files to process from the provided list.
- `record` (str): Identifier for the seismic record used for labeling plots and saving the results.

#### Returns:
- `REC` (DataFrame): DataFrame containing two columns, 'Time' and 'Acceleration', extracted from the seismic record.
- `time` (numpy array): Array of time values corresponding to the seismic record.
- `accel` (list): List of acceleration values extracted from the AT2 file.
- `RESULT` (DataFrame): DataFrame containing the frequency spectrum, with columns for frequencies and their corresponding FFT amplitudes.

#### Functionality:
1. **Data Extraction and Preprocessing**:  
   - Reads the provided AT2 files and extracts the acceleration data along with the time increment (DT) from the file header.
   - Constructs the time vector based on the DT value and combines it with the acceleration data into a structured DataFrame.
2. **FFT Computation**:  
   - Computes the Fast Fourier Transform (FFT) of the acceleration signal.
   - Sorts the frequency components, isolates the positive frequencies, and identifies the dominant frequency (i.e., the frequency with the maximum amplitude).
3. **Visualization and Annotation**:
   - **Time Domain Plot**: Plots the seismic record, highlighting the peak ground acceleration (PGA) with an annotated marker and a dashed vertical line at the occurrence time.
   - **Frequency Domain Plot**: Displays a semilog plot of the FFT amplitude spectrum with a marker indicating the dominant frequency.
4. **Results Saving**:
   - Creates a results folder (named as `Results_FFT_<record>.file`) if it does not exist.
   - Saves the generated time-domain and frequency-domain plots as PNG images within this folder.

#### Visualization:
- **Figure 1 - Time Domain**:  
  Illustrates the seismic record over time, marking the point of maximum acceleration (PGA) with annotations for clarity.
- **Figure 2 - Frequency Domain**:  
  Shows the FFT amplitude spectrum on a semilog scale, emphasizing the dominant frequency component with a distinct marker and label.

#### Usage:
This function is particularly useful for researchers, engineers, and students in seismic engineering and signal processing. By combining both time-domain and frequency-domain analyses, it provides a comprehensive overview of the seismic data, facilitating the identification of key signal characteristics such as the dominant frequency and peak acceleration.
