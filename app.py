
import streamlit as st
import matplotlib.pyplot as plt
import math

st.set_page_config(layout="wide")
st.title("Echo Dynamics - Beam Analyser")

tab1, tab2 = st.tabs(["Circular Crystal", "Rectangular / Square Crystal"])

with tab1:
    col1, col2, col3 = st.columns(3)
    with col1:
        material_velocity = st.number_input("Material Velocity (m/s)", value=3200.0, key="c_mat_vel")
    with col2:
        probe_frequency = st.number_input("Probe Frequency (MHz)", value=4.0, key="c_freq")
    with col3:
        probe_material_velocity = st.number_input("Probe Material Velocity (m/s)", value=6300.0, key="c_probe_vel")

    wavelength = material_velocity / (probe_frequency * 1e6) * 1000  # mm
    st.markdown(f"**Wavelength (mm):** {wavelength:.2f}")

    col4, col5 = st.columns(2)
    with col4:
        refracted_angle_deg = st.number_input("Refracted Angle (°)", value=60.0, key="c_refrac")
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

    st.markdown("### Crystal Properties & Near Zone")
    crystal_diameter = st.number_input("Crystal Diameter (mm)", value=10.0, key="c_diameter")
    near_zone = (crystal_diameter ** 2) / (4 * wavelength)
    st.markdown(f"**Near Zone (mm):** {near_zone:.2f}")

    st.markdown("### Beam Grid (150 mm × 150 mm)")
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, 150)
    ax.set_ylim(0, 150)
    ax.set_xticks(range(0, 160, 10))
    ax.set_yticks(range(0, 160, 10))
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.set_aspect('equal')
    ax.invert_yaxis()
    ax.set_xlabel("mm")
    ax.set_ylabel("mm")
    st.pyplot(fig)

with tab2:
    col1, col2, col3 = st.columns(3)
    with col1:
        r_material_velocity = st.number_input("Material Velocity (m/s)", value=3200.0, key="r_mat_vel")
    with col2:
        r_probe_frequency = st.number_input("Probe Frequency (MHz)", value=4.0, key="r_freq")
    with col3:
        r_probe_material_velocity = st.number_input("Probe Material Velocity (m/s)", value=6300.0, key="r_probe_vel")

    r_wavelength = r_material_velocity / (r_probe_frequency * 1e6) * 1000  # mm
    st.markdown(f"**Wavelength (mm):** {r_wavelength:.2f}")

    col4, col5 = st.columns(2)
    with col4:
        r_refracted_angle = st.number_input("Refracted Angle (°)", value=60.0, key="r_refrac")
    with col5:
        try:
            r_sin_incident = (r_probe_material_velocity * math.sin(math.radians(r_refracted_angle))) / r_material_velocity
            if abs(r_sin_incident) > 1:
                st.markdown("**Incident Angle (°):** Invalid (sin > 1)")
            else:
                r_incident_angle = math.degrees(math.asin(r_sin_incident))
                st.markdown(f"**Incident Angle (°):** {r_incident_angle:.2f}")
        except:
            st.markdown("**Incident Angle (°):** Error")

    st.markdown("### Crystal Properties & Near Zone")
    col6, col7 = st.columns(2)
    with col6:
        crystal_width = st.number_input("Crystal Width (mm)", value=10.0)
    with col7:
        crystal_length = st.number_input("Crystal Length (mm)", value=10.0)

    ratio = round(crystal_width / crystal_length, 2) if crystal_length != 0 else 0
    st.markdown(f"**Ratio (W/L):** {ratio}")

    # H-factor estimation
    if ratio <= 0.3:
        h_factor = 1.00
    elif 0.31 <= ratio <= 0.5:
        h_factor = 1.10
    elif 0.51 <= ratio <= 0.7:
        h_factor = 1.23
    elif 0.71 <= ratio <= 0.9:
        h_factor = 1.30
    elif 0.91 <= ratio <= 1.1:
        h_factor = 1.37
    else:
        h_factor = 1.50

    st.markdown(f"**H Factor:** {h_factor}")

    near_zone_rect = (crystal_length ** 2) / (4 * r_wavelength * h_factor)
    st.markdown(f"**Near Zone (mm):** {near_zone_rect:.2f}")

    st.markdown("### Beam Grid (150 mm × 150 mm)")
    fig2, ax2 = plt.subplots(figsize=(6, 6))
    ax2.set_xlim(0, 150)
    ax2.set_ylim(0, 150)
    ax2.set_xticks(range(0, 160, 10))
    ax2.set_yticks(range(0, 160, 10))
    ax2.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax2.set_aspect('equal')
    ax2.invert_yaxis()
    ax2.set_xlabel("mm")
    ax2.set_ylabel("mm")
    st.pyplot(fig2)
