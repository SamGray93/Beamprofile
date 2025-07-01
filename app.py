
import streamlit as st
import math

st.set_page_config(layout="wide")

st.title("Echo Dynamics - Beam Analyser")

tab1, tab2 = st.tabs(["Circular Crystal", "Rectangular / Square Crystal"])

with tab1:
    st.header("Circular Crystal Tab")

    col1, col2, col3 = st.columns(3)
    with col1:
        material_velocity = st.number_input("Material Velocity (m/s)", value=3200.0)
    with col2:
        probe_frequency = st.number_input("Probe Frequency (MHz)", value=4.0)
    with col3:
        probe_material_velocity = st.number_input("Probe Material Velocity (m/s)", value=6300.0)

    wavelength = material_velocity / (probe_frequency * 1e6) * 1000  # in mm
    st.markdown(f"**Wavelength (mm):** {wavelength:.2f}")

    col4, col5 = st.columns(2)
    with col4:
        refracted_angle_deg = st.number_input("Refracted Angle (°)", value=60.0)
    with col5:
        try:
            sin_incident = (probe_material_velocity * math.sin(math.radians(refracted_angle_deg))) / material_velocity
            if abs(sin_incident) > 1:
                st.markdown("**Incident Angle (°):** Invalid (sin > 1)")
            else:
                incident_angle_deg = math.degrees(math.asin(sin_incident))
                st.markdown(f"**Incident Angle (°):** {incident_angle_deg:.2f}")
        except:
            st.markdown("**Incident Angle (°):** Error")

with tab2:
    st.header("Rectangular / Square Crystal Tab")
    st.markdown("This tab is not part of this update.")
