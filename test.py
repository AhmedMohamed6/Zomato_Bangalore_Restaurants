
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
import joblib

columns = joblib.load('inputs.pkl')
model = joblib.load('model.pkl')
location_values = joblib.load('location.pkl')
rest_type_values = joblib.load('rest_type.pkl')
cuisines_values = joblib.load('cuisines.pkl')
type_values = joblib.load('type1.pkl')
city_values = joblib.load('city.pkl')

def prediction(online_order, book_table, location, rest_type, cuisines, avg_cost, typee, city):
    df = pd.DataFrame(columns=columns)
    df.at[0,'online_order'] = online_order
    df.at[0,'book_table'] = book_table
    df.at[0,'location'] = location
    df.at[0,'rest_type'] = rest_type 
    df.at[0,'cuisines'] = cuisines 
    df.at[0,'approx_cost'] = avg_cost
    df.at[0,'type'] = typee
    df.at[0,'city'] = city


    res = model.predict(df)
    return res[0]
    
    


def main():
    st.title('Zomato Bangalore Restaurants :fork_and_knife:')
    online_order = st.selectbox('Has online order ?', ['Yes', 'No'])
    book_table = st.selectbox('Prebooking ?', ['Yes', 'No'])
    location = st.selectbox('Location:', location_values)
    
    
    rest_type = st.selectbox('Restaurant type:', rest_type_values)
    cuisines = st.selectbox('Cuisines:', cuisines_values)
    
    avg_cost = st.slider("Approximate cost for two persons:", min_value=30, max_value=7000, step = 1, value = 600 )
    typee = st.selectbox('Another restaurant type:', type_values)
    city = st.selectbox('City:', city_values)
    
   # Display user inputs
    st.write("^-^ User Inputs:")
    st.write(f"Online Order: {online_order}")
    st.write(f"Book Table: {book_table}")
    st.write(f"Location: {location}")
    st.write(f"Rest Type: {rest_type}")
    st.write(f"Cuisines: {cuisines}")
    st.write(f"Approximate Cost: {avg_cost}")
    st.write(f"Type: {typee}")
    st.write(f"City: {city}")
    
    if st.button(":star2:Predict:star2:"):
        
        result = prediction(online_order, book_table, location, rest_type, cuisines, avg_cost, typee, city)
        st.text(f"The expected poits this player could score is : {result}")

main()
