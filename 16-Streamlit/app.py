import streamlit as st
import pandas as pd
import numpy as np

#Title of the application
st.title("Hello Streamlit")

#display a simple text
st.write("This is the simple text written by Harsh on 3 Sep, 2026")

#create a simple dataframe

df = pd.DataFrame({
  'first col': [1,2,3,4],
  'second col': [5,6,7,8]
})

#Display the datafrane

st.write("display the data frame")
st.write(df)

#create a line chart
chart_data= pd.DataFrame(
  np.random.randn(20,3), columns=['a','b','c']
)
st.line_chart(chart_data)