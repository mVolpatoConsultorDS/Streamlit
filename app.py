import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    os.system('clear')
    st.title("Line Plot Example")
    data = pd.DataFrame({
    "x": [1, 2, 3, 4],                # Load sample data
    "y": [10, 20, 30, 40]})
    plt.plot(data["x"], data["y"])         # Plot the data
    st.pyplot()                            # Show the plot in the Streamlit app

    num_points = st.slider("Number of points", min_value=100, max_value=1000, value=500, step=100)
    text_input = st.text_input("Enter some text:")
    st.write("The name :", text_input)
    show_plot = st.checkbox("Show plot", value=True)
    if not show_plot:
        plt.close()
    plot_color = st.selectbox("Plot color", ["blue", "red", "green"])
    plt.plot(data["x"], data["y"], color=plot_color)
    st.camera_input("Take a picture")
    #st.progress(progress_variable_1_to_100)

    
if __name__ == '__main__':
    main()