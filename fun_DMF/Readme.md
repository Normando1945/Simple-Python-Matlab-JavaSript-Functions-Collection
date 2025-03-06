<div align="center">
    <img src="https://github.com/Normando1945/Normando1945.github.io/assets/62081230/1ac0bf1d-67cd-43f6-87b0-141417a606db" alt="DMF Analysis">
</div>

>##### Author: [Msc. Ing. Carlos Andrés Celi Sánchez](https://www.researchgate.net/profile/Carlos-Celi). & [Phd(c). MSc. Ing. José Poveda](https://www.torrefuerte.com)

>##### Course: Structural Dynamics / Signal Processing

### **You can find me on**
[![Web Page](https://img.shields.io/badge/Web%20Page-caceli.net-blue)](http://caceli.net)
[![GitHub Carlos Celi](https://img.shields.io/github/followers/Normando1945?label=follow&style=social)](https://github.com/Normando1945)
[![ResearchGate](https://img.shields.io/badge/-ResearchGate-00CCBB?style=social&logo=researchgate)](https://www.researchgate.net/profile/Carlos-Celi)
[![Google Scholar](https://img.shields.io/badge/-Google%20Scholar-4285F4?style=social&logo=google)](https://scholar.google.com.ec/citations?hl=es&user=yR4Gz7kAAAAJ)
<a href="mailto:normando1945@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-normando1945@gmail.com-blue?style=flat&logo=gmail"></a>

### Function: DMF(REC, at2_file_name, lowcut, highcut, order, parts, percentage, scale_down, Tedificio, zimenor, zimayor, partes)

This Python function performs a comprehensive analysis of a seismic record by applying a Butterworth bandpass filter, computing its Fast Fourier Transform (FFT), and conducting a dynamic magnification study. It generates multiple visualizations that help in understanding the signal's frequency content, energy distribution, and the dynamic response characteristics relevant for seismic and structural analysis.



<p align="center">
    <img src="https://github.com/user-attachments/assets/132dd272-a4cc-4b5f-9a98-c45c800ebe0b" alt="DMF Function" width="100%">
</p>

#### Parameters:
- `REC` (DataFrame or numpy array): Seismic record data where the first column contains time values and the second column contains acceleration values.
- `at2_file_name` (str): Name of the AT2 file; used to label plots and output files.
- `lowcut` (float): Low cutoff frequency for the Butterworth bandpass filter.
- `highcut` (float): High cutoff frequency for the Butterworth bandpass filter.
- `order` (int): Order of the Butterworth filter, determining the filter’s roll-off steepness.
- `parts` (int): Number of segments into which the FFT spectrum is divided for predominant frequency analysis.
- `percentage` (float): Threshold percentage of cumulative energy used to select the usable predominant frequencies.
- `scale_down` (float): Scaling factor to adjust the amplitude of FFT components when overlaying on the 3D plot.
- `Tedificio` (float): Building period; used to compute the building's natural frequency.
- `zimenor` (float): Lower bound of the damping ratio range for dynamic magnification analysis.
- `zimayor` (float): Upper bound of the damping ratio range for dynamic magnification analysis.
- `partes` (int): Number of discrete points used in plotting the dynamic magnification curves.

#### Returns:
*(The function primarily generates visual plots and does not explicitly return data structures for further processing.)*

#### Functionality:
1. **Signal Filtering**:
   - **Input Conversion & DT Calculation**:  
     The function first checks if the seismic record (`REC`) is a DataFrame and converts it to a numpy array if needed. It then calculates the time increment (DT) from the first two time entries, which is critical for determining the sampling rate.
   - **Butterworth Bandpass Filtering**:  
     Using the `butter` and `lfilter` functions from `scipy.signal`, the function applies a bandpass filter to the acceleration data. The `lowcut` and `highcut` parameters define the frequency range of interest, while the `order` parameter controls the filter’s sharpness. This filtering step removes unwanted noise and isolates the frequency band relevant for subsequent analysis.
   - **Time Vector Reconstruction**:  
     A new time vector is generated based on the DT value and the length of the filtered signal, and the filtered data is reassembled into a new record.

2. **Maximum Acceleration Calculation**:
   - The function identifies the maximum absolute acceleration value (representing the peak ground acceleration, PGA) within the filtered signal and records the corresponding time. This information is essential for seismic analysis and further interpretation of the signal’s impact.

3. **FFT Computation**:
   - **Transformation to Frequency Domain**:  
     The function computes the FFT of the filtered signal, converting it from the time domain to the frequency domain.
   - **Frequency Sorting & Isolation**:  
     It then sorts the FFT results by frequency, isolates only the positive frequencies (which contain the meaningful spectral information for a real signal), and extracts the corresponding amplitude values. This step lays the groundwork for identifying dominant frequency components in the signal.

4. **3D Time-Frequency Plotting**:
   - **3D Visualization Setup**:  
     A 3D plot is created to display the evolution of the signal over time and frequency. The x-axis represents time, the y-axis displays frequency (with constant lines for each frequency component), and the z-axis shows the amplitude.
   - **Overlaying Frequency Components**:  
     The function overlays individual frequency components (scaled by `scale_down`) on the original filtered signal. This visualization helps in comprehending how different frequency components contribute to the overall signal over time.

5. **Predominant Frequency Analysis**:
   - **Segmentation of FFT Spectrum**:  
     The FFT spectrum is divided into segments based on the `parts` parameter. For each segment, the function finds the maximum amplitude, which is assumed to be the predominant frequency component within that segment.
   - **Energy Ratio Calculation**:  
     The maximum amplitudes are then used to calculate the energy ratio of each frequency segment. This ratio, expressed as a percentage, represents the contribution of each segment to the total energy.
   - **Spectrum Annotation and Bar Plot**:  
     The function generates a semilog plot of the FFT spectrum with vertical dashed lines and labels marking the predominant frequencies. Additionally, a bar plot is created to visualize the relationship between the relative energy (or pulse) and the corresponding frequencies, highlighting which segments contribute most to the overall energy.

6. **Dynamic Magnification Analysis**:
   - **Selection of Usable Frequencies**:  
     Based on the cumulative energy ratio (defined by the `percentage` parameter), the function selects the predominant frequencies that together account for the desired portion of the total energy.
   - **Calculation of Dynamic Magnification**:  
     For each usable predominant frequency, the function calculates the dynamic magnification factor (Ψ). It computes two sets of amplification factors using dynamic system response formulas over a range of normalized frequency ratios (ω/ωₙ) and damping ratios between `zimenor` and `zimayor`. The natural frequency of the building is determined from its period (`Tedificio`).
   - **Plotting Dynamic Magnification Curves**:  
     The dynamic magnification curves are plotted for different damping ratios. These plots illustrate how the building's response can be amplified under resonant conditions, providing valuable insights into potential structural vulnerabilities during seismic events.

#### Usage:
- **Input Requirements**:  
  - A well-formatted seismic record (`REC`) where the first column represents time and the second column represents acceleration.
  - Proper setting of filtering parameters (`lowcut`, `highcut`, `order`) to isolate the frequency band of interest.
  - Adequate segmentation (`parts`) of the FFT spectrum and a meaningful energy threshold (`percentage`) to identify predominant frequencies.
  - A defined scaling factor (`scale_down`) to appropriately visualize the FFT components.
  - Building-specific parameters (`Tedificio`, `zimenor`, `zimayor`, `partes`) to conduct the dynamic magnification analysis.
- **Application Context**:  
  This function is designed for use by seismic engineers, researchers, and students involved in signal processing and structural dynamics. It provides an integrated approach to analyze seismic records by filtering the data, transforming it into the frequency domain, identifying key frequency components, and evaluating how these frequencies can dynamically amplify the response of a structure. Such analyses are critical in understanding the potential impacts of seismic events on buildings and in designing structures to mitigate these effects.
