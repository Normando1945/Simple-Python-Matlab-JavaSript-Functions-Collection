import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Load and display the image
image_path = 'https://raw.githubusercontent.com/Normando1945/Simple-Python-Matlab-JavaSript-Functions-Collection/main/fun_SPEC_NEC/logo_TorreFuerte.png'
st.image(image_path, use_column_width=True)

# Título de la aplicación
st.markdown("<h4 style='text-align: center;'>Simple App: Seismic Response Spectrum [Normative Ecuadorian Spectrum]</h4>", unsafe_allow_html=True)

st.markdown("**Hola Xavier**")

st.markdown(
    """
    * Author: [Msc. Ing. Carlos Andrés Celi Sánchez](https://fragrant-knight-4af.notion.site/Main-Page-5c5f007b3f3f4c76a604960d9dbffca7?pvs=4)
    * Course: Structural Dynamics
    """
)


st.markdown('You can find me on : [![Web Page](https://img.shields.io/badge/Web%20Page-caceli.net-blue)](https://fragrant-knight-4af.notion.site/Main-Page-5c5f007b3f3f4c76a604960d9dbffca7?pvs=4)[![GitHub Carlos Celi](https://img.shields.io/github/followers/Normando1945?label=follow&style=social)](https://github.com/Normando1945)[![ResearchGate](https://img.shields.io/badge/-ResearchGate-00CCBB?style=social&logo=researchgate)](https://www.researchgate.net/profile/Carlos-Celi)[![Google Scholar](https://img.shields.io/badge/-Google%20Scholar-4285F4?style=social&logo=google)](https://scholar.google.com.ec/citations?hl=es&user=yR4Gz7kAAAAJ)')

st.markdown(
    '''
    ##### :open_book: Description
    
    This simple app performs spectral calculations using the NEC-SE-DS-2015 Ecuadorian Code. It computes the Elastic and Inelastic Acceleration Response Spectra for a range of structural periods and visualizes the results.
    
    '''
    )

st.markdown('##### :ledger: **More Information**')
with st.expander("**Click to read more**"):
    j1, j2 = st.columns([1, 2])
    with j1:
        image_path = 'https://raw.githubusercontent.com/Normando1945/Simple-Python-Matlab-JavaSript-Functions-Collection/main/fun_SPEC_NEC/Chapter1_portada.gif'
        st.image(image_path, use_column_width=True)
        
        st.markdown(
            """
            <div style="text-align: center;">
            <a href="https://cceli.neocities.org"> Online Book, Chapter 1</b></a>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
    with j2:
        st.markdown(
            '''
             **General Overview**
             
             Welcome to this presentation of the draft for the opening chapter of my upcoming book, titled **"Structural Engineering: Dynamics, Seismic Solution, and AI Integration."** This chapter delves into the intricate realm of undergraduate structural dynamics. This endeavor is not meant to mirror the exhaustive details laid out in some of the field's seminal literature. If you're familiar with works from esteemed authors such as **Chopra**, **Mario Paz**, **Cloth & Penzien**, among others, you'll be aware of the profound depth and rigor they bring to the underlying concepts and mathematical foundations of structural dynamics. Rather than merely echoing their profound insights, this book and the initial chapter provided here chart a distinctive course.

             The chief aim is to distill intricate theoretical mathematics into more accessible discrete mathematical frameworks, offering clear outlines of pivotal concepts in dynamic structures. This proves indispensable for students traversing the expansive realm of structural dynamics. By intertwining essential theories with illustrative **Python code samples**, readers will unlock understanding of the fundamental mechanics underpinning both single-degree-of-freedom **SDOF** and multi-degree-of-freedom **MDOF** dynamic systems. The focus remains unwaveringly on applications within structural engineering, positioning this as a prized asset for those immersing themselves in the field. It's vital to understand that this draft of the initial chapter isn't designed to serve as an isolated guide. Instead, it acts in tandem with conventional educational tools, reinforcing the bedrock knowledge students garner in academic settings. For a nuanced and comprehensive grasp of the domain, turning to the venerable tomes of dedicated structural dynamics literature is imperative. When combined with in-depth classroom learning, the revelations from such extensive studies will unquestionably refine a scholar's proficiency. I invite you to join me on this illuminating expedition, and I hope it lays the foundation for your scholastic and professional achievements in structural dynamics.
           
            ''', unsafe_allow_html=True
        )

st.markdown('##### :scroll: **Parameters**')
st.markdown('You can read the documentation at [**Function: fun_Nec(n, z, I, fads, r, R, fip, fie, TR)**](https://github.com/Normando1945/Simple-Python-Matlab-JavaSript-Functions-Collection/tree/main/fun_SPEC_NEC)')


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
    R = st.number_input('**R**: Seismic response reduction factor:', value=6.0, step=0.5)

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


st.markdown('##### 📊 **Response Spectra [Elastic and Inelastic]**')

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
        margin-right: 5px;
    }
    .footer .separator {
        border-left: 2px solid #eaeaea;
        height: 50px;
        margin-right: 5px;
    }
    </style>
    <div class="footer">
        <img class="logo" src="https://raw.githubusercontent.com/Normando1945/Simple-Python-Matlab-JavaSript-Functions-Collection/main/fun_SPEC_NEC/logo_TorreFuerte.png" alt="TorreFuerte Logo">
        <div class="separator"></div>
        <div>
            <p>Developed by Carlos Celi | <a href="https://www.http://torrefuerte.ec" target="_blank">TORREFUERTE</a> | <a href="https://www.caceli.net" target="_blank">Carlos Celi</a> | <a href="https://github.com/Normando1945" target="_blank">GitHub</a></p>
            <p>© Version 1.0.1 - July, 2024</p>
        </div>
    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)

display_footer()
