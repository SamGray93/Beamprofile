
import streamlit as st
import math

st.set_page_config(layout="wide")
st.title("Echo Dynamics - Beam Analyser")

# Tab layout for probe type
tab1, tab2 = st.tabs(["Circular Crystal", "Rectangular / Square Crystal"])

def render_tab(tab_key):
    st.markdown("### Input Parameters")
    col1, col2, col3 = st.columns(3)

    with col1:
        material_velocity = st.number_input("Material Velocity (m/s)", value=3200.0, key=f"mat_vel_{tab_key}")
    with col2:
        probe_frequency = st.number_input("Probe Frequency (MHz)", value=4.0, key=f"probe_freq_{tab_key}")
    with col3:
        try:
            wavelength = material_velocity / (probe_frequency * 1e6)
        except ZeroDivisionError:
            wavelength = 0
        st.number_input("Wavelength (mm)", value=round(wavelength * 1000, 3), disabled=True, key=f"wavelength_{tab_key}")

    col4, col5, col6 = st.columns(3)
    with col4:
        probe_velocity = st.number_input("Probe Material Velocity (m/s)", value=6300.0, key=f"probe_vel_{tab_key}")
    with col5:
        refracted_angle_deg = st.number_input("Refracted Angle (°)", value=60.0, key=f"refracted_angle_{tab_key}")
    with col6:
        try:
            refracted_angle_rad = math.radians(refracted_angle_deg)
            sin_incident = (probe_velocity * math.sin(refracted_angle_rad)) / material_velocity
            if abs(sin_incident) <= 1:
                incident_angle_rad = math.asin(sin_incident)
                incident_angle = round(math.degrees(incident_angle_rad), 2)
                st.number_input("Incident Angle (°)", value=incident_angle, disabled=True, key=f"incident_angle_{tab_key}")
            else:
                st.markdown("**Incident Angle (°)**: Invalid (sin > 1)")
                incident_angle = None
        except Exception:
            st.markdown("**Incident Angle (°)**: Error")
            incident_angle = None

    st.markdown("### Crystal Properties & Near Zone")
    col7, col8 = st.columns(2)
    with col7:
        crystal_diameter = st.number_input("Crystal Diameter (mm)", value=10.0, key=f"crystal_d_{tab_key}")
    with col8:
        try:
            nz = (crystal_diameter ** 2) / (4 * (wavelength * 1000)) if wavelength > 0 else 0
            st.number_input("Near Zone (mm)", value=round(nz, 2), disabled=True, key=f"nz_{tab_key}")
        except Exception:
            st.markdown("**Near Zone**: Error")

    st.markdown("### Beam Spread Grid (150 mm × 150 mm)")
    st.markdown("⬛ Grid and beam plot will appear here in future steps.")

with tab1:
    render_tab("circular")

with tab2:
    render_tab("rectangular")
