import streamlit as st 
import pandas as pd
import numpy as np

x = st.slider("Select a value")
st.write(x, "squared is", x * x)

df= pd.DataFrame(    np.random.randn(10, 2),    columns=['x', 'y'])
st.bar_chart(df)
