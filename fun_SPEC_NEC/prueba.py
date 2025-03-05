import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
from datetime import datetime
import pytz
import os
import string
import random
import shutil
# import pythoncom
# pythoncom.CoInitialize()


if 'executed' not in st.session_state:
    st.session_state.executed = False
    

#############################################################################################################################
#############################################################################################################################
######################################################## Side BAR ###########################################################
#############################################################################################################################
#############################################################################################################################
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


st.sidebar.title("**Welcome to: Seismic Disaggregation Tool for Ecuador 2024 (SDTE - 2024)**")


## About the Authors ##
st.sidebar.markdown('#### 😎 **About the Authors**')
with st.sidebar.expander("**Click to read more**"):
    # st.image("https://www.dropbox.com/scl/fi/24umxisfp4tedeqzndj3n/foto.jpg?rlkey=4yrliifi3xjuhbmjbhh1zrjv8&st=widakesu&raw=1",  use_column_width=True)
    st.image("https://www.dropbox.com/scl/fi/24umxisfp4tedeqzndj3n/foto.jpg?rlkey=4yrliifi3xjuhbmjbhh1zrjv8&st=widakesu&raw=1",  use_container_width=True)
       
    st.markdown(
        """
        **Carlos Celi**.
        A summa cum laude master's graduate in Structural Engineering with over 16 years of experience in high-rise building consultancy. Senior engineer at TORREFUERTE and professor, specializing in nonlinear mathematical modeling with international publications
        
        For more information, visit the:
        
        [![Web Page](https://img.shields.io/badge/Web%20Page-caceli.net-blue)](https://fragrant-knight-4af.notion.site/Main-Page-5c5f007b3f3f4c76a604960d9dbffca7?pvs=4)
        
        [![GitHub Carlos Celi](https://img.shields.io/github/followers/Normando1945?label=follow&style=social)](https://github.com/Normando1945)
        
        """
    )
    
    # st.image("https://www.dropbox.com/scl/fi/fo6wg23mlp0zaykwmhpnt/patricio.jpg?rlkey=vywivzcnki46nyoyy7goyfdtc&st=ck0xll4b&dl&raw=1", use_column_width=True)
    st.image("https://www.dropbox.com/scl/fi/fo6wg23mlp0zaykwmhpnt/patricio.jpg?rlkey=vywivzcnki46nyoyy7goyfdtc&st=ck0xll4b&dl&raw=1", use_container_width=True)
       
    st.markdown(
        """
        **Patricio Palacios**.
        A Civil Engineer from the Escuela Politécnica Nacional with a Master's in Structural Research from the Universidad de las Fuerzas Armadas ESPE. He teaches at the Pontifical Catholic University of Ecuador and researches seismic hazard modeling for continental Ecuador, specializing in BIM methodology        
        
        For more information, visit the:
                
        [![GitHub Patricio Palacios](https://img.shields.io/github/followers/ppalacios92?label=follow&style=social)](https://github.com/ppalacios92)
        """
    )
    
    # st.image("https://www.dropbox.com/scl/fi/pqapzmhsdva93urk48gca/jose.jpg?rlkey=w3epr4l9rizrv60f8v3apfem9&st=08d76yga&dl&raw=1", use_column_width=True)
    st.image("https://www.dropbox.com/scl/fi/pqapzmhsdva93urk48gca/jose.jpg?rlkey=w3epr4l9rizrv60f8v3apfem9&st=08d76yga&dl&raw=1", use_container_width=True)
       
    st.markdown(
        """
        **José Poveda**.
        A Civil Engineer (PUCE, 2012), Master's in Seismic Engineering (IUSS Pavia, 2016). Over a decade of experience, professor at Ecuadorian universities, and independent consultant. Currently pursuing PhD, known for practical approach, client interactions, and teamwork at Torrefuerte     
        
        For more information, visit the:
                
        [![GitHub José Poveda](https://img.shields.io/github/followers/JosePovedaHinojosa?label=follow&style=social)](https://github.com/JosePovedaHinojosa)
        """
    )

    
    ### TORREFUERTE ###
    st.sidebar.markdown('#### 🏢 **About the TORREFUERTE**')
    with st.sidebar.expander("**Click to read more**"):
        # st.image("https://www.dropbox.com/scl/fi/h0j8ka62z0vkrxu6lvlei/torrefuerte.png?rlkey=074h6ei1wuti5vsjllj2ep5mc&st=nyb7mr7i&dl&raw=1", use_column_width=True)
        st.image("https://www.dropbox.com/scl/fi/h0j8ka62z0vkrxu6lvlei/torrefuerte.png?rlkey=074h6ei1wuti5vsjllj2ep5mc&st=nyb7mr7i&dl&raw=1", use_container_width=True)
        st.markdown(
            """
            Expert structural engineering company with highly skilled professionals dedicated to overcoming design and structural challenges. 
            
            **Our mission:** provide excellent structural engineering, offering comprehensive and efficient solutions, continuous support, and ensuring safe, high-quality designs that exceed client expectations
            
            For more information, visit the:
            
            [![Web Page](https://img.shields.io/badge/Web%20Page-Torrefuerte.ec-blue)](https://juant27.sg-host.com/)
      
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
            
            For more information, visit the:
            
            [![Web Page](https://img.shields.io/badge/Web%20Page-Ecuador.en-blue)](https://ecuador.travel/en/)
            """
        )


#############################################################################################################################
#############################################################################################################################
######################################################## header #############################################################
#############################################################################################################################
#############################################################################################################################

image_path = 'https://www.dropbox.com/scl/fi/y0c4h21d3ymdowbvj6o21/logo_TorreFuerte.png?rlkey=5iwsegde7z8b7k59b54nrj1y8&st=jfn90j36&raw=1'
url = 'https://juant27.sg-host.com/'  # Replace this with your desired URL
st.markdown(f'<a href="{url}" target="_blank"><img src="{image_path}" width="100%"></a>', unsafe_allow_html=True)


# Título de la aplicación
st.markdown("<h4 style='text-align: center;'>Seismic Disaggregation Tool for Ecuador 2024 (SDTE - 2024)</h4>", unsafe_allow_html=True)

col1, col2  = st.columns([1,1])
with col1:
    st.markdown(
        """
        [![Web Page](https://img.shields.io/badge/Web%20Page-Torrefuerte.ec-blue)](https://juant27.sg-host.com/)
        
        * **Authors:**
        
        Msc. Ing. Carlos Celi. [![GitHub Carlos Celi](https://img.shields.io/github/followers/Normando1945?label=follow&style=social)](https://github.com/Normando1945)
        
        Msc. Ing. Patricio Palacios. [![GitHub Patricio Palacios](https://img.shields.io/github/followers/ppalacios92?label=follow&style=social)](https://github.com/ppalacios92)
        
        PHD(c). Msc. Ing. José Poveda. [![GitHub José Poveda](https://img.shields.io/github/followers/JosePovedaHinojosa?label=follow&style=social)](https://github.com/JosePovedaHinojosa)
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
        

#############################################################################################################################
#############################################################################################################################
######################################################## Description ########################################################
#############################################################################################################################
#############################################################################################################################

j1, j2 = st.columns([1,2])
with j1:
    image_path = 'https://www.dropbox.com/scl/fi/94qin1gz0946us9zd2hxm/SDTE2024.2.jpg?rlkey=16w1vvnp6i52wewz4z881rrxi&st=f7es9y33&dl&raw=1'
    # st.image(image_path, use_column_width=True)
    st.image(image_path, use_container_width=True)

with j2:
    st.markdown(
        '''
        ##### 📖 **Description of this App**
        This application performs disaggregation calculations for fault source areas in Ecuador. Using site-specific coordinates and logic tree configurations, it determines seismic hazard contributions. Disaggregation is crucial for understanding the contribution of different seismic sources to the hazard at a specific site, which helps in designing more resilient structures.
        
        '''
    )

#############################################################################################################################
#############################################################################################################################
#################################################### More Information #######################################################
#############################################################################################################################
#############################################################################################################################
st.markdown('##### :ledger: **Proposal for 2024 Seismic Hazard Model and Seismic Disaggregation Tool for Ecuador using Probabilistic Seismic Hazard Analysis**')

image_path = 'https://www.dropbox.com/scl/fi/6s7gnzoj2l2ybineetsu5/psha2.png?rlkey=qjyh1fx97c1i11g8tgcujgpmr&st=8ol1f98e&dl&raw=1'

st.markdown(
    """
    <style>
    @keyframes wave {
        0% { transform: rotate(0.0deg); }
        10% { transform: rotate(14.0deg); }
        20% { transform: rotate(-8.0deg); }
        30% { transform: rotate(14.0deg); }
        40% { transform: rotate(-4.0deg); }
        50% { transform: rotate(10.0deg); }
        60% { transform: rotate(0.0deg); }  
        100% { transform: rotate(0.0deg); }
    }

    .wave-hand {
        display: inline-block;
        animation: wave 2s infinite;
        transform-origin: 70% 70%;
        font-size: 24px;
    }

    .blinking {
        animation: blinkingText 1.5s infinite;
        font-weight: bold;
        font-size: 18px;
    }

    @keyframes blinkingText {
        0% { color: #007BFF; }
        50% { color: #00BFFF; }
        100% { color: #007BFF; }
    }
    </style>

    <div style="text-align: center;">
        <span class="wave-hand">👉</span> <a href="https://ppalacios92.github.io/HazardMapTest03/HazardMapTest03.html" class="blinking">Interactive Map</a>
    </div>
    """,
    unsafe_allow_html=True
)


st.image(image_path, use_column_width=True)
with st.expander("**Click to read more**"):
    st.markdown(
        '''
        **Authors**
            
        Patricio Palacios, Carlos Celi, José Poveda 
            
        **Abstract**
             
        This work presents an updated proposal for the probabilistic seismic hazard assessment in the continental Ecuador, a country that is consistently exposed to subduction and shallow crustal seismic events. A comprehensive seismic catalog has been compiled based on data from the Instituto Geofisico de la Escuela Politecnica Nacional (2023), incorporating historical seismic records dating from 1587 to 1976, processed and homogenized data spanning from 1901 to March 2013, and recorded information up to 2023. Subsequently, a series of procedures were carried out to shape, process, and homogenize the catalog. The study employs specified source zones from the research conducted by Beauval et al. (2018) and conducts various mathematical modeling processes to derive the resulting seismic hazard map. Utilizing compatible and harmonized ground motion prediction equations with the available dataset, the analysis is further supplemented with probabilistic methods based on initial conditions and logical trees. A standout feature of this research is the development of interactive tools for seismic disaggregation calculations, designed for applicability throughout the continental Ecuador. These Python-based tools are made available to researchers, policymakers, and the public. This model and the accompanying tools aim to enhance the understanding of seismic hazard in Ecuador, building upon previous efforts while leveraging them for a better grasp of this complex subject. However, it is acknowledged that the models generated in this research can be further explored considering advances in the state of the art, therefore, the determination of seismic hazard in the continental Ecuador should remain an ongoing endeavor involving continuous research and updates
             
        ''', unsafe_allow_html=True
    )

st.markdown('##### :scroll: **Parameters**')
st.markdown('You can read the documentation at [**xxxxxxxxxxx**')

with st.expander('📺 **Tutorial Video**'):
    video_url = "https://www.youtube.com/embed/mYc1xVH2Tos"
    st.markdown(f"""
        <div class="centered-iframe-container">
            <iframe src="{video_url}" width="650" height="365" frameborder="0" allowfullscreen></iframe>
        </div>
    """, unsafe_allow_html=True)




#############################################################################################################################
#############################################################################################################################
############################################## csv file and .ini file #######################################################
#############################################################################################################################
#############################################################################################################################
df = []

project_name = st.text_input("Enter the project name:")         # name of the project
if not project_name:
    st.warning("Please enter a project name before uploading files.")
    st.stop()


uploaded_file = st.file_uploader(
    "Upload a csv file",
    type=["csv"],
    help="Read the Documentation",
)

uploaded_file2 = st.file_uploader(
    "Upload a ini file",
    type=["ini"],
    help="Read the Documentation",
)



if uploaded_file is not None and uploaded_file2 is not None:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        file_csv_name = uploaded_file.name
        st.metric(label='Name of the file', value=uploaded_file.name)
        df = pd.read_csv(uploaded_file, skiprows=1, header=0) 
        
        if not df.empty:
            st.write(df)
        else:
            st.write("The uploaded CSV file is empty.")
    
    with col2:
        st.metric(label='Name of the file', value=uploaded_file2.name)
        lines_data = uploaded_file2.getvalue().decode('utf-8').splitlines()                         # Read .ini file
        Lines_ini = pd.DataFrame(lines_data, columns=['Data_from_Configuration ".ini"_file'])       # Convert to DataFrame to see the Data
        
        sites_line = next((line for line in lines_data if "sites" in line), None)                   # Find in the variable the line with the content "sites" and in a varible type 'str'
        if sites_line:
            values_of_site = sites_line.split('=')[1].strip().split()                               # Separate the values of the variable 'str'
            LAT = float(values_of_site[0])                                                          # Save the value Latitude
            LON = float(values_of_site[1])                                                          # Save the value Longitude

        if not Lines_ini.empty:
            st.write(Lines_ini)
        else:
            st.write("The uploaded ini file is empty.")

#############################################################################################################################
#############################################################################################################################
######################################################## CODE ###############################################################
#############################################################################################################################
#############################################################################################################################
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    with col1:
        st.metric(label= "",value="")
    with col2:
        st.metric(label= "Latitude",value=f"{LAT:.5f}", delta='')
    with col3:
        st.metric(label= "Longitude",value=f"{LON:.5f}", delta='')
    with col4:
        st.metric(label= "",value="")

    ecuador_tz = pytz.timezone('America/Guayaquil')
    current_time = datetime.now(ecuador_tz)
    Dia_mes_ano = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    
    ############################# Map of the Location of for the Dissagregation Analysis #####################################
    LaT = [LON]                                                                         # Longitud extracted from the .ini file.
    LoN = [LAT]                                                                         # Latitude extracted from the .ini file.
    Disagre = [Dia_mes_ano]                                                             # Date.

    from World_MAP_LAT_LON import World_Map_LAT_LON                                     # World Map Function imported
    map, latitudes, longitudes, Locations, Date = World_Map_LAT_LON(LaT, LoN, Dia_mes_ano)  # Using of World_Map Function
    ########################################### Code Dissagregation ###########################################################
    
    if st.button("Start the analysis"):
        st.markdown('##### :earth_americas: **Results for Seismic Disaggregation Analysis**')
        # Set the current working directory as the results directory
        st.session_state.folder_path = os.getcwd()
        
        # Function to create a random 5-letter folder name
        def random_string(length=5):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(length))
        
        folder_name = f"{'Results_TF_'+ random_string()}"  # Create a new folder
        folder_path = os.path.join(st.session_state.folder_path, folder_name)
    
        # Create the folder if it does not exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        else:
            print(f"The folder '{folder_path}' already exists!")
        
        # Check if the analysis has already been executed
        if not st.session_state.executed:
            from Dissagregation_functions import Code_dissagregation                                     
            TRT_Rmeans_Mmeans_IMT = Code_dissagregation(df, LAT, LON, file_csv_name, folder_path, project_name)
        
            st.session_state.executed = True  # Mark as executed
            st.session_state.folder_path = folder_path  # Save the folder path
            
            # Only do this if st.session_state.executed is True
            if st.session_state.executed:
                st.markdown(
                    """
                    <div style="font-weight: bold; animation: colorChange 3s infinite;">
                        Due to server restrictions, once you click the download button, the sample results will no longer be visible. However, you can find <strong>ALL</strong> the analysis results in the ZIP file. 
                        If you wish to perform another analysis, please refresh the webpage. Note that due to server restrictions, you might have to wait until another user finishes their calculations.
                    </div>
                    <style>
                    @keyframes colorChange {
                        0% { color: red; }
                        50% { color: blue; }
                        100% { color: red; }
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                )

     
                shutil.make_archive(folder_path, 'zip', folder_path)
            
                with open(f"{folder_path}.zip", "rb") as zip_file:
                    st.download_button(label="Download Results", data=zip_file, file_name=f"{folder_path.split('/')[-1]}.zip")
        else:
            st.markdown('##### :sparkles: The results have been downloaded')

 






    


    
    
##############################################################################################################################
else:
    if uploaded_file is None:
        st.markdown("**Please upload a .csv file.**")
    if uploaded_file2 is None:
        st.markdown("**Please upload a .ini file.**")







#############################################################################################################################
#############################################################################################################################
#################################################### Disclaimer #############################################################
#############################################################################################################################
#############################################################################################################################
st.markdown('##### ⚠️ **Disclaimer**')
st.markdown(
    '''
    This application is provided solely for academic purposes. The user bears full responsibility for the scope and application of this tool. The developers disclaim any liability for misuse or any unintended consequences arising from the use of this application.
        
    [![Creative Commons License](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
    ''', unsafe_allow_html=True
)


#############################################################################################################################
#############################################################################################################################
######################################################## Footer #############################################################
#############################################################################################################################
#############################################################################################################################

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
            <p>Developed by TORREFUERTE | <a href="https://www.http://torrefuerte.ec" target="_blank">TORREFUERTE</a> | </p>
            <p>© Version 1.0.2 (BETA) - August, 2024</p>
        </div>
    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)

display_footer()
