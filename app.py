import streamlit as st

def calculate_coal_gcv(fixed_carbon, volatile_matter, total_moisture, inherent_moisture, ash_content, sulfur):
    fixed_carbon_factor = 9900  # kcal/kg
    volatile_matter_factor = 3550  # kcal/kg
    sulfur_factor = 2400  # kcal/kg
    ash_factor = 100  # kcal/kg

    dry_gcv = ((fixed_carbon / 100 * fixed_carbon_factor) +
               (volatile_matter / 100 * volatile_matter_factor) +
               (sulfur / 100 * sulfur_factor) -
               (ash_content / 100 * ash_factor))

    gcv_dry_basis = dry_gcv * (1 - inherent_moisture / 100)
    gcv = gcv_dry_basis * (1 - total_moisture / 100)

    return gcv

def calculate_biomass_gcv(fixed_carbon, volatile_matter, total_moisture, inherent_moisture, ash_content, sulfur):
    fixed_carbon_factor = 7500  # kcal/kg
    volatile_matter_factor = 3500  # kcal/kg
    sulfur_factor = 2000  # kcal/kg
    ash_factor = 100  # kcal/kg

    dry_gcv = ((fixed_carbon / 100 * fixed_carbon_factor) +
               (volatile_matter / 100 * volatile_matter_factor) +
               (sulfur / 100 * sulfur_factor) -
               (ash_content / 100 * ash_factor))

    gcv_dry_basis = dry_gcv * (1 - inherent_moisture / 100)
    gcv_total_adjusted = gcv_dry_basis * (1 - total_moisture / 100)

    return gcv_total_adjusted

def main():
    st.title("GCV Calculator for Coal and Biomass")

    # Add some styling
    st.markdown(
        """
        <style>
        .main {
            background-color: #f0f0f0;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
        }
        .footer {
            font-size: 14px;
            color: gray;
        }
        </style>
        """, unsafe_allow_html=True
    )

    fuel_type = st.selectbox("Select the type of fuel:", ("Coal", "Biomass"))

    fixed_carbon = st.number_input("Fixed Carbon (%)", min_value=0.0, max_value=100.0)
    volatile_matter = st.number_input("Volatile Matter (%)", min_value=0.0, max_value=100.0)
    total_moisture = st.number_input("Total Moisture (%)", min_value=0.0, max_value=100.0)
    inherent_moisture = st.number_input("Inherent Moisture (%)", min_value=0.0, max_value=100.0)
    ash_content = st.number_input("Ash Content (%)", min_value=0.0, max_value=100.0)
    sulfur = st.number_input("Sulfur (%)", min_value=0.0, max_value=100.0)

    if st.button("Calculate GCV"):
        if fuel_type == "Coal":
            gcv = calculate_coal_gcv(fixed_carbon, volatile_matter, total_moisture, inherent_moisture, ash_content, sulfur)
            st.success(f"The Gross Calorific Value (GCV) of coal is: {gcv:.2f} kcal/kg")
        elif fuel_type == "Biomass":
            gcv = calculate_biomass_gcv(fixed_carbon, volatile_matter, total_moisture, inherent_moisture, ash_content, sulfur)
            st.success(f"The Gross Calorific Value (GCV) of biomass is: {gcv:.2f} kcal/kg")

    # Add a "Developed by" section
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<div class='footer'>Developed by mak3.5</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
