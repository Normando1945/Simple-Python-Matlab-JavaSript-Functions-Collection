<div align="center">
    <img src="https://github.com/Normando1945/Normando1945.github.io/assets/62081230/1ac0bf1d-67cd-43f6-87b0-141417a606db">
</div>

>##### Author:                 [Msc. Ing. Carlos Andrés Celi Sánchez](https://www.researchgate.net/profile/Carlos-Celi). & [Phd(c). MSc. Ing. José Poveda](https://www.torrefuerte.com)

>##### Course:                 Structural Dynamics


### **You can find me on**
[![GitHub Carlos Celi](https://img.shields.io/github/followers/Normando1945?label=follow&style=social)](https://github.com/Normando1945)
[![ResearchGate](https://img.shields.io/badge/-ResearchGate-00CCBB?style=social&logo=researchgate)](https://www.researchgate.net/profile/Carlos-Celi)
[![Google Scholar](https://img.shields.io/badge/-Google%20Scholar-4285F4?style=social&logo=google)](https://scholar.google.com.ec/citations?hl=es&user=yR4Gz7kAAAAJ)
<a href="Carlos Celi:normando1945@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-normando1945@gmail.com-blue?style=flat&logo=gmail"></a>

### Function: fun_Spec_B_Newmark_2023(To, Tf, dT, zi, xo, xvo, TG, SG, record)

This Python function calculates the spectral response including acceleration, velocity, and displacement of a structure subjected to ground motion using a modified Newmark method.

<p align="center">
    <img src="https://github.com/Normando1945/Simple-Python-Functions-Collection/assets/62081230/a5d747fd-45e4-447e-ab21-71fa71f71224" alt="fun_Spec_B_Newmark_2023" width="50%">
</p>

#### Parameters:
- `To` (float): Initial period of the structure.
- `Tf` (float): Final period of the structure.
- `dT` (float): Step size for the period.
- `zi` (float): Damping ratio of the structure.
- `xo` (float): Initial displacement response.
- `xvo` (float): Initial velocity response.
- `TG` (list): Time vector of the motion history.
- `SG` (list of lists): Acceleration time history of the ground motion.
- `record` (string): Name or identifier for the seismic record.

#### Returns:
- `Period` (list): List of structural periods.
- `Sa` (list): Max response acceleration.
- `Sd` (list): Max response displacement.
- `Sv` (list): Max response velocity.
- `fig1` (matplotlib.figure.Figure): Figure object for seismic record plot.
- `fig2` (matplotlib.figure.Figure): Figure object for acceleration response spectra plot.
- `ax1` (matplotlib.axes.Axes): Axes object for seismic record plot.
- `ax2` (matplotlib.axes.Axes): Axes object for acceleration response spectra plot.
- `line` (matplotlib.lines.Line2D): Line2D object for spectra plot.
- `linepos` (matplotlib.lines.Line2D): Line2D object for draggable line.
- `textbox` (matplotlib.text.Text): Text object for displaying values.
- `point` (matplotlib.lines.Line2D): Line2D object for marker point.

#### Functionality:
1. **Initialization**: Sets up parameters, initializes arrays for response calculation, and calculates stiffness.
2. **Spectral Calculation Loop**: Iterates over a range of periods, updating response values using the modified Newmark method.
3. **Conversion and Plotting**: Converts arrays to lists and uses Matplotlib to plot the seismic record and acceleration response spectra. Includes interactive features for better visualization.

#### Visualization:
- **Figure 1 - Seismic Record**: Plots the seismic record over time with highlights on the peak ground acceleration (PGA).
- **Figure 2 - Acceleration Response Spectra**: Displays the acceleration response spectra over a range of periods with interactive draggable line and marker.

#### Usage:
This function is useful for engineers, researchers, and students involved in the study of seismic effects on structures. It's particularly beneficial for spectral analysis and understanding the dynamic response over a range of structural periods. Recommended parameters for a typical use case might include:
- `To` = Initial period, e.g., 0.1.
- `Tf` = Final period, e.g., 3.0.
- `dT` = Period step size, e.g., 0.05.
- `zi` = Damping ratio, e.g., 0.05 for 5% damping.
- `xo` = Initial displacement, typically 0.
- `xvo` = Initial velocity, typically 0.
- `TG` = Time vector from seismic record.
- `SG` = Acceleration data from seismic record.
- `record` = Identifier for the seismic record, e.g., "ChiChi_Long Earthquake".

**Note**: The function includes interactive features for enhanced visualization. Users can explore the response spectra by moving the cursor along the curve. The seismic record and spectral plots provide valuable insights into the structural response under seismic loading.


