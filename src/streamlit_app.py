import streamlit as st
import streamlit.components.v1 as components
from src.tabs import demo_tab, examples_tab, about_tab

# Title of the app
st.title("ABC Notation Renderer")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Demo", "Examples", "About"])

with tab1:
    demo_tab.render()

with tab2:
    examples_tab.render()

with tab3:
    about_tab.render()