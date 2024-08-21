<div align="center">
    <img src="https://github.com/Normando1945/Normando1945.github.io/assets/62081230/1ac0bf1d-67cd-43f6-87b0-141417a606db">
</div>

>##### Author:                 [Msc. Ing. Carlos Andrés Celi Sánchez](https://www.researchgate.net/profile/Carlos-Celi). & [Phd(c). MSc. Ing. José Poveda](https://www.torrefuerte.com)

>##### Course:                 Structural Dynamics


### :earth_americas: **You can find me on**

[![Web Page](https://img.shields.io/badge/Web%20Page-caceli.net-blue)](http:caceli.net)
[![GitHub Carlos Celi](https://img.shields.io/github/followers/Normando1945?label=follow&style=social)](https://github.com/Normando1945)
[![ResearchGate](https://img.shields.io/badge/-ResearchGate-00CCBB?style=social&logo=researchgate)](https://www.researchgate.net/profile/Carlos-Celi)
[![Google Scholar](https://img.shields.io/badge/-Google%20Scholar-4285F4?style=social&logo=google)](https://scholar.google.com.ec/citations?hl=es&user=yR4Gz7kAAAAJ)
[![YouTube](https://img.shields.io/badge/-YouTube-FF0000?style=social&logo=youtube)](https://www.youtube.com/@CCeli1945)
<a href="Carlos Celi:normando1945@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-normando1945@gmail.com-blue?style=flat&logo=gmail"></a>


* If you found this free repository useful and enjoyable, please consider supporting us with a donation. Your contribution helps us continue developing and maintaining free software.

<a href='https://ko-fi.com/H2H111V2R3' target='_blank'>
    <img src='https://storage.ko-fi.com/cdn/kofi5.png?v=3' alt='Support Me on Ko-fi' style='width: 15%; height: auto; border:0;'>
</a>

### Function: fun_B_Newmark_2023(TG, SG, M, T, xo, xvo, zi, record)

This Python function calculates the displacement, velocity, and acceleration response of a structure subjected to ground motion using the Newmark method.

<p align="center">
    <img src="https://github.com/Normando1945/Simple-Python-Functions-Collection/assets/62081230/069ba2db-724a-453b-af7c-9e103dbb2743" alt="fun_BNewmark" width="50%">
</p>



#### Parameters:
- `TG` (list): Time vector of the motion history.
- `SG` (list of lists): Acceleration time history of the ground motion.
- `M` (float): Mass of the structure.
- `T` (float): Period of the structure.
- `xo` (float): Initial displacement response.
- `xvo` (float): Initial velocity response.
- `zi` (float): Damping ratio of the structure.
- `record` (string): Name or identifier for the seismic record.

#### Returns:
- `Xn1` (list): Displacement response.
- `Xvn1` (list): Velocity response.
- `Xan1` (list): Acceleration response.
- `At` (list): Total acceleration response.
- `ti` (list): Time vector.
- `Sgg` (list): Acceleration time history of the ground motion.
- `dt` (float): Time step size.
- `folder_path` (str): Path to the created results folder, named as `Results_XXXX` where `XXXX` is the record value.
- `file_path1` (str): Path to the saved `.AT2` file containing the seismic record data within the results folder.
- `file_path2` (str): Path to the saved `.AT2` file containing the total acceleration response within the results folder.
- `fig_path1` (fig): Path to the saved `.PNG` file containing the figure of the seismic record, displacement response, velocity response & acceleration response data within the results folder.

#### Functionality:
1. **Initialization**: Sets up the time vector, calculates stiffness, and initializes arrays for displacement, velocity, and acceleration. Initial conditions are set based on input parameters.
2. **Calculation Loop**: Iterates over each time step, updating the values of displacement, acceleration, and velocity using the Newmark method equations.
3. **Conversion and Plotting**: Converts arrays to lists and uses Matplotlib to plot the seismic record, displacement, velocity, and acceleration in separate subplots.

#### Visualization:
- **Sub Figure 1 - Seismic Record**: Plots the seismic record over time.
- **Sub Figure 2 - Displacement**: Shows the displacement response over time.
- **Sub Figure 3 - Velocity**: Illustrates the velocity response over time.
- **Sub Figure 4 - Acceleration**: Compares the seismic record, acceleration response, and total acceleration response over time.

#### Usage:
This function is ideal for engineers and researchers studying the effects of seismic activity on structures. It can be used for educational purposes or practical applications in structural engineering and seismology. Below is an example of recommended parameters for a typical use case:

- `TG` = List of time intervals.
- `SG` = Nested list containing acceleration data.
- `M` = Value representing the mass of the structure, e.g., 1000 (for a structure with a mass of 1000 kg).
- `T` = Value for the period of the structure, e.g., 0.5.
- `xo` = Initial displacement, typically 0 for structures at rest.
- `xvo` = Initial velocity, typically 0 for structures at rest.
- `zi` = Damping ratio, e.g., 0.05 for 5% damping.
- `record` = Identifier for the seismic record, e.g., "ChiChi_Long Earthquake".

**Note**: The visualization's default configuration is designed for optimal visibility and understanding, but users can adjust parameters and settings to suit specific requirements or scenarios.
Attached in this same repository is a file (.AT2) that contains a seismic record organized in 2 columns. The first column has the time of the record and the second column has the corresponding acceleration in a fraction of gravity.



