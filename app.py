from re import S
from turtle import width
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time


import pickle
pickle_in=open('rfClassifier.pkl','rb')
classifier = pickle.load(pickle_in)

def main():
    st.sidebar.title('**MENU**')
    activities=["[$$-PREDICTION-$$]","[-ABOUT-]"]
    choice = st.sidebar.selectbox("Select",activities)

    if choice=="[$$-PREDICTION-$$]" :

        st.header("**length**")
        length = st.text_input('length')
        st.write("--------------------------------")

        st.header("**width**")
        width=st.text_input('width')
        st.write("--------------------------------")

        st.header("**avgWind**")
        avgWind=st.text_input('avgWind')
        st.write("--------------------------------")

        st.header("**country**")
        country_col = st.selectbox(label='',options=["India","Dubai","England","Pakistan","Australia","Sri Lanka",
                                    "Afghanistan","Bangladesh","New Zealand","South Africa","West Indies"])
    
        if country_col=='India':
            cc=[1,0,0,0,0,0,0,0,0,0,0]
        if country_col=='Dubai':
            cc=[0,1,0,0,0,0,0,0,0,0,0]
        if country_col=='England':
            cc=[0,0,1,0,0,0,0,0,0,0,0]
        if country_col=='Pakistan':
            cc=[0,0,0,1,0,0,0,0,0,0,0]
        if country_col=='Australia':
            cc=[0,0,0,0,1,0,0,0,0,0,0]
        if country_col=='Sri Lanka':
            cc=[0,0,0,0,0,1,0,0,0,0,0]
        if country_col=='Afghanistan':
            cc=[0,0,0,0,0,0,1,0,0,0,0]
        if country_col=='Bangladesh':
            cc=[0,0,0,0,0,0,0,1,0,0,0]
        if country_col=='New Zealand':
            cc=[0,0,0,0,0,0,0,0,1,0,0]
        if country_col=='South Africa':
            cc=[0,0,0,0,0,0,0,0,0,1,0]
        if country_col=='West Indies':
            cc=[0,0,0,0,0,0,0,0,0,0,1]


        st.write("--------------------------------")


        st.header("**pitch**")
        pitch_col = st.selectbox(label='',options=["Dead","Dusty","Green"])

        if pitch_col=='Dead':
            pc=[1,0,0]
        if pitch_col=='Dusty':
            pc=[0,1,0]
        if pitch_col=='Green':
            pc=[0,0,1]

        st.write("--------------------------------")

        data=[]
        data.extend([length])
        data.extend([width])
        data.extend([avgWind])
        data=data+cc
        data=data+pc
        

        def saved_testing_rf(data):
    
            data_list = list((np.array(data)).reshape(-1))

            df = pd.DataFrame()
            col_names = ['f%d' % i for i in range(17)]
            df = df.append(pd.Series(data=data_list, index=col_names), ignore_index=True)

            result1 = classifier.predict(df)
            
            return np.around(int(result1))

        #pred = saved_testing_rf([120,112,20,0,0,0,0,0,1,0,0,0,0,0,1,0,0])
        #st.write(pred)
        #st.write(data)
        pred1=saved_testing_rf(data)

        if st.button(' SCORE '):
            with st.spinner(text=":tophat: PREDICT :tophat:"):
                time.sleep(1)
                st.warning(':space_invader:   :house:   :space_invader: ')
                st.balloons()
                st.success("Predicted Score :  {}".format(pred1))
        #st.write(pred1)


if __name__ == '__main__':
    main()