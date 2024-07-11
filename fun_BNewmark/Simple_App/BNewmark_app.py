import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob

######################################################## header ########################################################
image_path = 'https://raw.githubusercontent.com/Normando1945/Simple-Python-Matlab-JavaSript-Functions-Collection/main/fun_SPEC_NEC/logo_TorreFuerte.png'
st.image(image_path, use_column_width=True)

# Título de la aplicación
st.markdown("<h4 style='text-align: center;'>Simple App: Time History Response, SDOF (B_Newmark)</h4>", unsafe_allow_html=True)


st.markdown(
    """
    * Author: [Msc. Ing. Carlos Andrés Celi Sánchez](https://fragrant-knight-4af.notion.site/Main-Page-5c5f007b3f3f4c76a604960d9dbffca7?pvs=4)
    * University: [PUCE](https://www.puce.edu.ec/)
    * Course: Structural Dynamics
    """
)


st.markdown('You can find me on : [![Web Page](https://img.shields.io/badge/Web%20Page-caceli.net-blue)](https://fragrant-knight-4af.notion.site/Main-Page-5c5f007b3f3f4c76a604960d9dbffca7?pvs=4)[![GitHub Carlos Celi](https://img.shields.io/github/followers/Normando1945?label=follow&style=social)](https://github.com/Normando1945)[![ResearchGate](https://img.shields.io/badge/-ResearchGate-00CCBB?style=social&logo=researchgate)](https://www.researchgate.net/profile/Carlos-Celi)[![Google Scholar](https://img.shields.io/badge/-Google%20Scholar-4285F4?style=social&logo=google)](https://scholar.google.com.ec/citations?hl=es&user=yR4Gz7kAAAAJ)')

######################################################## Author ########################################################
st.markdown('##### 😎 **About the Author**')
with st.expander("**Click to read more**"):
    coll1, coll2 = st.columns([1,1])
    with coll1:
        st.image("https://raw.githubusercontent.com/Normando1945/Simple-Python-Matlab-JavaSript-Functions-Collection/main/fun_SPEC_NEC/assets/foto.jpg", width= 325)
    with coll2:
        st.markdown(
            """
            **Short Curriculum Vitae Overview**.

            I am Ecuadorian, I have a Master's degree in Structural Engineering with a **SUMMA CUM LAUDE** distinction from the National Polytechnic School. With over 15 years of experience, I have notably provided structural consultancy for buildings surpassing 140 meters in height. I am currently affiliated with the Department of Civil Engineering at the [**Pontifical Catholic University of Ecuador**](https://www.puce.edu.ec/). My primary research domain is nonlinear mathematical modeling, leading to several 
            international scientific publications. My ongoing projects include:
            
            * The Application of Artificial Neural Networks (ANN) in Estimating Local Fragility in Zero-Length Elements.
            * Generating Synthetic Accelerograms based on Chaos Theory and Wavelets.
            * Participation in the 'Training And Communication for Earthquake Risk Assessment - GEM' project.
            
            """
        )

    st.markdown(':ledger: **More Information about my New Book**')
    jj1, jj2 = st.columns([1, 1])
    with jj1:
        st.image("https://raw.githubusercontent.com/Normando1945/Simple-Python-Matlab-JavaSript-Functions-Collection/main/fun_SPEC_NEC/assets/Structural Engineering2.png", width= 300)
        st.markdown(
            """
            <div style="text-align: center;">
            <a href="https://fragrant-knight-4af.notion.site/My-Personal-Page-for-Academic-Use-5c5f007b3f3f4c76a604960d9dbffca7"> Online Book </b></a>
            </div>
            """, 
            unsafe_allow_html=True
        )
    with jj2:
        st.markdown(
        """
        **Structural Engineering: Dynamics, Seismic Solution, and AI Integration**
    
        In an era where structural engineering faces multifaceted challenges, this book offers an integrated approach that melds core dynamics, seismic-resistant design techniques, and the transformative potential of AI in modern structural solutions. Beginning with foundational principles, readers are ushered into the intricate world of structural dynamics, with a spotlight on the importance of understanding multi-degree of freedom systems. As societies grapple with the increasing prominence of seismic threats, the imperative for resilient construction methods is laid bare.
    
        However, it's paramount to note that this work doesn't aspire to replace or overshadow the comprehensive mathematical insights found in the seminal works of the discipline or the invaluable depth of formal university education. Rather, this book positions itself as a supplementary resource, designed to complement these foundational sources of knowledge. By bridging the gap between time-honored techniques and contemporary technological advancements, it underscores the evolving synergy between traditional engineering practices and modern AI-driven tools.
    
        Harnessing the power of discrete mathematics, the book reveals how automation is revolutionizing the field, not just simplifying but also optimizing the design process. In ensuring structural safety and cost-effectiveness, it aims to pave a path toward a future where structures are not only robust against threats but are also emblematic of efficiency and innovation. Dive in to discover a confluence of tradition and technology, all designed to enhance and enrich the existing knowledge landscape of structural engineering.
        """
        )

######################################################## Description ########################################################
st.markdown(
    '''
    ##### 📖 **Description of this Simple App**
    This simple application performs step-by-step calculations of the displacement, velocity, and acceleration response of a single-degree-of-freedom (SDOF) structure, whether conservative or non-conservative, subjected to ground motion using the Newmark method.
    '''
)

######################################################## More Information ########################################################
st.markdown('##### :ledger: **More Information about this Simple App**')
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
st.markdown('You can read the documentation at [**Function: fun_B_Newmark_2023(TG, SG, M, T, xo, xvo, zi, record)**](https://github.com/Normando1945/Simple-Python-Matlab-JavaSript-Functions-Collection/tree/main/fun_BNewmark)')




################################################ Selection of Record #################################################
# Selection of Record
at2_files = glob.glob('*.AT2')

if len(at2_files) > 0:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown('**Seismic Records in the Directory**')
        srd = pd.DataFrame(at2_files, columns=["Record Files"])
        st.write(srd)
    
    with col2:
        st.markdown('**Select a Record form the list**')
        row_numbers = list(range(len(srd)))
        aux = st.selectbox('**Record #**:', row_numbers)
        
        if aux is not None:
            st.metric(label='Record Selected', value=at2_files[aux])
            with open(at2_files[aux], 'r') as f:
                contents = f.read()
            lines = contents.splitlines()
            data = []
            for line in lines:
                time, accel = line.split()
                data.append((float(time), float(accel)))
            Seismic = pd.DataFrame(data, columns=["Time [s]", "Acceleration [g]"])
            
            # Further processing of the selected record
            TG = np.vstack([item[0] for item in data])  # Extracting the first column of data (time) as a NumPy array
            SG = np.vstack([item[1] for item in data])  # Extracting the second column of data (Acceleration) as a NumPy array

            # Other parts of your code for plotting and displaying results remain the same
else:
    st.warning("No seismic records found in the directory.")


    ################################################ Convertion of Selected Record #################################################
    TG = np.vstack([item[0] for item in data])                                  # Extracting the first column of data (time) as a NumPy array
    SG = np.vstack([item[1] for item in data])                                  # Extracting the second column of data (Acceleration) as a NumPy array
    
    tii =  list(TG)
    Sggg = list(SG)
    fs  = 1.5
    scale_line = 0.3 
    fig1, (ax1) = plt.subplots(nrows=1, ncols=1, figsize=((16/fs)/1.5, (16/fs)/3.5))
    ax1.plot(tii, Sggg, color=(0, 0, 0), marker='+', markersize=0, markerfacecolor='w',
            markeredgewidth=0, linewidth=scale_line, alpha=1.0, label='Seismic Record')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    ax1.spines['left'].set_visible(False)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.text(0.01, 0.99, '© by Carlos Celi', transform=ax1.transAxes, color=(0, 0, 1), alpha=0.5,
         fontsize=10, verticalalignment='top', horizontalalignment='left')
    plt.tight_layout()
    # plt.show()
    st.pyplot(fig1) 

######################################################## user parameters ########################################################
col1, col2 = st.columns([1,1])

# User input for parameters with descriptions
with col1:
    T = st.number_input('**T**: Structural Period [s]:', value=0.15, step=0.05)
with col2:
    zi = st.number_input('**ξ**: Damping Factor:', value=0.05, step=0.01)
       
    
    


################################################ Parameters #################################################
xo = 0                                                                      # Initial condition for displacement
xvo = 0                                                                     # Initial condition for velocity
# T = 0.1775                                                                  # Period of motion
w = (2*np.pi)/T                                                             # Angular frequency
# zi = 0.05                                                                   # Damping ratio
wz = w*np.sqrt(1-zi**2)                                                     # Natural frequency
M = 1                                                                       # Mass
record = at2_files[aux]                                                       # Seismic Record name


################################################ Code #################################################
ti  = TG        
dt = ti[1] - ti[0]
K = (2 * np.pi / T) ** 2 * M

xn1 = np.zeros((len(SG), 1))
xvn1 = np.zeros((len(SG), 1))
xan1 = np.zeros((len(SG), 1))
at = np.zeros((len(SG), 1))

xn1[0, 0] = xo
xvn1[0, 0] = xvo
xan1[0, 0] = ((-SG[0] * M) - 2 * zi * (2*np.pi / T) * M * xvo - (np.pi / T) ** 2 * xo) * 1 / M

for i in range(1, len(SG)):
    xn1[i, 0] = xn1[i - 1, 0] + (dt * xvn1[i - 1, 0]) + (dt ** 2 / 2 * xan1[i - 1, 0])
    xan1[i, 0] = 1 / (M + (1 / 2) * (2 * zi * (2*np.pi / T) * M * dt)) * ((-SG[i] * M) - K * xn1[i] - 2 * zi * (2*np.pi / T) * M * (xvn1[i - 1] + dt * (1 - (1 / 2)) * xan1[i - 1]))
    xvn1[i, 0] = xvn1[i - 1, 0] + dt * ((1 - (1 / 2)) * xan1[i - 1, 0] + (1 / 2) * xan1[i, 0])
    at[i, 0] = xan1[i, 0] + SG[i][0]

Xn1 = list(xn1)
Xvn1 = list(xvn1)
Xan1 = list(xan1)
At =  list(at)
ti =  list(TG)
Sgg = list(SG)


################################################ Results #################################################

# Lista de mensajes graciosos
messages = [
    "Well, well, well... look who needed some results.",
    "Behold! The miraculous results you've been waiting for!",
    "Surprise! Here are your results. Try not to faint.",
    "Results are in. Try to act surprised.",
    "Ta-da! Your results, served with a side of irony.",
    "Eureka! Your results are here. Don't spend them all in one place.",
    "Drum roll, please... Your results have arrived.",
    "Breaking news! Your results are hot off the press.",
    "Hold onto your hat! Here are your sparkling new results.",
    "Voilà! Your results have magically appeared.",
    "No, I am not ChatGPT, don't insist. Wink wink."
]
# Lista de gif's
gifs = [
    "https://media4.giphy.com/media/EbeeDkvlC3fFRGJ6Om/200.webp?cid=ecf05e47pr1lqu1ercua819ufpxbbjc92z3b6eerc825ilv1&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media2.giphy.com/media/dXpAxrUk0Ya9TXBJH9/200.webp?cid=ecf05e47pr1lqu1ercua819ufpxbbjc92z3b6eerc825ilv1&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media0.giphy.com/media/wzu3RR6iZGD7ryCFdm/200.webp?cid=ecf05e472d4zjoh9xvy2h63ugepvflgkoseft7fe2rjdcs7a&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media1.giphy.com/media/XreQmk7ETCak0/200.webp?cid=ecf05e478au4hlrh86lo1v25qxz7hrz7qkubs967m720usle&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media1.giphy.com/media/xUPGcmvgjMIEhy6jZu/200.webp?cid=ecf05e474k63y0j7jtbydaaikmvhrfsz8bcdlzji0u0jr385&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media4.giphy.com/media/JliGmPEIgzGLe/200.webp?cid=ecf05e474k63y0j7jtbydaaikmvhrfsz8bcdlzji0u0jr385&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media3.giphy.com/media/l3fZXTZdS6Ofi7U6A/100.webp?cid=ecf05e47rwnp5i6yc3odmtob7g480qqlo56d0pugbbtroo7q&ep=v1_gifs_search&rid=100.webp&ct=g",
    "https://media1.giphy.com/media/3oswhordgO0ZbDkTio/200.webp?cid=ecf05e472vc7m7m1ngpi9rkt38gk6200t3c5ov68mq6nauuh&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media0.giphy.com/media/xTdy8lYBh2XGvzz5UA/200.webp?cid=ecf05e472vc7m7m1ngpi9rkt38gk6200t3c5ov68mq6nauuh&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media2.giphy.com/media/l0MYuPnFNsKteNw1a/200.webp?cid=ecf05e471izn0s02usul3fv0scf9mtjmghbsryi3rsbufpcd&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media0.giphy.com/media/Dh5q0sShxgp13DwrvG/200.webp?cid=790b7611oiq55hr7mtdyx682bu69e8tfe4597zdp56l1ezeu&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media2.giphy.com/media/EHxx63vDG0jQ8bKIkP/200.webp?cid=ecf05e470cgg4omlys19jn9w0dv38kqrz7wlbjpyg8f83kn7&ep=v1_gifs_search&rid=200.webp&ct=g",
    "https://media0.giphy.com/media/26gJAkoJKPKoFH7DW/200.webp?cid=ecf05e4712aizlynkwpnfsfwaf5aboy7qf6aacbaodjfso58&ep=v1_gifs_search&rid=200.webp&ct=g"
]

# Seleccionar un mensaje al azar
random_message = np.random.choice(messages)
random_gif = np.random.choice(gifs)

st.markdown('##### 📊 **Results**')
col1, col2 = st.columns([1, 3])
with col1:
    st.image(random_gif, use_column_width=True)
with col2:
    with st.chat_message("assistant"):
        st.write(random_message)


################################################ Plotting #################################################    

fs  = 1.15
scale_line = 0.3 
fig2, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1, figsize=((16/fs)/1.5, (16/fs)/1.5))

ax1.plot(ti, Sgg, color=(0, 0, 0), marker='+', markersize=0, markerfacecolor='w',
        markeredgewidth=0, linewidth=scale_line, alpha=1.0, label='Seismic Record')
ax1.set_xlim([0, (max(ti))])
ax1.set_title(f'Seismic Record ({record})', fontsize=7, color=(0, 0, 1))
ax1.set_xlabel('Time [s]', rotation=0, fontsize=7, color=(0, 0, 0))
ax1.set_ylabel('Amplitude [g]', rotation=90, fontsize=7, color=(0, 0, 0))
legend = ax1.legend(fontsize=7)
legend.get_frame().set_edgecolor('none')
ax1.grid(which='both', axis='x', alpha=0.5)
ax1.text(0.01, 0.99, '© by Carlos Celi', transform=ax1.transAxes, color=(0, 0, 1), alpha=0.5,
         fontsize=7, verticalalignment='top', horizontalalignment='left')

ax2.plot(ti, xn1, color=(0, 0, 1), marker='+', markersize=0, markerfacecolor='w',
        markeredgewidth=0, linewidth=scale_line, alpha=0.5, label='Displacement')
ax2.set_xlim([0, (max(ti))])
ax2.set_title(f'Displacement ({record})', fontsize=7, color=(0, 0, 1))
ax2.set_xlabel('Time [s]', rotation=0, fontsize=7, color=(0, 0, 0))
ax2.set_ylabel('Amplitude [X]', rotation=90, fontsize=7, color=(0, 0, 0))
legend = ax2.legend(fontsize=7)
legend.get_frame().set_edgecolor('none')
ax2.grid(which='both', axis='x', alpha=0.5)
ax2.text(0.01, 0.99, '© by Carlos Celi', transform=ax2.transAxes, color=(0, 0, 1), alpha=0.5,
         fontsize=7, verticalalignment='top', horizontalalignment='left')

ax3.plot(ti, xvn1, color=(1, 0, 0), marker='+', markersize=0, markerfacecolor='w',
        markeredgewidth=0, linewidth=scale_line, alpha=0.5, label='Velocity')
ax3.set_xlim([0, (max(ti))])
ax3.set_title(f'Velocity ({record})', fontsize=7, color=(0, 0, 1))
ax3.set_xlabel('Time [s]', rotation=0, fontsize=7, color=(0, 0, 0))
ax3.set_ylabel('Amplitude [V]', rotation=90, fontsize=7, color=(0, 0, 0))
legend = ax3.legend(fontsize=7)
legend.get_frame().set_edgecolor('none')
ax3.grid(which='both', axis='x', alpha=0.5)
ax3.text(0.01, 0.99, '© by Carlos Celi', transform=ax3.transAxes, color=(0, 0, 1), alpha=0.5,
         fontsize=7, verticalalignment='top', horizontalalignment='left')

ax4.plot(ti, Sgg, color=(0, 0, 0), marker='+', markersize=0, markerfacecolor='w',                                
        markeredgewidth=0, linewidth=scale_line, alpha=1.0,label= f'Seismic Record')
ax4.plot(ti, Xan1, color=(0, 0, 1), marker='+', markersize=0, markerfacecolor='w',                               
        markeredgewidth=0, linewidth=scale_line, alpha=0.5,label= f'Acceleration Response [B-Newmark]')
ax4.plot(ti, At, color=(1, 0, 0), marker='+', linestyle = '--', markersize=0, markerfacecolor='w',               
        markeredgewidth=0, linewidth=scale_line, alpha=0.5,label= f'Total Acceleration Response [B-Newmark]')
ax4.set_xlim([0, (max(ti))])                                                                                     
ax4.set_title(f'Acceleration ({record})', fontsize=7, color=(0, 0, 1))                                                         
ax4.set_xlabel('Time [s]', rotation=0, fontsize=7, color=(0, 0, 0))                                                
ax4.set_ylabel('Acceleration [g]', rotation=90, fontsize=7, color=(0, 0, 0))                                          
ax4.grid(which='both', axis='x', alpha=0.5)
ax4.text(0.01, 0.99, '© by Carlos Celi', transform=ax4.transAxes, color=(0, 0, 1), alpha=0.5,
         fontsize=7, verticalalignment='top', horizontalalignment='left')   

legend1 = ax4.legend(fontsize=7, loc='lower center', ncol=3)
legend1.get_frame().set_edgecolor('none')                                                                      

plt.tight_layout()
plt.show() 
st.pyplot(fig2) 

TG = np.array([item[0] for item in data]).flatten()  
SG = np.array([item[1] for item in data]).flatten()
X = xn1.flatten() 
V = xvn1.flatten()
A = xan1.flatten()  
At = at.flatten() 
Resul = pd.DataFrame({'time [s]': TG,'Sg [g]': SG,'X': X,'V': V,'A [g]': A,'AT [g]': At})
max_abs_SG = np.max(np.abs(SG))
time_max_abs_SG = TG[np.argmax(np.abs(SG))]
max_abs_AT = np.max(np.abs(At))
time_max_abs_AT = TG[np.argmax(np.abs(At))]


col1, col2, col3 = st.columns([0.7,0.7,2])
with col1:
    st.metric(label='**T**: Structural Period [s]:', value=f"{T:.3f}", delta='s')
    st.metric(label='**ξ**: Damping Factor', value=f"{zi:.3f}")
with col2:
    st.metric(label='Time, Max Sg', value=f"{time_max_abs_SG:.4f}", delta='s')
    st.metric(label='Max Sg', value=f"{max_abs_SG:.4f}", delta='g')
    st.metric(label='Time, Max AT', value=f"{time_max_abs_AT:.4f}", delta='s')
    st.metric(label='Max AT', value=f"{max_abs_AT:.4f}", delta='g')
with col3:
    st.write(Resul)




st.markdown('##### ⚠️ **Disclaimer**')
st.markdown(
    '''
    It is important for users to understand that this application is provided for academic purposes only. The scope and use of this tool are entirely the responsibility of the user. The developers assume no liability for any misuse or unintended use of this application.
    '''
)



######################################################## Footer ########################################################

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

