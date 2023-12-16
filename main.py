import sys
import streamlit as st
from DataProcessing import Data
from Plottingandcharts import plots
from Predict import predict
sys.path.insert(1, r'SingaporeResaleFlatPricesPredicting\venv\Lib\site-packages')
import streamlit_option_menu

st.set_page_config(layout="wide",page_title="SingaporeResaleFlatPricesprediction")


selected = streamlit_option_menu.option_menu("Menu", ["About", "Data","Plots and Charts",'Prediction','Contact'],
                                                 icons=["exclamation-circle","search","bar-chart","globe",'telephone-forward' ],
                                                 menu_icon= "menu-button-wide",
                                                 default_index=0,
                                                 orientation="horizontal",
                                                 styles={"nav-link": {"font-size": "15px", "text-align": "centre",  "--hover-color": "#d1798e"},
                        "nav-link-selected": {"background-color": "#b30e35"}})

if selected=="About":
    st.header(":green[Singapore Flat re-sale price prediction]")
    st.subheader(":red[Technology:]")
    st.text("Data Wrangling, EDA, Model Building, Model Deployment")
    st.subheader(":violet[Domain:]")
    st.text("Real Estate")
    st.text("About:")
    st.markdown("""
    Predicting Singapore's flat resale prices accurately is a challenging task due to the dynamic nature of the housing market. Various stakeholders,including real estate analysts, property agents, and economists, rely on historical trends, economic data, market sentiment, and  government policies to make informed predictions. However, unforeseen events such as a global economic downturn,
    changes in government policies, or unexpected market shocks can quickly disrupt any forecasted trends.While it is difficult to predict exact figures, monitoring market indicators, analyzing housing policies, and
    understanding economic factors can provide valuable insights into the direction of Singapore's flat resale prices. However, buyers and sellers should always exercise caution and seek professional advice when making decisions in the dynamic real estate market of Singapore.
    This application aids to predict the resale prices.
""")
if selected=="Data":
    Data()

if selected=="Prediction":
    predict()

if selected=="Plots and Charts":
    plots()

if selected=='Contact':
    page_bg_img = '''
        <style>
        [data-testid="stAppViewContainer"] {
        background-image: url("https://st.depositphotos.com/1038225/3793/i/600/depositphotos_37937771-stock-photo-wood-background-texture.jpg");
        background-size: cover;
        }
        </style>
        '''

    st.markdown(page_bg_img, unsafe_allow_html=True)
    col1, col2, col3 =st.columns(3)
    with col1:
        st.markdown(":violet[About me:]")
        st.markdown("Name: :orange[Vinoth Palanivel]")
        st.markdown(":green[Aspiring Data Scientist]")
        st.write("Degree: :green[Bachelor of Engineering in Electrical and Electronics Engineering]")
        st.write("E-mail: :green[vinothchennai97@gmail.com]")
        st.write("Mobile: :green[7904197698 or 9677112815]")
    with col2:
        st.markdown(":violet[Links to connect with me:]")
        st.write("Linkedin: :orange[https://www.linkedin.com/in/vinoth-palanivel-265293211/]")
        st.write("Github: :orange[https://github.com/Vinoth0208/]")
    with col3:
        st.write(":violet[Project links:]")
        st.write("1. https://github.com/Vinoth0208/Youtube_Project_For_DataScience")
        st.write("2. https://github.com/Vinoth0208/PhonepePulse")
        st.write("3. https://github.com/Vinoth0208/Bizcard")
        st.write("4. https://github.com/Vinoth0208/Airbnb")
