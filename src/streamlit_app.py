"""
@moduleName: streamlit_app
@version: 1.0
@since: 10-03-2023
@lastUpdated: 10-03-2023
@completionTag: TO_DO

@projectSummary: 
 This module is the main entry point for the ABC Notation Renderer app.

@techStack: Python, Streamlit

@dependency: streamlit

@interModuleDependency: 
 - demo_tab: Utilized for rendering the Demo section.
 - examples_tab: Utilized for rendering the Examples section.
 - about_tab: Utilized for rendering the About section.

@requirementsTraceability:
 - RQ_MainApp: Should provide a main entry point for the app and render different tabs.

@briefDescription: 
 streamlit_app encapsulates the functionalities related to the main entry point of the app.

@methods:
 - None

@contributors: 
 - Jorge Sequeira Rojas

@examples: 
 Run the script to start the Streamlit app.
"""

import streamlit as st
import streamlit.components.v1 as components
from tabs import demo_tab, examples_tab, about_tab

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