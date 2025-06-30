
import streamlit as st
import math

st.set_page_config(layout="wide")
st.title("Echo Dynamics - Beam Analyser")

# Tabs for crystal type
tab1, tab2 = st.tabs(["Circular Crystal", "Rectangular / Square Crystal"])

def show_inputs(tab):
    with tab:
        st.markdown("### Input Parameters")
        col1, col2, col3 = st.columns(3)

        with col1:
            material_velocity = st.number_input("Material Velocity (m/s)", value=3200.0, key=f"mat_vel_{tab}")
        with col2:
            probe_frequency = st.number_input("Probe Frequency (MHz)", value=4.0, key=f"probe_freq_{tab}")
        with col3:
            wavelength = material_velocity / (probe_frequency * 1e6)
            st.number_input("Wavelength (mm)", value=round(wavelength * 1000, 4), disabled=True, key=f"wavelength_{tab}")

        col4, col5, col6 = st.columns(3)

        with col4:
            probe_velocity = st.number_input("Probe Material Velocity (m/s)", value=1490.0, key=f"probe_vel_{tab}")
        with col5:
            refracted_angle = st.number_input("Refracted Angle (°)", value=60.0, key=f"refracted_angle_{tab}")
        with col6:
            try:
                numerator = probe_velocity * math.sin(math.radians(refracted_angle))
                denominator = material_velocity
                if abs(numerator / denominator) <= 1:
                    incident_rad = math.asin(numerator / denominator)
                    incident_angle = math.degrees(incident_rad)
                    st.number_input("Incident Angle (°)", value=round(incident_angle, 2), disabled=True, key=f"incident_{tab}")
                else:
                    st.write("**Incident Angle (°)**: Invalid (sin > 1)")
            except:
                st.write("**Incident Angle (°)**: Calculation Error")

        col7, col8 = st.columns(2)

        with col7:
            crystal_diameter = st.number_input("Crystal Diameter D (mm)", value=10.0, key=f"crystal_d_{tab}")
        with col8:
            try:
                near_zone = (crystal_diameter ** 2) / (4 * (wavelength * 1000))
                st.number_input("Near Zone (mm)", value=round(near_zone, 2), disabled=True, key=f"nz_{tab}")
            except:
                st.write("**Near Zone**: Error")

        st.markdown("---")
        st.markdown("### Beam Spread Grid (150 mm × 150 mm)")
        st.write("🟦 Grid and beam plot will appear here in future steps.")

# Render both tab contents
show_inputs(tab1)
show_inputs(tab2)
