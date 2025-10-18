import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.title("Interaktiv Grafik")

st.write("Matematik funksiyani `x` o'zgaruvchisi bilan kiriting. Masalan:")
st.code("np.sin(x)*x\nnp.exp(-x**2)\nx**3 - 2*x + 1", language="python")

user_function = st.text_input("Funksiyani kiriting:", "np.sin(x) * x")

x_min = st.number_input("X minimal qiymat", value=-10.0)
x_max = st.number_input("X maksimal qiymat", value=10.0)
points = st.slider("Nuqtalar soni (grafik aniqligi)", 50, 1000, 200)

if st.button("Grafikni chizish"):
    try:
        x_values = np.linspace(x_min, x_max, points)
        y_values = eval(user_function, {"np": np, "x": x_values, "__builtins__": {}})

        df = pd.DataFrame({"x": x_values, "y": y_values})

        fig = px.line(df, x="x", y="y", title=f"Grafik: y = {user_function}")
        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"❌ Funksiya bajarishda xatolik: {e}")
