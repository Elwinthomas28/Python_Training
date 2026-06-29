import streamlit as st 
st.title("password manager")
password=st.text_input("enter the password",type="password")
st.button("validate")