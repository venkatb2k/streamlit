import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = st.slider("Select a value")
st.write(x, "squared is", x * x)

df= pd.DataFrame(    np.random.randn(10, 2),    columns=['x', 'y'])
st.bar_chart(df)




# Create a sample dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
        'Product': ['Apples', 'Apples', 'Apples', 'Oranges', 'Oranges', 'Oranges', 'Pears', 'Pears', 'Pears'],
        'Sales': [100, 200, 300, 50, 75, 125, 75, 100, 150]}
df = pd.DataFrame(data)

# Create a pivot table
pivot = df.pivot_table(values='Sales', index='Name', columns='Product')

# Create a bar chart
fig, ax = plt.subplots()
pivot.plot(kind='line', ax=ax)

# Set chart title and axis labels
ax.set_title('Sales by Product and Name')
ax.set_xlabel('Name')
ax.set_ylabel('Sales')

# Display the chart using Streamlit
st.pyplot(fig)
