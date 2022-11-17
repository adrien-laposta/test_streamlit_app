import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("**First application build using `streamlit`**")
#st.markdown("# **First application build using `streamlit`**")

pow = st.sidebar.slider("Select the power", min_value=0, max_value=10, step=1)
xmin, xmax = st.sidebar.slider(r"Select a range of x", -10., 10., (-5., 5.), step = 0.5)
color = st.sidebar.color_picker("Color picker", value = "#000000")


funcs = {"power": lambda x: x ** pow,
         "sin": lambda x: np.sin(x) ** pow}

func_labels = {"power": r"$y = x^{{{}}}$",
               "sin": r"$y = sin^{{{}}}(x)$"}

displayed = st.sidebar.multiselect("Select the functions to display",  sorted(list(func_labels.keys())), sorted(list(func_labels.keys())))
displayed.sort()

cols = st.columns(len(displayed))
cols = {func_type: cols[i] for i, func_type in enumerate(displayed)}

print(displayed)

if xmax <= xmin:
    st.markdown("$x_{min}$ must be lower than $x_{max}$")
else:
    for i, (func_type, col) in enumerate(cols.items()):
        with col:
            fig = plt.figure()
            x = np.linspace(xmin, xmax, 100)
            y = funcs[func_type](x)

            plt.plot(x, y, color = color)
            plt.xlabel(r"$x$")
            plt.ylabel(func_labels[func_type].format(pow))
            plt.tight_layout()

            #st.plotly_chart(fig)
            st.pyplot(fig)
