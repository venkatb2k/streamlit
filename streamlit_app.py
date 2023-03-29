import streamlit as st
x = st.slider("Select a value")
st.write(x, "squared is", x * x)

import streamlit as stimport pandas as pdimport numpy as npdf= pd.DataFrame(    np.random.randn(10, 2),    columns=['x', 'y'])st.bar_chart(df)
