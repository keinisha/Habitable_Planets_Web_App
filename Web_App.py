import numpy as np
import streamlit as st
import pickle
import math

with open('xgboost.pickle', 'rb') as f:
    xgboost = pickle.load(f)

def predicthab(input_data):
    innp = np.asarray(input_data)
    resha = innp.reshape(1, -1)
    prediction = xgboost.predict(resha)
    print(prediction)

    if prediction[0] == 0:
        return 'Not Habitable'
    else:
        return 'Habitable'

def main():
    st.title("Habitable Exoplanets")
    html_temp = """
    <div style="background-color:rgb(32,32,32);padding:10px">
    <h2 style="color:rgb(128,128,128);text-align:center;">Habitable Exoplanet Detection</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    POrbit = st.number_input('POrbit', 0.000001, format="%.6f")
    PRadius = st.number_input('PRadius', 0.000001, format="%.6f")
    PMass = st.number_input('PMass', 0.000001, format="%.6f")
    STemp = st.number_input('STemp', 0.000001, format="%.6f")
    SRadius = st.number_input('SRadius', 0.000001, format="%.6f")
    SMass = st.number_input('SMass', 0.000001, format="%.6f")
    SLum = (math.pow(SRadius, 2)*math.pow((STemp/5778), 4))
    HZCenter = math.sqrt(SLum)
    HZInner = 0.75*HZCenter
    HZOuter = 1.77*HZCenter
    PFlux = ((SLum*13)/math.pow((4*3.14*POrbit), 2))
    PTemp = (PFlux/math.pow((5.67*math.pow(10, -8)*4.361*math.pow(10, -3)), 0.25))
    results = ""
    if st.button('Predict'):
        results = predicthab([POrbit, PRadius, PMass, STemp, SRadius, SMass, SLum, HZCenter, HZInner, HZOuter, PFlux, PTemp])
    st.success('According to the details entered, the planet is {}'.format(results))

if __name__ == '__main__':
    main()
