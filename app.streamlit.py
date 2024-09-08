import streamlit as st
import numpy as np
import altair as alt
import pandas as pd


# Ejemplo 1

st.write("Hola Sungas")

# Ejemplo 2

st.write(1234)

# Ejemplo 3

df = pd.DataFrame({
    "primera Columna": [1,2,3,4,5],
    "Segunda Columna": [6,7,8,9,10],
    "Tercera Columna": [11,12,13,14,15]
    })

# Ejemplo 4

st.write('Dentro de un fragmento de dato', df, 'Acerca de un fragmento de dato')

# Ejemplo 5

df2 = pd.DataFrame(
     np.random.randn(300, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)