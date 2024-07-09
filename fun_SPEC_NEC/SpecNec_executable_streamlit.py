import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# # Load and display the image
# image_path = 'logo_TorreFuerte.png'
# st.image(image_path, use_column_width=True)



# Título de la aplicación
st.markdown("<h4 style='text-align: center;'>Simple App: Seismic Response Spectrum [Normative Ecuadorian Spectrum]</h4>", unsafe_allow_html=True)


st.markdown(
    """
    * Author:                 [Msc. Ing. Carlos Andrés Celi Sánchez](https://fragrant-knight-4af.notion.site/Main-Page-5c5f007b3f3f4c76a604960d9dbffca7?pvs=4)
    * Course:                 Structural Dynamics
    """
)

st.markdown('* You can find me on : [![Web Page](https://img.shields.io/badge/Web%20Page-caceli.net-blue)](https://fragrant-knight-4af.notion.site/Main-Page-5c5f007b3f3f4c76a604960d9dbffca7?pvs=4)[![GitHub Carlos Celi](https://img.shields.io/github/followers/Normando1945?label=follow&style=social)](https://github.com/Normando1945)[![ResearchGate](https://img.shields.io/badge/-ResearchGate-00CCBB?style=social&logo=researchgate)](https://www.researchgate.net/profile/Carlos-Celi)[![Google Scholar](https://img.shields.io/badge/-Google%20Scholar-4285F4?style=social&logo=google)](https://scholar.google.com.ec/citations?hl=es&user=yR4Gz7kAAAAJ)')

st.markdown('This simple app performs spectral calculations using the NEC-SE-DS-2015 Ecuadorian Code. It computes the Elastic and Inelastic Acceleration Response Spectra for a range of structural periods and visualizes the results.')

st.markdown("#### **Parameters**")


n = st.number_input('**n**: Ratio between spectral ordinates **Sa(T = 0.1 s)** and **PGA**:', value=2.48, step=0.1)
z = st.number_input('**z**: Maximum expected acceleration (fraction of gravitational acceleration):', value=0.4, step=0.1)

# Create a grid layout with a maximum of 5 columns
col1, col2, col3, col4 = st.columns(4)

# User input for parameters with descriptions
with col1:
    fa = st.number_input('**fa**: Short period amplification factor:', value=1.2, step=0.1)
    fip = st.number_input('**Φp**: Penalty coefficient for plan irregularity:', value=1.0, step=0.1)
    
with col2:
    fd = st.number_input('**fd**: Velocity amplification factor:', value=1.11, step=0.1)
    fie = st.number_input('**Φe**: Penalty coefficient for elevation irregularity:', value=1.0, step=0.1)
        
with col3:
    fs = st.number_input('**fs**: Soil non-linearity amplification factor:', value=1.11, step=0.1)
    R = st.number_input('**R**: Seismic response reduction factor:', value=6.0, step=0.1)

with col4:
    I = st.number_input('**I**: Importance coefficient [for different structures]:', value=1.0, step=0.1)
    r = st.number_input('**r**: Geographic zone factor [for Ecuador]:', value=1.0, step=0.1)


fads = [fa, fd, fs]
To = 0.10 * fads[2] * fads[1] / fads[0]
Tc = 0.55 * fads[2] * fads[1] / fads[0]

Sae = []
Sai = []
Tie = []

for T in np.arange(0, 4, 0.005):
    if T <= To:
        Sae.append([z * fads[0] * (1 + (n - 1) * T / To) * I])
        Sai.append([n * z * fads[0] / (R * fip * fie) * I])
        Tie.append([T])
    else:
        if T <= Tc:
            Sae.append([n * z * fads[0] * I])
            Sai.append([n * z * fads[0] / (R * fip * fie) * I])
            Tie.append([T])
        else:
            Sae.append([I * n * z * fads[0] * (Tc / T) ** r])
            Sai.append([I * n * z * fads[0] * (Tc / T) ** r / (R * fip * fie)])
            Tie.append([T])

Resul = pd.DataFrame({ 'Period [s]': Tie,'Sae [g]': Sae,'Sai [g]': Sai})
    
Tie = np.array(Tie)
Sae = np.array(Sae)
Sai = np.array(Sai)
Tie = Tie[:, 0]
Sae = Sae[:, 0]
Sai = Sai[:, 0]
    
    
fig1, ax1 = plt.subplots(figsize=(16/1.5, 9/1.5))                                                                

ax1.plot(Tie, Sae, color=(0, 0, 1), marker='+', markersize=0, markerfacecolor='w',                             
markeredgewidth=0, linewidth=1.0, alpha=0.5,linestyle = '-',label= f'Sa_elastic')
ax1.plot(Tie, Sai, color=(0, 0, 0), marker='+', markersize=0, markerfacecolor='w',                              
markeredgewidth=0, linewidth=1.5, alpha=0.7,linestyle = '--',label= f'Sa_inelastic')
ax1.set_xlim([Tie[0], (max(Tie))])                                                                               
ax1.set_ylim([0, (max(Sae)*1.05)])                                                                              
plt.title('UHS [NEC-SE-DS-2015]', fontsize=10, color=(0, 0, 1))                                                      
plt.xlabel('Period (T) [s]', rotation=0, fontsize=10, color=(0, 0, 0))                                          
plt.ylabel('Max Response Acceleration (Sa) [g]', rotation=90, fontsize=10, color=(0, 0, 0))                     
legend = plt.legend(fontsize=10)                                                                               
legend.get_frame().set_edgecolor('none')                                                                       
ax1.grid(which='both', axis='x', alpha=0.5)                                                                      

st.pyplot(fig1)


st.markdown("##### **Response Spectra [Elastic and Inelastic]**")
st.write(Resul)

def display_footer():
    footer = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: white;
        color: black;
        text-align: center;
        padding: 10px;
        border-top: 1px solid #eaeaea;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .footer .logo {
        height: 60px; /* Increased size */
        margin-right: 20px;
    }
    .footer .separator {
        border-left: 2px solid #eaeaea;
        height: 120px;
        margin-right: 20px;
    }
    </style>
    <div class="footer">
        <img class="logo" src="https://raw.githubusercontent.com/nmorabowen/constitutiveRelationshipsApp/main/APE_LOGO.png" alt="APE Logo">
        <div class="separator"></div>
        <div>
            <p>Developed by Nicolás Mora Bowen | <a href="https://www.ape-ec.com" target="_blank">APE</a> | <a href="https://www.nmorabowen.com" target="_blank">Nicolás Mora Bowen</a> | <a href="https://github.com/nmorabowen" target="_blank">GitHub</a></p>
            <p>© Version 1.0.1  - July, 2024</p>
        </div>
    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)
  
