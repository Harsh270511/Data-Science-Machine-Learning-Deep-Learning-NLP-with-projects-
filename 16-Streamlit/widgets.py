import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")


name= st.text_input("Enter your name")


age = st.slider("Select your age: ",0,100,25)
st.write(f"Your age is : {age}")


options=["Python","AI","ML","DL","NLP"]
choics = st.selectbox("choose your end goal", options)
st.write(f"you select {choics}")
if name:
  st.write(f"Hello Mr. {name}")


data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}
df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)


upload_file = st.file_uploader("Choose a CSV file", type="csv")
if upload_file is not None:
  df= pd.read_csv(upload_file)
  st.write(df)
