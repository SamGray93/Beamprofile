
import streamlit as st
import math

st.set_page_config(layout="wide")
st.title("Echo Dynamics - Beam Analyser")

tab1, tab2 = st.tabs(["Circular Crystal", "Rectangular / Square Crystal"])

def calculate_incident_angle(material_velocity, probe_velocity, refracted_angle_deg):
    try:
        sin_incident = (probe_velocity * math.sin(math.radians(refracted_angle_deg))) / material_velocity
        if abs(sin_incident) > 1:
            return None
        angle_rad = math.asin(sin_incident)
        return round(math.degrees(angle_rad), 2)
    except Exception:
        return None

def rectangular_tab():
    st.markdown("### Input Parameters")
    col1, col2, col3 = st.columns(3)

    with col1:
        material_velocity = st.number_input("Material Velocity (m/s)", value=3200.0, key="r_mat_vel")
    with col2:
        probe_frequency = st.number_input("Probe Frequency (MHz)", value=4.0, key="r_probe_freq")
    with col3:
        probe_velocity = st.number_input("Probe Material Velocity (m/s)", value=6300.0, key="r_probe_vel")

    wavelength = material_velocity / (probe_frequency * 1e6)
    st.write(f"**Wavelength (mm):** {round(wavelength * 1000, 3)}")

    col4, col5 = st.columns(2)
    with col4:
        refracted_angle = st.number_input("Refracted Angle (°)", value=60.0, key="r_refracted_angle")
    with col5:
        incident_angle = calculate_incident_angle(material_velocity, probe_velocity, refracted_angle)
        if incident_angle is not None:
            st.write(f"**Incident Angle (°):** {incident_angle}")
        else:
            st.write("**Incident Angle (°):** Invalid (sin > 1)")

    st.markdown("### Crystal Properties & Near Zone")

    col6, col7 = st.columns(2)
    with col6:
        crystal_width = st.number_input("Crystal Width (mm)", value=10.0, key="r_crystal_width")
        crystal_length = st.number_input("Crystal Length (mm)", value=10.0, key="r_crystal_length")

        # Ratio and H-factor
        ratio = round(crystal_width / crystal_length, 1)
        h_factor_lookup = {
            1.0: 1.37, 0.9: 1.25, 0.8: 1.15, 0.7: 1.09, 0.6: 1.04,
            0.5: 1.01, 0.4: 1.00, 0.3: 0.99, 0.2: 0.99, 0.1: 0.99
        }
        h_factor = h_factor_lookup.get(ratio, 1.00)

        st.write(f"**Ratio (W/L):** {ratio}")
        st.write(f"**H Factor:** {h_factor}")

    with col7:
        near_zone = h_factor * (crystal_length**2) / (4 * (wavelength * 1000))
        st.number_input("Near Zone (mm)", value=round(near_zone, 2), disabled=True, key="r_nz")

    st.markdown("### Beam Spread Grid (150 mm × 150 mm)")
    st.markdown("🔲 Grid and beam plot will appear here in future steps.")

with tab1:
    st.markdown("### Circular Crystal Tab")
    st.markdown("This tab remains unchanged.")

with tab2:
    rectangular_tab()
