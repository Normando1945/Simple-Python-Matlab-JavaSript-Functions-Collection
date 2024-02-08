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

### Script: SHM_Response_Superposition_Animation

This JavaScript creates an animated visualization representing the superposition of multiple **SHM Response**, which can be used to illustrate concepts such as interference patterns or individual frecuencies of a seismic record.

![SHM_animation_p5js_2](https://github.com/Normando1945/Simple-Python-Matlab-JavaSript-Functions-Collection/assets/62081230/ce57cfe4-0fd7-4b4e-945c-c7dea3eeb838)


#### Parameters:
- `R` (number): The maximum amplitude of the sine waves.
- `T` (number): The maximum period of the sine waves.
- `phi` (number): The initial phase of the sine waves.
- `number_waves` (number): The starting number of sine waves to be superimposed.
- `max_number_waves` (number): The maximum number of sine waves that can be superimposed.
- `inv_frames` (number): The speed of the animation.
- `number_of_pi` (number): The multiplier for the initial phase to vary the phase of sine waves.
- `ranCB` (number), `ranCS` (number): The initial and final color ranges for the RGB color model.

#### Functionality:
1. **Initialization**: Sets up the p5.js canvas and initializes the slider control for selecting the number of waves.
2. **Wave Calculation**: A `Wave_Class` object calculates individual sine wave responses and updates their phase.
3. **Animation Loop**: In the `draw` function, the superposition of waves is calculated and visualized. The color and placement of each point are determined by the superposition result.

#### Visualization:
- The animation displays a series of points moving in a pattern that represents the superposition of different sine waves.
- A line represents the zero amplitude level for reference.
- Each wave's individual response is plotted, along with the cumulative response of all waves.

#### Usage:
This script can be useful for educational demonstrations in physics and engineering, particularly in areas that deal with Simple Harmonic Motion (SHM) and superposition.

**Note**: The parameters can be adjusted to visualize different numbers and configurations of **SHM Response**. The speed and complexity of the animation can be customized using the slider and the `inv_frames` parameter.


