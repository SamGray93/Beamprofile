
import streamlit as st
import math

st.set_page_config(layout="wide")
st.title("Echo Dynamics - Beam Analyser")

# Tabs for crystal type
tab1, tab2 = st.tabs(["Circular Crystal", "Rectangular / Square Crystal"])

def show_inputs(tab_name):
    with tab_name:
        st.markdown("### Input Parameters")
        col1, col2, col3 = st.columns(3)

        with col1:
            material_velocity = st.number_input("Material Velocity (m/s)", value=3200)
        with col2:
            probe_frequency = st.number_input("Probe Frequency (MHz)", value=4.0)
        with col3:
            wavelength = material_velocity / (probe_frequency * 1e6)
            st.number_input("Wavelength (mm)", value=round(wavelength * 1000, 4), disabled=True)

        st.markdown("### Beam Angles")
        col4, col5 = st.columns(2)

        with col4:
            refracted_angle = st.number_input("Refracted Angle (°)", value=60.0)
        with col5:
            try:
                incident_angle_rad = math.asin((material_velocity / material_velocity) * math.sin(math.radians(refracted_angle)))
                incident_angle = math.degrees(incident_angle_rad)
            except:
                incident_angle = 0.0
            st.number_input("Incident Angle (°)", value=round(incident_angle, 2), disabled=True)

        st.markdown("---")

show_inputs(tab1)
show_inputs(tab2)

# Placeholder for beam grid
st.markdown("### Beam Spread Grid (150 mm × 150 mm)")
st.image("grid_placeholder.png", caption="Scaled grid preview", use_column_width=True)
