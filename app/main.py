"""
Entry point for the precision health platform prototype.

Status: placeholder only. No calculation logic exists yet (Phase 2 has not
started). This file exists so the project runs end-to-end and can be
committed as a clean, working checkpoint.
"""

import streamlit as st

st.set_page_config(page_title="Precision Health Platform (prototype)")

st.title("Explainable Multi-Domain Precision Health Platform")
st.caption("Research prototype — not a diagnostic tool. See README.md for scope and limitations.")

st.write(
    "This is an early scaffold. Domain modules (obesity, mental well-being, "
    "type 2 diabetes, cardiovascular risk), the shared-factor engine, and the "
    "what-if simulator are not implemented yet — see ROADMAP.md and "
    "PROJECT_STATUS.md for current progress."
)
