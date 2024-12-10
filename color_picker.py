import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to update the image based on slider values
def update_image(r, g, b, switch_on):
    img = np.zeros((300, 513, 3), np.uint8)
    if switch_on:
        img[:] = [r, g, b]  # Set RGB values (BGR in OpenCV, but RGB for this code)
    return img

# Streamlit app
st.title("Color Picker")

# Add a switch to toggle color on or off
st.text("Check to get Color")
switch = st.checkbox("Enable Color", value=True)

# Create sliders for R, G, B
r = st.slider("Red", 0, 255, 0)
g = st.slider("Green", 0, 255, 0)
b = st.slider("Blue", 0, 255, 0)

# Update image based on sliders and switch
img = update_image(r, g, b, switch)

# Display image using Matplotlib
fig, ax = plt.subplots()
ax.imshow(img)
ax.axis('off')  # Hide axes for better visualization
st.pyplot(fig)
output = f"**RGB Values (r, g, b)**:  `({r}, {g}, {b})`"
st.markdown(output)
