
import streamlit as st
import math

st.set_page_config(layout="wide")
st.title("Echo Dynamics - Beam Analyser")

# Tabs for probe types
tab1, tab2 = st.tabs(["Circular Crystal", "Rectangular / Square Crystal"])

def show_inputs(tab_name, tab_key):
    with tab_name:
        st.markdown("### Input Parameters")
        col1, col2, col3 = st.columns(3)

        with col1:
            material_velocity = st.number_input("Material Velocity (m/s)", value=3200.0, key=f"mat_vel_{tab_key}")
        with col2:
            probe_frequency = st.number_input("Probe Frequency (MHz)", value=4.0, key=f"probe_freq_{tab_key}")
        with col3:
            wavelength = material_velocity / (probe_frequency * 1e6)
            st.number_input("Wavelength (mm)", value=round(wavelength * 1000, 3), disabled=True, key=f"wavelength_{tab_key}")

        col4, col5, col6 = st.columns(3)
        with col4:
            probe_material_velocity = st.number_input("Probe Material Velocity (m/s)", value=1490.0, key=f"probe_mat_vel_{tab_key}")
        with col5:
            refracted_angle = st.number_input("Refracted Angle (°)", value=60.0, key=f"refracted_angle_{tab_key}")
        with col6:
            try:
                sin_incident = (probe_material_velocity * math.sin(math.radians(refracted_angle))) / material_velocity
                if abs(sin_incident) > 1:
                    raise ValueError
                incident_angle = math.degrees(math.asin(sin_incident))
                st.number_input("Incident Angle (°)", value=round(incident_angle, 2), disabled=True, key=f"incident_angle_{tab_key}")
            except:
                st.write("Incident Angle (°): Invalid (sin > 1)")

        col7, col8 = st.columns(2)
        with col7:
            crystal_diameter = st.number_input("Crystal Diameter D (mm)", value=10.0, key=f"crystal_diameter_{tab_key}")
        with col8:
            try:
                nz = (crystal_diameter ** 2) / (4 * (wavelength * 1000))
                st.number_input("Near Zone (mm)", value=round(nz, 2), disabled=True, key=f"near_zone_{tab_key}")
            except:
                st.write("Near Zone: Error")

        st.markdown("---")
        st.markdown("### Beam Spread Grid (150 mm × 150 mm)")
        st.markdown("⬛ Grid and beam plot will appear here in future steps.")

show_inputs(tab1, "circular")
show_inputs(tab2, "rectangular")
