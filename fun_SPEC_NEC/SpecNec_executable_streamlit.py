import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import pytz


#########
# line of run c:\users\normando\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\scripts\streamlit.exe run SpecNec_executable_streamlit.py
#########

######################################################## Side BAR ########################################################
st.markdown(
    """
    <style>
    /* Cambia el fondo del sidebar */
    [data-testid="stSidebar"] {
        background-color: #fdc30a;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <div style="text-align: center;">
        <img src="https://www.dropbox.com/scl/fi/3vpwdr61i4la2hhqq54lz/TorreFuerte_ico.png?rlkey=yd6ll1cojtfybjvo8jmtc6zj3&raw=1" alt="Torre Fuerte Icon" style="width: 35%;">
    </div>
    """, 
    unsafe_allow_html=True
)


st.sidebar.title("**Welcome to Simple App: Seismic Response Spectrum [Normative Ecuadorian Spectrum]**")

# Obtener la fecha y hora actual en Quito, Ecuador
ecuador_tz = pytz.timezone('America/Guayaquil')
current_time = datetime.now(ecuador_tz)
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# Mostrar la fecha y hora en el sidebar
st.sidebar.markdown(f"**Current Date and Time in Quito, Ecuador:**\n\n{formatted_time}")

## Author ##
st.sidebar.markdown('#### 😎 **About the Author**')
with st.sidebar.expander("**Click to read more**"):
    # st.image("https://www.dropbox.com/scl/fi/24umxisfp4tedeqzndj3n/foto.jpg?rlkey=4yrliifi3xjuhbmjbhh1zrjv8&st=widakesu&raw=1",  use_column_width=True)
    st.image("https://www.dropbox.com/scl/fi/24umxisfp4tedeqzndj3n/foto.jpg?rlkey=4yrliifi3xjuhbmjbhh1zrjv8&st=widakesu&raw=1",  use_container_width=True)
       
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

    st.markdown('📘 **More Information about my New Book**')
    # st.image("https://www.dropbox.com/scl/fi/o9os3igy46ynjzw2stt1a/Structural-Engineering2.png?rlkey=so80xqe0zuj3ilsdlwm4awkmz&st=9v750dgq&raw=1", use_column_width=True)
    st.image("https://www.dropbox.com/scl/fi/o9os3igy46ynjzw2stt1a/Structural-Engineering2.png?rlkey=so80xqe0zuj3ilsdlwm4awkmz&st=9v750dgq&raw=1", use_container_width=True)
    st.markdown(
        """
        <div style="text-align: center;">
        <a href="https://fragrant-knight-4af.notion.site/My-Personal-Page-for-Academic-Use-5c5f007b3f3f4c76a604960d9dbffca7"> Online Book </b></a>
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.markdown(
    """
    **Structural Engineering: Dynamics, Seismic Solution, and AI Integration**

    In an era where structural engineering faces multifaceted challenges, this book offers an integrated approach that melds core dynamics, seismic-resistant design techniques, and the transformative potential of AI in modern structural solutions. Beginning with foundational principles, readers are ushered into the intricate world of structural dynamics, with a spotlight on the importance of understanding multi-degree of freedom systems. As societies grapple with the increasing prominence of seismic threats, the imperative for resilient construction methods is laid bare.

    However, it's paramount to note that this work doesn't aspire to replace or overshadow the comprehensive mathematical insights found in the seminal works of the discipline or the invaluable depth of formal university education. Rather, this book positions itself as a supplementary resource, designed to complement these foundational sources of knowledge. By bridging the gap between time-honored techniques and contemporary technological advancements, it underscores the evolving synergy between traditional engineering practices and modern AI-driven tools.

    Harnessing the power of discrete mathematics, the book reveals how automation is revolutionizing the field, not just simplifying but also optimizing the design process. In ensuring structural safety and cost-effectiveness, it aims to pave a path toward a future where structures are not only robust against threats but are also emblematic of efficiency and innovation. Dive in to discover a confluence of tradition and technology, all designed to enhance and enrich the existing knowledge landscape of structural engineering.
    """
    )

    ### University ###
    st.sidebar.markdown('#### 🎓 **About the PUCE University**')
    with st.sidebar.expander("**Click to read more**"):
        # st.image("https://conexion.puce.edu.ec/wp-content/uploads/2021/11/M7A4696-1024x683.jpg", use_column_width=True)
        st.image("https://conexion.puce.edu.ec/wp-content/uploads/2021/11/M7A4696-1024x683.jpg", use_container_width=True)
        st.markdown(
            """
            The Pontifical Catholic University of Ecuador (PUCE), founded in 1946, is one of the most prestigious universities in Ecuador. It offers a wide range of undergraduate and postgraduate programs across various disciplines, fostering a rich environment for research and academic excellence. The university is dedicated to the holistic development of its students, emphasizing both academic rigor and ethical values.
            
            **Mission and Vision**:
            
            PUCE aims to contribute to society by training competent, ethical professionals committed to the development of their communities and the country. The university focuses on creating knowledge through research and innovation, promoting cultural and social activities that enrich the educational experience.
            
            **Notable Achievements**:
            
            * Extensive research output with numerous publications in international journals.
            * Strong emphasis on community engagement and social responsibility.
            * Wide network of international collaborations and exchange programs.
            
            For more information, visit the [**PUCE website**](https://www.puce.edu.ec/).
            """
        )

    st.sidebar.markdown('#### 🌎 **About Ecuador**')
    with st.sidebar.expander("**Click to read more**"):
        # st.image("https://www.dropbox.com/scl/fi/6eogj3i8n39lvwq8zmj81/PortadaProyecto-10_PatricioPalacios.png?rlkey=j65628ycr0ncgsy50gsiy4wxu&st=kfhgkoop&dl&raw=1", use_column_width=True)
        st.image("https://www.dropbox.com/scl/fi/6eogj3i8n39lvwq8zmj81/PortadaProyecto-10_PatricioPalacios.png?rlkey=j65628ycr0ncgsy50gsiy4wxu&st=kfhgkoop&dl&raw=1", use_container_width=True)
        st.markdown(
            """
            Ecuador, located on the west coast of South America, is renowned for its stunning natural beauty, megadiversity, and vibrant culture. From the lush Amazon rainforest to the breathtaking Andes mountains and the beautiful beaches of the Pacific coast, Ecuador offers a diverse range of landscapes and ecosystems.
            
            **Biodiversity**:
            
            Ecuador is one of the most biodiverse countries in the world, home to a vast array of flora and fauna. The Galápagos Islands, a UNESCO World Heritage site, are famous for their unique wildlife and played a crucial role in Charles Darwin's theory of evolution.
            
            **Culture and People**:
            
            Ecuador boasts a rich cultural heritage, with influences from indigenous, Spanish, and African traditions. The capital city, Quito, is known for its well-preserved colonial architecture and is also a UNESCO World Heritage site. Ecuadorians are known for their warm hospitality and vibrant traditions.
            
            **Cosmopolitan Cities**:
            
            Cities like Quito and Guayaquil offer a blend of modern amenities and historical charm. These cosmopolitan hubs are centers of commerce, culture, and education, offering a dynamic lifestyle for residents and visitors alike.
            
            For more information, visit the [**Ecuador Travel website**](https://ecuador.travel/en/).
            """
        )


######################################################## header ########################################################
image_path = 'https://www.dropbox.com/scl/fi/y0c4h21d3ymdowbvj6o21/logo_TorreFuerte.png?rlkey=5iwsegde7z8b7k59b54nrj1y8&st=jfn90j36&raw=1'
url = 'https://juant27.sg-host.com/'  # Replace this with your desired URL
st.markdown(f'<a href="{url}" target="_blank"><img src="{image_path}" width="100%"></a>', unsafe_allow_html=True)

# App Title
col1, col2  = st.columns([1,1])
with col1:
    st.markdown(
        """
        * Author: [Msc. Ing. Carlos Andrés Celi Sánchez](https://fragrant-knight-4af.notion.site/Main-Page-5c5f007b3f3f4c76a604960d9dbffca7?pvs=4)
        * University: [PUCE](https://www.puce.edu.ec/)
        * Course: Structural Dynamics
        """
    )
    st.markdown(
        """
        You can find me on : 
        [![Web Page](https://img.shields.io/badge/Web%20Page-caceli.net-blue)](http:caceli.net)
        [![GitHub Carlos Celi](https://img.shields.io/github/followers/Normando1945?label=follow&style=social)](https://github.com/Normando1945)
        [![ResearchGate](https://img.shields.io/badge/-ResearchGate-00CCBB?style=social&logo=researchgate)](https://www.researchgate.net/profile/Carlos-Celi)
        [![Google Scholar](https://img.shields.io/badge/-Google%20Scholar-4285F4?style=social&logo=google)](https://scholar.google.com.ec/citations?hl=es&user=yR4Gz7kAAAAJ)
        [![YouTube](https://img.shields.io/badge/-YouTube-FF0000?style=social&logo=youtube)](https://www.youtube.com/@CCeli1945)
        """
    )
with col2:
    st.markdown(
            """
            If you found this free application useful and enjoyable, please consider supporting us with a donation. Your contribution helps us continue developing and maintaining free software.
            """
        )
    j1, j2, j3 = st.columns([0.2,1,0.2])
    with j1:
        st.metric(label= "",value="")
    with j2:
        components.html(
            """
            <script type='text/javascript' src='https://storage.ko-fi.com/cdn/widget/Widget_2.js'></script><script type='text/javascript'>kofiwidget2.init('Support Me on Ko-fi', '#29abe0', 'H2H111V2R3');kofiwidget2.draw();</script> 
            """,
        )
    with j3:
        st.metric(label= "",value="")


# ######################################################## Author ########################################################
# st.markdown('##### 😎 **About the Author**')
# with st.expander("**Click to read more**"):
#     coll1, coll2 = st.columns([1,1])
#     with coll1:
#         st.image("https://www.dropbox.com/scl/fi/24umxisfp4tedeqzndj3n/foto.jpg?rlkey=4yrliifi3xjuhbmjbhh1zrjv8&st=widakesu&raw=1", width= 325)
#         # st.image("https://raw.githubusercontent.com/Normando1945/Simple-Python-Matlab-JavaSript-Functions-Collection/main/fun_SPEC_NEC/assets/foto.jpg", width= 325)
#     with coll2:
#         st.markdown(
#             """
#             **Short Curriculum Vitae Overview**.

#             I am Ecuadorian, I have a Master's degree in Structural Engineering with a **SUMMA CUM LAUDE** distinction from the National Polytechnic School. With over 15 years of experience, I have notably provided structural consultancy for buildings surpassing 140 meters in height. I am currently affiliated with the Department of Civil Engineering at the [**Pontifical Catholic University of Ecuador**](https://www.puce.edu.ec/). My primary research domain is nonlinear mathematical modeling, leading to several 
#             international scientific publications. My ongoing projects include:
            
#             * The Application of Artificial Neural Networks (ANN) in Estimating Local Fragility in Zero-Length Elements.
#             * Generating Synthetic Accelerograms based on Chaos Theory and Wavelets.
#             * Participation in the 'Training And Communication for Earthquake Risk Assessment - GEM' project.
            
#             """
#         )

#     st.markdown(':ledger: **More Information about my New Book**')
#     jj1, jj2 = st.columns([1, 1])
#     with jj1:
#         st.image("https://www.dropbox.com/scl/fi/o9os3igy46ynjzw2stt1a/Structural-Engineering2.png?rlkey=so80xqe0zuj3ilsdlwm4awkmz&st=9v750dgq&raw=1", width= 300)
#         # st.image("https://raw.githubusercontent.com/Normando1945/Simple-Python-Matlab-JavaSript-Functions-Collection/main/fun_SPEC_NEC/assets/Structural Engineering2.png", width= 300)
#         st.markdown(
#             """
#             <div style="text-align: center;">
#             <a href="https://fragrant-knight-4af.notion.site/My-Personal-Page-for-Academic-Use-5c5f007b3f3f4c76a604960d9dbffca7"> Online Book </b></a>
#             </div>
#             """, 
#             unsafe_allow_html=True
#         )
#     with jj2:
#         st.markdown(
#         """
#         **Structural Engineering: Dynamics, Seismic Solution, and AI Integration**
    
#         In an era where structural engineering faces multifaceted challenges, this book offers an integrated approach that melds core dynamics, seismic-resistant design techniques, and the transformative potential of AI in modern structural solutions. Beginning with foundational principles, readers are ushered into the intricate world of structural dynamics, with a spotlight on the importance of understanding multi-degree of freedom systems. As societies grapple with the increasing prominence of seismic threats, the imperative for resilient construction methods is laid bare.
    
#         However, it's paramount to note that this work doesn't aspire to replace or overshadow the comprehensive mathematical insights found in the seminal works of the discipline or the invaluable depth of formal university education. Rather, this book positions itself as a supplementary resource, designed to complement these foundational sources of knowledge. By bridging the gap between time-honored techniques and contemporary technological advancements, it underscores the evolving synergy between traditional engineering practices and modern AI-driven tools.
    
#         Harnessing the power of discrete mathematics, the book reveals how automation is revolutionizing the field, not just simplifying but also optimizing the design process. In ensuring structural safety and cost-effectiveness, it aims to pave a path toward a future where structures are not only robust against threats but are also emblematic of efficiency and innovation. Dive in to discover a confluence of tradition and technology, all designed to enhance and enrich the existing knowledge landscape of structural engineering.
#         """
#         )

######################################################## Description ########################################################
st.markdown(
    '''
    ##### :open_book: Description of this Simple App
    
    This simple app performs spectral calculations using the NEC-SE-DS-2024 Ecuadorian Code. It computes the Elastic and Inelastic Acceleration Response Spectra for a range of structural periods and visualizes the results.
    
    '''
    )

######################################################## More Information ########################################################
st.markdown('##### :ledger: **More Information about this Simple App**')
with st.expander("**Click to read more**"):
    j1, j2 = st.columns([1, 2])
    with j1:
        image_path = 'https://www.dropbox.com/scl/fi/f1ha8s6021wyf432j0f2f/Chapter1_portada.gif?rlkey=m0iozpmg7rz5p59t6z8jggnfa&st=ice80to1&raw=1'
        # image_path = 'https://raw.githubusercontent.com/Normando1945/Simple-Python-Matlab-JavaSript-Functions-Collection/main/fun_SPEC_NEC/Chapter1_portada.gif'
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




######################################################## user parameters ########################################################

n = st.number_input('**n**: Ratio between spectral ordinates **Sa(T = 0.1 s)** and **PGA**:', value=2.40, step=0.1)
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
    R = st.number_input('**R**: Seismic response reduction factor:', value=7.0, step=0.5)

with col4:
    I = st.number_input('**I**: Importance coefficient [for different structures]:', value=1.0, step=0.1)
    r = st.number_input('**r**: Geographic zone factor [for Ecuador]:', value=1.0, step=0.1)

dt = 0.005
Tf = 5

######################################################## Code ########################################################
fads = [fa, fd, fs]

To = 0.10 * fads[2] * fads[1] / fads[0]
Tc = 0.45 * fads[2] * fads[1] / fads[0]
Tl = 2.4 * fads[1]

Sae = []
Sai = []
Tie = []

for T in np.arange(0, Tf, dt):
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
            if T <= Tl:
                Sae.append([I * n * z * fads[0] * (Tc / T) ** r])
                Sai.append([I * n * z * fads[0] * (Tc / T) ** r / (R * fip * fie)])
                Tie.append([T])
            else:
                Sae.append([I * n * z * fads[0] * (Tc / T) ** r * (Tl / T) ** 2])
                Sai.append([I * n * z * fads[0] * (Tc / T) ** r * (Tl / T) ** 2 / (R * fip * fie)])
                Tie.append([T])


Resul = pd.DataFrame({ 'Period [s]': Tie,'Sae [g]': Sae,'Sai [g]': Sai})
    
Tie = np.array(Tie)
Sae = np.array(Sae)
Sai = np.array(Sai)
Tie = Tie[:, 0]
Sae = Sae[:, 0]
Sai = Sai[:, 0]

# Valores de SDS & SD1
Sds = n * z * fads[0] * I
Sd1 = I * n * z * fads[0] * (Tc / 1) ** r
    

fig1, ax1 = plt.subplots(figsize=(16/1.5, 9/1.5))                                                                
    
ax1.plot(Tie, Sae, color=(0, 0, 0), marker='+', markersize=0, markerfacecolor='w',                             
markeredgewidth=0, linewidth=1.5, alpha=1.0,linestyle = '-',label= f'Elastic Response Spectra')
ax1.plot(Tie, Sai, color=(0, 0, 1), marker='+', markersize=0, markerfacecolor='w',                              
markeredgewidth=0, linewidth=1.5, alpha=1.0,linestyle = '-',label= f'Inelastic Response Spectra')

ax1.plot([0.3,0.3], [0,Sds], color=(0.5, 0.5, 0.5), marker='o', markersize=5, markerfacecolor='white',                              
markeredgewidth=1, linewidth=1.0, alpha=1.0,linestyle = '--')
ax1.plot([1,1], [0,Sd1], color=(0.5, 0.5, 0.5), marker='o', markersize=5, markerfacecolor='white',                              
markeredgewidth=1, linewidth=1.0, alpha=1.0,linestyle = '--')

ax1.text(0.3, Sds + 0.01, f'Sds = {Sds:.3f} g', fontsize=10, verticalalignment='bottom', horizontalalignment='left')
ax1.text(1, Sd1 + 0.01, f'Sd1 = {Sd1:.3f} g', fontsize=10, verticalalignment='bottom', horizontalalignment='left')

ax1.set_xlim([Tie[0], (max(Tie))])                                                                               
ax1.set_ylim([0, (max(Sae)*1.05)])                                                                              
plt.title('SPEC NEC-SE-DS-2024', fontsize=10, color=(0, 0, 1))                                                      
plt.xlabel('Period (T) [s]', rotation=0, fontsize=10, color=(0, 0, 0))                                          
plt.ylabel('Max Response Acceleration (Sa) [g]', rotation=90, fontsize=10, color=(0, 0, 0))                     
legend = plt.legend(fontsize=10)                                                                               
legend.get_frame().set_edgecolor('none')                                                                       
ax1.grid(which='both', axis='x', alpha=0.5) 

# plt.show()                                                                     
    
st.pyplot(fig1)


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

st.markdown('##### 📊 **Response Spectra [Elastic and Inelastic]**')

col1, col2 = st.columns([1, 3])
with col1:
    # st.image(random_gif, use_column_width=True)
    st.image(random_gif, use_container_width=True)
with col2:
    with st.chat_message("assistant"):
        st.write(random_message)

o1, o2 = st.columns([1,2])
with o1:
    st.metric(label='Max Sae', value=f"{np.max(Sae):.4f}", delta='g')
    st.metric(label='Max Sai', value=f"{np.max(Sai):.4f}", delta='g')
    st.metric(label='Sds', value=f"{Sds:.4f}", delta='g')
    st.metric(label='Sd1', value=f"{Sd1:.4f}", delta='g')
with o2:
    st.write(Resul)
    


st.markdown('##### ⚠️ **Disclaimer**')
st.markdown(
    '''
    This application is provided solely for academic purposes. The user bears full responsibility for the scope and application of this tool. The developers disclaim any liability for misuse or any unintended consequences arising from the use of this application.
        
    [![Creative Commons License](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
    ''', unsafe_allow_html=True
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
        <img class="logo" src="https://www.dropbox.com/scl/fi/y0c4h21d3ymdowbvj6o21/logo_TorreFuerte.png?rlkey=5iwsegde7z8b7k59b54nrj1y8&st=jfn90j36&raw=1" alt="TorreFuerte Logo">
        <div class="separator"></div>
        <div>
            <p>Developed by Carlos Celi | <a href="https://www.http://torrefuerte.ec" target="_blank">TORREFUERTE</a> | <a href="https://www.caceli.net" target="_blank">Carlos Celi</a> | <a href="https://github.com/Normando1945" target="_blank">GitHub</a></p>
            <p>© Version 1.0.2 - July, 2024</p>
        </div>
    </div>
    """
    
    st.markdown(footer, unsafe_allow_html=True)

display_footer()


