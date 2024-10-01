import streamlit as st
from components import home, art_module, counterfit_module, pyrit_module, results, model_scan_module

# Configure the main page
st.set_page_config(page_title="AI Red Teaming Platform", layout="wide")

# Sidebar for navigation
st.sidebar.title("AI Red Teaming Navigation")
page = st.sidebar.radio(
    "Go to", ["Home", "Adversarial Robustness Toolbox (ART)", "Counterfit", "PyRIT", "Results & Reports", "Model Scan"]
)

# Main section switching
if page == "Home":
    home.display_home()
elif page == "Adversarial Robustness Toolbox (ART)":
    art_module.display_art_section()
elif page == "Counterfit":
    counterfit_module.display_counterfit_section()
elif page == "PyRIT":
    pyrit_module.display_pyrit_section()

elif page == "Model Scan":
    model_scan_module.display_model_scan_section()

elif page == "Results & Reports":
    results.display_results_section()
