
import streamlit as st
import math

st.set_page_config(layout="wide")

# Title
st.title("Echo Dynamics - Beam Analyser")

# Tabs for probe type
probe_type = st.radio("Select Probe Type", ["Circular Crystal", "Rectangular / Square Crystal"], horizontal=True)

# Shared input fields
col1, col2, col3 = st.columns(3)
with col1:
    material_velocity = st.number_input("Material Velocity (m/s)", min_value=1.0, value=3200.0)
with col2:
    probe_frequency = st.number_input("Probe Frequency (MHz)", min_value=0.1, value=4.0)
with col3:
    wavelength = material_velocity / (probe_frequency * 1_000_000)
    st.markdown(f"**Wavelength (mm):** {wavelength:.3f}")

# Additional inputs
col4, col5, col6 = st.columns(3)
with col4:
    probe_velocity = st.number_input("Probe Material Velocity (m/s)", min_value=1.0, value=6300.0)
with col5:
    refracted_angle_deg = st.number_input("Refracted Angle (°)", min_value=0.0, max_value=90.0, value=60.0)
with col6:
    try:
        refracted_angle_rad = math.radians(refracted_angle_deg)
        sin_incident = (probe_velocity * math.sin(refracted_angle_rad)) / material_velocity
        if abs(sin_incident) <= 1:
            incident_angle_rad = math.asin(sin_incident)
            incident_angle_deg = math.degrees(incident_angle_rad)
            st.markdown(f"**Incident Angle (°):** {incident_angle_deg:.2f}")
        else:
            st.markdown("**Incident Angle (°):** Invalid (sin > 1)")
    except:
        st.markdown("**Incident Angle (°):** Error")

# Grid display placeholder
st.markdown("---")
st.markdown("🟦 **Grid and beam plot will appear here in future steps.**")
