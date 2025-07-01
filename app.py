
import streamlit as st
import math

st.set_page_config(layout="wide")
st.title("Echo Dynamics - Beam Analyser")

# Tabs for crystal type
tab1, tab2 = st.tabs(["Circular Crystal", "Rectangular / Square Crystal"])

# === CIRCULAR CRYSTAL TAB ===
with tab1:
    st.markdown("### Input Parameters")
    col1, col2, col3 = st.columns(3)

    with col1:
        material_velocity = st.number_input("Material Velocity (m/s)", value=3200.0, key="circ_mat_vel")
    with col2:
        probe_frequency = st.number_input("Probe Frequency (MHz)", value=4.0, key="circ_probe_freq")
    with col3:
        probe_material_velocity = st.number_input("Probe Material Velocity (m/s)", value=1490.0, key="circ_probe_mat_vel")

    col4, col5 = st.columns(2)
    with col4:
        refracted_angle = st.number_input("Refracted Angle (°)", value=60.0, key="circ_refracted_angle")
    with col5:
        try:
            incident_angle_rad = math.asin((probe_material_velocity / material_velocity) * math.sin(math.radians(refracted_angle)))
            incident_angle = round(math.degrees(incident_angle_rad), 2)
            st.markdown(f"**Incident Angle (°):** {incident_angle}")
        except:
            st.markdown("**Incident Angle (°):** Invalid (sin > 1)")

    # Wavelength
    try:
        wavelength = round(material_velocity / (probe_frequency * 1e6) * 1000, 3)
        st.markdown(f"**Wavelength (mm):** {wavelength}")
    except:
        st.markdown("**Wavelength (mm):** Error")

    # Crystal diameter and Near Zone
    st.markdown("### Crystal Properties & Near Zone")
    crystal_diameter = st.number_input("Crystal Diameter (mm)", value=10.0, key="circ_diameter")
    try:
        near_zone = round((crystal_diameter ** 2) / (4 * wavelength), 2)
        st.markdown(f"**Near Zone (mm):** {near_zone}")
    except:
        st.markdown("**Near Zone (mm):** Error")

    st.markdown("### Beam Spread Grid (150 mm × 150 mm)")
    st.markdown("🟦 Grid and beam plot will appear here in future steps.")

# === RECTANGULAR CRYSTAL TAB ===
with tab2:
    st.markdown("### Input Parameters")
    col1, col2, col3 = st.columns(3)

    with col1:
        material_velocity = st.number_input("Material Velocity (m/s)", value=3200.0, key="rect_mat_vel")
    with col2:
        probe_frequency = st.number_input("Probe Frequency (MHz)", value=4.0, key="rect_probe_freq")
    with col3:
        probe_material_velocity = st.number_input("Probe Material Velocity (m/s)", value=1490.0, key="rect_probe_mat_vel")

    col4, col5 = st.columns(2)
    with col4:
        refracted_angle = st.number_input("Refracted Angle (°)", value=60.0, key="rect_refracted_angle")
    with col5:
        try:
            incident_angle_rad = math.asin((probe_material_velocity / material_velocity) * math.sin(math.radians(refracted_angle)))
            incident_angle = round(math.degrees(incident_angle_rad), 2)
            st.markdown(f"**Incident Angle (°):** {incident_angle}")
        except:
            st.markdown("**Incident Angle (°):** Invalid (sin > 1)")

    # Wavelength
    try:
        wavelength = round(material_velocity / (probe_frequency * 1e6) * 1000, 3)
        st.markdown(f"**Wavelength (mm):** {wavelength}")
    except:
        st.markdown("**Wavelength (mm):** Error")

    st.markdown("### Crystal Properties & Near Zone")
    col6, col7 = st.columns(2)
    with col6:
        width = st.number_input("Crystal Width (mm)", value=10.0, key="rect_width")
    with col7:
        length = st.number_input("Crystal Length (mm)", value=20.0, key="rect_length")

    try:
        ratio = round(width / length, 1)
        h_lookup = {
            1.0: 1.37,
            0.9: 1.25,
            0.8: 1.15,
            0.7: 1.09,
            0.6: 1.04,
            0.5: 1.01,
            0.4: 1.00,
            0.3: 0.99,
            0.2: 0.99,
            0.1: 0.99
        }
        h_factor = h_lookup.get(ratio, 1.0)
        st.markdown(f"**Width/Length Ratio:** {ratio}")
        st.markdown(f"**H Factor:** {h_factor}")
        near_zone = round(h_factor * ((length ** 2) / (4 * wavelength)), 2)
        st.markdown(f"**Near Zone (mm):** {near_zone}")
    except:
        st.markdown("**Near Zone (mm):** Error")

    st.markdown("### Beam Spread Grid (150 mm × 150 mm)")
    st.markdown("🟦 Grid and beam plot will appear here in future steps.")
