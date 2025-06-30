
import streamlit as st
import math

st.set_page_config(layout="wide")

# Tabs for crystal type
tab1, tab2 = st.tabs(["Circular Crystal", "Rectangular / Square Crystal"])

def calculate_wavelength(velocity, frequency):
    try:
        return round(velocity / (frequency * 1e6) * 1000, 3)
    except:
        return ""

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        velocity = st.number_input("Material Velocity (m/s)", key="circ_vel")
        frequency = st.number_input("Probe Frequency (MHz)", key="circ_freq")
    with col2:
        wavelength = calculate_wavelength(velocity, frequency)
        st.text_input("Wavelength (mm)", value=wavelength, disabled=True)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        velocity = st.number_input("Material Velocity (m/s)", key="rect_vel")
        frequency = st.number_input("Probe Frequency (MHz)", key="rect_freq")
        probe_velocity = st.number_input("Probe Material Velocity (m/s)", key="probe_vel")
        refracted_angle = st.number_input("Refracted Angle (°)", key="refr_angle")
        length = st.number_input("Crystal Length (mm)", key="cryst_len")
        width = st.number_input("Crystal Width (mm)", key="cryst_wid")
    with col2:
        wavelength = calculate_wavelength(velocity, frequency)
        st.text_input("Wavelength (mm)", value=wavelength, disabled=True)
        try:
            incident_angle = math.degrees(math.asin((probe_velocity * math.sin(math.radians(refracted_angle))) / velocity))
            st.text_input("Incident Angle (°)", value=round(incident_angle, 2), disabled=True)
        except:
            st.text_input("Incident Angle (°)", value="", disabled=True)

        try:
            ratio = width / length
            h_factor = round(1 + 1.6 * (ratio ** 2), 2)
            st.text_input("Width / Length Ratio", value=round(ratio, 2), disabled=True)
            st.text_input("H-Factor", value=h_factor, disabled=True)
            near_zone = round((length ** 2) / (4 * wavelength) * h_factor, 1)
            st.text_input("Near Zone Length (mm)", value=near_zone, disabled=True)
        except:
            st.text_input("Width / Length Ratio", value="", disabled=True)
            st.text_input("H-Factor", value="", disabled=True)
            st.text_input("Near Zone Length (mm)", value="", disabled=True)
