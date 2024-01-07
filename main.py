import streamlit as st

def main():


    # Add a heading for the master timetable
    st.header("MASTER TIMETABLE MECH WALO K LIYE")

    # Dropdown menu options
    options = ["SOLAR + COMPOSITE", "ROBOTICS + CFD", "GAS + COMPOSITE", "GAS + FEM", "SOLAR + FEM"]

    # Dropdown menu to select options
    selected_option = st.selectbox("Select an option", options)

    # Dictionary containing image URLs or paths
    image_urls = {
        "SOLAR + COMPOSITE": "IMAGES/Screenshot_20240107_230030.png",
        "ROBOTICS + CFD": "IMAGES/Screenshot_20240107_230703.png",
        "GAS + COMPOSITE": "IMAGES/Screenshot_20240107_231030.png",
        "GAS + FEM": "IMAGES/Screenshot_20240107_231234.png",
        "SOLAR + FEM": "IMAGES/Screenshot_20240107_231354.png",
    }

    # Display the selected image
    st.image(image_urls[selected_option], caption=f"Selected Option: {selected_option}", use_column_width=True)










    
    st.markdown("<p style='color: red;'>Note : G3 lab is on Tuesday And G2 on Wednesday.Will update Tomorrow</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
