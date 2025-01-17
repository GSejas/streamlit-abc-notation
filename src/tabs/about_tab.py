"""
@moduleName: about_tab
@version: 1.0
@since: 10-03-2023
@lastUpdated: 10-03-2023
@completionTag: TO_DO

@projectSummary: 
 This module renders the About tab of the ABC Notation Renderer app.

@techStack: Python, Streamlit

@dependency: streamlit

@interModuleDependency: 
 - main.py: Utilizes about_tab for rendering the About section.

@requirementsTraceability:
 - RQ_AboutTab: Should provide information about the app and its purpose.

@briefDescription: 
 about_tab encapsulates the functionalities related to rendering the About section of the app.

@methods:
 - render: Renders the About tab content.

@contributors: 
 - Jorge Sequeira Rojas

@examples: 
 import about_tab
 about_tab.render()
"""

import streamlit as st

def render():
    # Description of the app
    st.markdown("""
    Welcome to the ABC Notation Renderer! My name is Jorge, I'm extremely passionate about music and technology, and while playing around with AI+Music, to enhance my own understanding of both, I come across the abc.js library, which then let me to create this basic demo implementation.
                
    This tool allows you to render ABC notation
    into musical scores and play them back with audio. ABC notation is a shorthand form
    of musical notation that uses the letters A through G, along with other symbols,
    to represent music.
    """)

    # Footer with documentation link
    st.markdown("""
    ---
    For more information on ABC notation, visit the [ABC Notation website](http://abcnotation.com/).
    """)
