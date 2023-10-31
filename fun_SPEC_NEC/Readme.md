<div align="center">
    <img src="https://github.com/Normando1945/Normando1945.github.io/assets/62081230/1ac0bf1d-67cd-43f6-87b0-141417a606db">
</div>

>##### Author:                 [Msc. Ing. Carlos Andrés Celi Sánchez](https://www.researchgate.net/profile/Carlos-Celi). & [Phd(c). MSc. Ing. José Poveda](https://www.torrefuerte.com)

>##### Course:                 Structural Dynamics


### **You can find me on**
[![Web Page](https://img.shields.io/badge/Web%20Page-caceli.net-blue)](http:caceli.net)
[![GitHub Carlos Celi](https://img.shields.io/github/followers/Normando1945?label=follow&style=social)](https://github.com/Normando1945)
[![ResearchGate](https://img.shields.io/badge/-ResearchGate-00CCBB?style=social&logo=researchgate)](https://www.researchgate.net/profile/Carlos-Celi)
[![Google Scholar](https://img.shields.io/badge/-Google%20Scholar-4285F4?style=social&logo=google)](https://scholar.google.com.ec/citations?hl=es&user=yR4Gz7kAAAAJ)
<a href="Carlos Celi:normando1945@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-normando1945@gmail.com-blue?style=flat&logo=gmail"></a>

### Function: fun_Nec(n, z, I, fads, r, R, fip, fie, TR)

The `fun_Nec` function performs spectral calculations using the NEC-SE-DS-2015 Ecuadorian Code. It computes the Elastic and Inelastic Acceleration Response Spectra for a range of structural periods and visualizes the results. Moreover, the function saves the results and figures in a folder specific to the return period (`TR`) used.


<p align="center">
    <img src="https://github.com/Normando1945/Simple-Python-Functions-Collection/assets/62081230/37734b39-2ef5-4b71-a765-438173b8cf8f" alt="fun_Spec_B_Newmark_2023" width="50%">
</p>



#### Parameters:
- `n` (float): Ratio between expected accelerations, Sa(T=0.1s) and the PGA for the selected return period.
- `z` (float): Maximum acceleration on rock expected for the design earthquake, expressed as a fraction of gravity's acceleration.
- `I` (float): Importance factor.
- `fads` (list): List of soil amplification coefficients (fa,fs,fs).
- `r` (float): Amplification due to geographical location.
- `R` (float): Seismic resistance reduction factor.
- `fip` (float): Penalty for plan irregularity.
- `fie` (float): Penalty for elevation irregularity.
- `TR` (str): Return period, used in naming the results folder.


### Returns:
- `Resul` (DataFrame): Contains columns 'Period [s]', 'Sae [g]', and 'Sai [g]' representing the period, elastic response acceleration, and inelastic response acceleration respectively.
- `fig1` (matplotlib.figure.Figure): Figure object displaying the Elastic and Inelastic Acceleration Response Spectra (UHS).
- `folder_path` (str): Path to the created results folder named `Results_NEC_UHS_TR_XXXX` where `XXXX` is the target return period value.



### Functionality:
1. **Initialization and Preliminary Calculations**: Computes initial and cutoff periods (`To` and `Tc`). Initializes lists for storing results.
2. **Spectral Calculation Loop**: Iterates over a range of periods to compute elastic and inelastic response acceleration values based on given conditions.
3. **Conversion and Visualization**: Converts lists to arrays and DataFrames, followed by visualization using Matplotlib.
4. **Result and Figure Saving**: Saves the computed results and figure in a specified folder, with names reflecting the target return period (`TR`).


### Visualization:
- **Figure - UHS [NEC-SE-DS-2015]**: Plots both the Elastic and Inelastic Acceleration Response Spectra against structural periods, providing a clear visual distinction between them.


### Usage:
The `fun_Nec` function is essential for earthquake engineering practitioners, researchers, and students to understand and evaluate the seismic response based on the NEC-SE-DS-2015 Ecuadorian Code. It provides insights into how different factors and periods influence the spectral response of structures. Typical inputs might include:
- `n` = Ratio between expected accelerations, Sa(T=0.1s) and the PGA for the selected return period, e.g., 2.48.
- `z` = Maximum acceleration on rock expected for the design earthquake, expressed as a fraction of gravity's acceleration, e.g., 0.4.
- `I` = Importance factor based on the structure's functional use, e.g., 1.
- `fads` = List of soil amplification coefficients (fa,fs,fs), e.g., [1.2, 1.11, 1.11].
- `r`, `R`, `fip`, `fie` = Various factors as per the design code.
- `TR` = Target return period, e.g., "475 years".

**Note**: The function not only computes and visualizes the spectra but also neatly saves them for future reference. For those who wish to further understand or extend this analysis, refer to the NEC-SE-DS-2015 guidelines and standards.


