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

### Function: SHM_animation(R, phi, w, T)

This Python function generates an animated visualization of a Simple Harmonic Motion (SHM) system using Matplotlib. It's designed to represent the motion of a particle or object in SHM, typically found in physics.


![SHM_animation](https://github.com/Normando1945/Simple-Python-Functions-Collection/assets/62081230/68e71aca-3849-4e5f-a76e-28bd85f75189)


#### Parameters:
- `R` (float): The amplitude of the motion, indicating the maximum distance from the equilibrium position.
- `phi` (float): The phase of the motion, determining where in its cycle the oscillation begins.
- `w` (float): The angular frequency of the motion, defining how many oscillations occur per unit of time.
- `T` (float): The time period over which the animation is displayed, indicating how long one complete cycle of the motion lasts.

#### Functionality:
1. **Initialization**: Sets up the Matplotlib figure and axes, preparing three subplots. The first two are for visualizing the circular motion in SHM, and the third is for plotting the displacement over time.

2. **Animation Preparation**: Configures various elements of the animation, including the circle representing the path of the SHM, the line showing the current position, and the dot indicating the particle or object in motion.

3. **Updating Function**: Updates the position of the particle or object for each frame of the animation, recalculating its position based on the SHM equations and redrawing the relevant elements of the plot.

4. **Execution**: Uses `FuncAnimation` from Matplotlib to create the animation by repeatedly calling the updating function for each time step.

#### Visualization:
- **Subplot 1 & 2**: Show the particle's motion along a circular path, emphasizing the SHM's characteristics. The parameters `w` and `T` are doubled in the second subplot, demonstrating the effect of changing these values.
- **Subplot 3**: Plots the displacement of the particle over time, providing a direct view of how the SHM progresses over the period `T`.

#### Usage:
This function is ideal for educational purposes, especially for providing students with a visual understanding of SHM concepts in physics. Below is an example of recommended parameters for a typical use case:

- `R` =         0.5 or 1.0: Depending on the desired amplitude, you may choose a value of 0.5 for a standard representation or any value for a motion with a higher amplitude.
- `phi` =       0: This starts the motion at the equilibrium position, which is common for basic demonstrations of **SHM**.
- `w` =         1.0 * np.pi: This value sets a standard angular frequency, corresponding to one complete oscillation every **2π** units of time.
- `T` =         (2 * np.pi) / w: By setting the time period like this, the animation will display exactly one complete cycle, given the angular frequency **w**.

**Note**: The animation's default configuration aims for optimal visibility and comprehension, but users can adjust parameters and settings to suit specific requirements or scenarios. For instance, altering the value of `R` can show students how changes in amplitude affect the motion, while different values of `phi` can demonstrate the effects of phase shifts.

