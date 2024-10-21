import streamlit as st

def calculate_coal_gcv(fixed_carbon, volatile_matter, total_moisture, inherent_moisture, ash_content, sulfur):
    fixed_carbon_factor = 8080  # kcal/kg
    volatile_matter_factor = 3450  # kcal/kg
    sulfur_factor = 2240  # kcal/kg
    ash_factor = 100  # kcal/kg

    dry_gcv = ((fixed_carbon / 100 * fixed_carbon_factor) +
               (volatile_matter / 100 * volatile_matter_factor) +
               (sulfur / 100 * sulfur_factor) -
               (ash_content / 100 * ash_factor))

    gcv_dry_basis = dry_gcv * (1 - inherent_moisture / 100)
    gcv = gcv_dry_basis * (1 - total_moisture / 100)

    return gcv


def calculate_biomass_gcv(fixed_carbon, volatile_matter, total_moisture, inherent_moisture, ash_content, sulfur):
    fixed_carbon_factor = 8000  # kcal/kg
    volatile_matter_factor = 4000  # kcal/kg
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


if __name__ == "__main__":
    main()
