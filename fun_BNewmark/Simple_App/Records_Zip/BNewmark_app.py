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
    st.sidebar.markdown('##### 🎓 **About the PUCE University**')
    with st.sidebar.expander("**Click to read more**"):
        st.image("data:image/jpeg;base64,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", use_column_width=True)
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
    This simple application utilizes the PEER format, enabling you to download seismic records directly from the [**PEER Ground Motion Database**](https://ngawest2.berkeley.edu/). Additionally, you can download .AT2 files with real earthquake examples in the required format from the following [**repository**](https://github.com/Normando1945/Simple-Python-Matlab-JavaSript-Functions-Collection/tree/main/fun_BNewmark/Simple_App/Records_Zip)
    
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

        #plt.tight_layout()
        #plt.show() 
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
