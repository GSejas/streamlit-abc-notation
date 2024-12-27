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
