
import streamlit as st
import math

st.set_page_config(layout="wide")
st.title("Echo Dynamics - Beam Analyser")

tab1, tab2 = st.tabs(["Circular Crystal", "Rectangular / Square Crystal"])

def show_circular_tab():
    st.markdown("### Input Parameters")
    col1, col2, col3 = st.columns(3)
    with col1:
        material_velocity = st.number_input("Material Velocity (m/s)", value=3200.0, key="circ_mat_vel")
    with col2:
        probe_frequency = st.number_input("Probe Frequency (MHz)", value=4.0, key="circ_probe_freq")
    with col3:
        wavelength = material_velocity / (probe_frequency * 1e6)
        st.number_input("Wavelength (mm)", value=round(wavelength * 1000, 3), disabled=True, key="circ_wavelength")

    col4, col5 = st.columns(2)
    with col4:
        probe_material_velocity = st.number_input("Probe Material Velocity (m/s)", value=6300.0, key="circ_probe_mat_vel")
    with col5:
        refracted_angle = st.number_input("Refracted Angle (°)", value=60.0, key="circ_refracted_angle")

    try:
        sin_val = (probe_material_velocity * math.sin(math.radians(refracted_angle))) / material_velocity
        if abs(sin_val) <= 1:
            incident_angle = math.degrees(math.asin(sin_val))
            st.number_input("Incident Angle (°)", value=round(incident_angle, 2), disabled=True, key="circ_incident_angle")
        else:
            st.write("**Incident Angle (°): Invalid (sin > 1)**")
    except:
        st.write("**Incident Angle (°): Error in calculation**")

def show_rectangular_tab():
    st.markdown("### Input Parameters")
    col1, col2, col3 = st.columns(3)
    with col1:
        material_velocity = st.number_input("Material Velocity (m/s)", value=3200.0, key="rect_mat_vel")
    with col2:
        probe_frequency = st.number_input("Probe Frequency (MHz)", value=4.0, key="rect_probe_freq")
    with col3:
        wavelength = material_velocity / (probe_frequency * 1e6)
        st.number_input("Wavelength (mm)", value=round(wavelength * 1000, 3), disabled=True, key="rect_wavelength")

    col4, col5 = st.columns(2)
    with col4:
        probe_material_velocity = st.number_input("Probe Material Velocity (m/s)", value=6300.0, key="rect_probe_mat_vel")
    with col5:
        refracted_angle = st.number_input("Refracted Angle (°)", value=60.0, key="rect_refracted_angle")

    try:
        sin_val = (probe_material_velocity * math.sin(math.radians(refracted_angle))) / material_velocity
        if abs(sin_val) <= 1:
            incident_angle = math.degrees(math.asin(sin_val))
            st.number_input("Incident Angle (°)", value=round(incident_angle, 2), disabled=True, key="rect_incident_angle")
        else:
            st.write("**Incident Angle (°): Invalid (sin > 1)**")
    except:
        st.write("**Incident Angle (°): Error in calculation**")

    st.markdown("### Crystal Properties & Near Zone")
    col6, col7 = st.columns(2)
    with col6:
        crystal_width = st.number_input("Crystal Width (mm)", value=10.0, key="rect_crystal_width")
        crystal_length = st.number_input("Crystal Length (mm)", value=10.0, key="rect_crystal_length")

    ratio = round(crystal_width / crystal_length, 1) if crystal_length != 0 else 0.0
    h_factor_lookup = {
        1.0: 1.37, 0.9: 1.25, 0.8: 1.15, 0.7: 1.09,
        0.6: 1.04, 0.5: 1.01, 0.4: 1.00, 0.3: 0.99,
        0.2: 0.99, 0.1: 0.99
    }
    h_factor = h_factor_lookup.get(ratio, 1.00)

    near_zone = (h_factor * ((crystal_length ** 2) / (4 * (wavelength * 1000)))) if wavelength > 0 else 0

    st.write(f"**Rounded Ratio (Width / Length)**: {ratio}")
    st.write(f"**H Factor**: {h_factor}")
    st.write(f"**Near Zone (mm)**: {round(near_zone, 2)}")

with tab1:
    show_circular_tab()

with tab2:
    show_rectangular_tab()

st.markdown("### Beam Spread Grid (150 mm × 150 mm)")
st.write("⬛ Grid and beam plot will appear here in future steps.")
