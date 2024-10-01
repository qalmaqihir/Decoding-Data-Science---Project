import streamlit as st
from components import home, art_module, counterfit_module, pyrit_module, results

def display_home():
    st.title("Welcome to the AI Red Teaming Platform")
    st.markdown(
        """
        This platform allows you to test your AI models for vulnerabilities using state-of-the-art tools:
        - **Adversarial Robustness Toolbox (ART)** for adversarial attack simulations.
        - **Counterfit** for attack surface exploration.
        - **PyRIT** for risk identification and compliance evaluation.

        Navigate through the sidebar to start testing and evaluating your AI models.
        """
    )

    # Quick Start Section
    st.subheader("Quick Start")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("Run ART Test")    

    with col2:
        st.button("Run Counterfit Test")
     
    with col3:
        st.button("Run PyRIT Analysis")

    # Display recent activity
    st.subheader("Recent Activity")
    st.markdown("No recent activities to display.")
