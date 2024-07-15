import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
from datetime import datetime
import pytz


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


st.sidebar.title("**Welcome to Simple App: Time History Response, SDOF (B_Newmark)**")

# Obtener la fecha y hora actual en Quito, Ecuador
ecuador_tz = pytz.timezone('America/Guayaquil')
current_time = datetime.now(ecuador_tz)
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# Mostrar la fecha y hora en el sidebar
st.sidebar.markdown(f"**Current Date and Time in Quito, Ecuador:**\n\n{formatted_time}")

## Author ##
st.sidebar.markdown('#### 😎 **About the Author**')
with st.sidebar.expander("**Click to read more**"):
    st.image("https://www.dropbox.com/scl/fi/24umxisfp4tedeqzndj3n/foto.jpg?rlkey=4yrliifi3xjuhbmjbhh1zrjv8&st=widakesu&raw=1",  use_column_width=True)
       
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
    st.image("https://www.dropbox.com/scl/fi/o9os3igy46ynjzw2stt1a/Structural-Engineering2.png?rlkey=so80xqe0zuj3ilsdlwm4awkmz&st=9v750dgq&raw=1", use_column_width=True)
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
        st.image("https://conexion.puce.edu.ec/wp-content/uploads/2021/11/M7A4696-1024x683.jpg", use_column_width=True)
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
        st.image("https://d3rhcahk56mofm.cloudfront.net/eyJrZXkiOiJtZWRpYS9iYzMyODNlYS0yYjI1LTRmYWEtYTA2Yy0xM2VlODhmMjhiMjEuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7IndpZHRoIjozMDcuNSwiaGVpZ2h0IjozNzAuNX0sIndlYnAiOnsibG9zc2xlc3MiOmZhbHNlLCJxdWFsaXR5Ijo4MCwibmVhckxvc3NsZXNzIjpmYWxzZSwic21hcnRTdWJzYW1wbGUiOmZhbHNlfX19", use_column_width=True)
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


## # line of run c:\users\normando\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\scripts\streamlit.exe run BNewmark_app.py


######################################################## header ########################################################
# # image_path = 'https://raw.githubusercontent.com/Normando1945/Simple-Python-Matlab-JavaSript-Functions-Collection/main/fun_SPEC_NEC/logo_TorreFuerte.png'
image_path = 'https://www.dropbox.com/scl/fi/y0c4h21d3ymdowbvj6o21/logo_TorreFuerte.png?rlkey=5iwsegde7z8b7k59b54nrj1y8&st=jfn90j36&raw=1'
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

######################################################## Description ########################################################
st.markdown(
    '''
    ##### 📖 **Description of this Simple App**
    This simple application performs step-by-step calculations of the displacement, velocity, and acceleration response of a single-degree-of-freedom (SDOF) structure, whether conservative or non-conservative, subjected to ground motion using the Newmark method.
    
    ##### 📥 **Seismic Records**
    This simple application utilizes the PEER format, enabling you to download seismic records directly from the [**PEER Ground Motion Database**](https://ngawest2.berkeley.edu/). Additionally, you can download .AT2 files with real earthquake examples in the required format from the following [**repository**](https://github.com/Normando1945/Simple-Python-Matlab-JavaSript-Functions-Collection/tree/main/fun_BNewmark/Simple_App/Records_Zip/Examples%20of%20Seismic%20Records%20PEER)
    
    '''
)

######################################################## More Information ########################################################
st.markdown('##### :ledger: **More Information about this Simple App**')
with st.expander("**Click to read more**"):
    j1, j2 = st.columns([1, 2])
    with j1:
        # image_path = 'https://raw.githubusercontent.com/Normando1945/Simple-Python-Matlab-JavaSript-Functions-Collection/main/fun_SPEC_NEC/Chapter1_portada.gif'
        image_path = 'https://www.dropbox.com/scl/fi/f1ha8s6021wyf432j0f2f/Chapter1_portada.gif?rlkey=m0iozpmg7rz5p59t6z8jggnfa&st=ice80to1&raw=1'
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
data = []

uploaded_file = st.file_uploader(
    "Upload a AT2 file",
    type=["AT2"],
    help="Read the Documentation",
)


col1, col2 = st.columns([1,2])
with col1:
    if uploaded_file is not None:
        ####################################### Using CCeli Format #######################################
        # # Read the contents of the uploaded file
        # contents = uploaded_file.getvalue().decode('utf-8')
        # lines = contents.splitlines()
        # data = []
        # for line in lines:
        #     time, accel = line.split()
        #     data.append((float(time), float(accel)))
        
        ####################################### Using PEER format #######################################
        # Define the cutoff frequencies for the low-pass and high-pass filters
        lowcut = 0.1                                            # low-frequency cutoff in Hz
        highcut = 20.0                                          # high-frequency cutoff in Hz
        order = 4                                               # Define the order of the Butterworth filter
        if uploaded_file is not None:
            contents = uploaded_file.getvalue().decode('utf-8')
            lines = contents.split('\n')    # Split the contents into lines and extract the acceleration values and the DT value
            first_four_lines = lines[:4]    # F|irts 4 Lines (Header of the file)
            linex = lines[3]                # Extract the fourth line where the DT value is alocated
            values = linex.split()          # Split the line by space
            indexx = values.index("DT=")    # Find the index of the string "DT="
            DT_value = values[indexx + 1]   # Get the numeric value following "DT="

            accel = []                      # variable in which all the acceleration of the current signal will be recorded
            for line in lines[4:]:
                values = line.split()       # variable in which the numereic values of each "Line" will be recorded
                if len(values) == 5:        # set the maximum numeric values per line
                    accel.extend(values)    # record the numeric values
            accel = [float(value) for value in accel]
            ########################  Filtering the signal ########################################
            sample_rate = 1/float(DT_value)
            nyquist = 0.5 * sample_rate
            low = lowcut / nyquist
            high = highcut / nyquist
            b, a = butter(order, [low, high], btype='band')
            filtered_signal = lfilter(b, a, accel)
            time = np.arange(0, len(filtered_signal)*float(DT_value), float(DT_value))
            rec1 = np.column_stack((time, filtered_signal))
            last_time_value = time[-1]
            rec1 = list(rec1)
            data = rec1
        
        
        
        Seismic = pd.DataFrame(data, columns=["Time [s]", "Acceleration [g]"])

        # Display the Seismic Data
        st.markdown('**Seismic Data**')
        st.write(Seismic)

with col2:
    if not data:
        st.markdown('**Please upload an AT2 file**')
    else:
        # st.markdown('**Select Record**')
        st.metric(label='Name of the file', value=uploaded_file.name)
        st.markdown("**File Header Information**")
        for line in first_four_lines:
            st.write(line)
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


if not data:
    st.markdown('**---------------------------------------------------------------------------------------------------------------------------------------**')
else:

    ######################################################## user parameters ########################################################
    col1, col2 = st.columns([1,1])

    # User input for parameters with descriptions
    with col1:
        T = st.number_input('**T**: Structural Period [s]:', value=0.15, step=0.05)
    with col2:
        zi = st.number_input('**ξ**: Damping Factor:', value=0.05, step=0.01)

    error_gifs = [
        "https://media4.giphy.com/media/EbeeDkvlC3fFRGJ6Om/200.webp?cid=ecf05e47pr1lqu1ercua819ufpxbbjc92z3b6eerc825ilv1&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media0.giphy.com/media/l46CyJmS9KUbokzsI/200.webp?cid=ecf05e47p7yoa7op690nbgwgkure3taa6lkosgjcx1ne97d2&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTR5Z3phcnZrb3FuMTNjN2gwZWJuY3RjYnR6ZG5pNjdrYmhwa2JxMCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/TNYy8aY7yateU/giphy.webp",
        "https://media1.giphy.com/media/z8rEcJ6I0hiUM/200.webp?cid=ecf05e47tbus30qqlv4zn20qz98yaruncas11gxsxn5nbmu4&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjBpajhpNHU3MXd5eHpxNGJ3NDRwdGJyZ2RvaXdybmdyY2R3NHJtYiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/27EhcDHnlkw1O/200.webp"
        "https://media0.giphy.com/media/KBaxHrT7rkeW5ma77z/200.webp?cid=790b7611xshnf2t6ods2oiu3d29uqt9t9jxjg3rqkz5p61wo&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media1.giphy.com/media/8bM31J3aa0OWScU0r0/200.webp?cid=ecf05e4703logri2kf23l9iwbdhp8jrb9vk5e6998unhwylr&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media4.giphy.com/media/wRwPiWQFz8dEV58TEI/200.webp?cid=ecf05e47gx5ekqjovmh2fkj4kvdzb7jf1teuq0bgzm1qe4uj&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media3.giphy.com/media/PvxHiFvaPweU8/200.webp?cid=ecf05e47oa1nc4frrayxm0ckfcifrjj2egtux1spbs5sod4v&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media2.giphy.com/media/HX7pvh1mIqImc/200.webp?cid=ecf05e47vlvh19vm4bzu8plfr6y0p0cj402t9w4wcna9rxk7&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media1.giphy.com/media/l0Iy9Qcyz0AwYvuEg/100.webp?cid=ecf05e470z243qlvqds3isa3sl51reevmktnfk9cek9vdwlt&ep=v1_gifs_search&rid=100.webp&ct=g",
        "https://media0.giphy.com/media/RBeddeaQ5Xo0E/200.webp?cid=ecf05e478tckf399izro7j986ml9lkgddzouloli2ya3krnx&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media0.giphy.com/media/l41Ym49ppcDP6iY3C/200.webp?cid=ecf05e47tiwkoqqimmaq41d11qg92tcefbpicpvk84oufxud&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media4.giphy.com/media/VFAke5Xm1TDwjgimyW/200.webp?cid=ecf05e471akr5c1xeaxwbuqlqqustk64yaakt39mq3qmj1ae&ep=v1_gifs_search&rid=200.webp&ct=g",
        "https://media1.giphy.com/media/VEVfqy0Vu4c7xziUUN/200.webp?cid=ecf05e476r5nla3l9lhdpkdd512tswzkx3amtbg0f092m8zt&ep=v1_gifs_search&rid=200.webp&ct=g"
    ]
    if not (0 <= T <= 10) or not (0 <= zi <= 1):
        if not (0 <= T <= 10):
            st.error("The value of the structural period [ T ] should be between 0 and 10.")
        if not (0 <= zi <= 1):
            st.error("The value of the Damping Factor [ ξ ] should be between 0 and 1.")
        
        col1,col2,col3 = st.columns([1,2,1])
        with col2:
            st.image(np.random.choice(error_gifs), use_column_width=False, width=350)
    else:        

        ################################################ Parameters #################################################
        xo = 0                                                                      # Initial condition for displacement
        xvo = 0                                                                     # Initial condition for velocity
        w = (2*np.pi)/T                                                             # Angular frequency
        wz = w*np.sqrt(1-zi**2)                                                     # Natural frequency
        M = 1                                                                       # Mass
        record = uploaded_file.name                                                 # Seismic Record name


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
        ax1.tick_params(axis='both', labelsize=5)

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
        This application is provided solely for academic purposes. The user bears full responsibility for the scope and application of this tool. The developers disclaim any liability for misuse or any unintended consequences arising from the use of this application.
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
