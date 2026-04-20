import streamlit as st

from data_loader import load_claims
from pages import (
    render_claim_detail,
    render_command_center,
    render_priority_queue,
)
from ui_helpers import apply_css, apply_sidebar_filters

st.set_page_config(
    page_title="Healthcare Claims Operations Platform",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_css()

df = load_claims()

st.sidebar.markdown(
    """
    <div class="sidebar-brand">
        <div class="sidebar-brand__mark">🏥</div>
        <div class="sidebar-brand__title">Claims Operations</div>
        <div class="sidebar-brand__tag">Revenue cycle · Denial triage · Live portfolio view</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown('<p class="sidebar-nav-label">Navigate</p>', unsafe_allow_html=True)
page = st.sidebar.radio(
    "Navigation",
    ["Command Center", "Priority Queue", "Claim Detail"],
    label_visibility="collapsed",
)

filtered_df = apply_sidebar_filters(df)

if "selected_claim_id" not in st.session_state:
    st.session_state.selected_claim_id = (
        str(filtered_df.iloc[0]["claim_id"]) if not filtered_df.empty else None
    )

if page == "Command Center":
    render_command_center(filtered_df)
elif page == "Priority Queue":
    render_priority_queue(filtered_df)
else:
    render_claim_detail(filtered_df)
