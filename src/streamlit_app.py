import streamlit as st
import streamlit.components.v1 as components

# Title of the app
st.title("ABC Notation Renderer")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Demo", "Examples", "About"])

with tab1:
    # Sidebar for inputs and controls
    st.sidebar.header("Settings")

    # Text area for ABC notation input
    abc_notation = st.sidebar.text_area(
        "Enter ABC Notation",
        value="X: 1\nT: Scale\nM: 4/4\nK: C\nC D E F | G A B c |",
        height=200
    )
    st.sidebar.markdown(
        "Enter your ABC notation above. You can use the example provided as a starting point."
    )

    # Height for the custom component
    height = st.sidebar.slider("Select height for rendering", 200, 800, 400)
    st.sidebar.markdown(
        "Adjust the height of the rendered musical score using the slider above."
    )

    # Custom CSS input
    custom_css = st.sidebar.text_area("Custom CSS", value="pre { color: red; }", height=100)
    st.sidebar.markdown(
        "You can customize the appearance of the rendered musical score by entering custom CSS above."
    )

    # Checkbox for continuous rendering
    continuous_render = st.sidebar.checkbox("Enable continuous rendering", value=False)
    st.sidebar.markdown(
        "Enable this option to render the ABC notation continuously without pressing the 'Render' button."
    )

    # Buttons for rendering and clearing the input
    if not continuous_render:
        with st.container():
            # Create two columns for the buttons
            col1, col2 = st.sidebar.columns(2)

            # Button to render the ABC notation in the first column
            with col1:
                renderClicked = st.button(
                    "Render", use_container_width=True, help="Render the ABC notation", key="render",
                    type='primary',
                    icon=":material/play_arrow:"
                )

            # Button to clear the input in the second column
            with col2:
                clear = st.button(
                    "Clear", 
                    use_container_width=True,
                    help="Clear the input fields and start over",
                    type='secondary',
                    icon=":material/delete:"
                )
    else:
        renderClicked = False
        clear = False

    # Render the ABC notation if the render button is clicked or continuous rendering is enabled
    if renderClicked or continuous_render:
        components.html(
            f"""
            <div id="paper" style="width: 100%;"></div>
            <div id="audio"></div>
            <link rel="stylesheet" type="text/css"
                  href="https://cdn.jsdelivr.net/npm/abcjs@6.3.0/dist/abcjs-audio.css">
            <script src="https://cdn.jsdelivr.net/npm/abcjs@6.3.0/dist/abcjs-basic-min.js">
            </script>
            <script type="text/javascript">
                document.addEventListener('DOMContentLoaded', function() {{
                    const abcNotation = `{abc_notation}`;
                    const customCss = `{custom_css}`;
                    const styleElement = document.createElement('style');
                    styleElement.innerHTML = customCss;
                    document.head.appendChild(styleElement);

                    var visualOptions = {{
                        responsive: 'resize'
                    }};
                    var visualObj = ABCJS.renderAbc("paper", abcNotation, visualOptions);

                    if (ABCJS.synth.supportsAudio()) {{
                        var controlOptions = {{
                            displayRestart: true,
                            displayPlay: true,
                            displayProgress: true,
                            displayClock: true
                        }};
                        var synthControl = new ABCJS.synth.SynthController();
                        synthControl.load("#audio", null, controlOptions);
                        var midiBuffer = new ABCJS.synth.CreateSynth();
                        midiBuffer.init({{
                            visualObj: visualObj[0],
                            options: {{}}
                        }}).then(function () {{
                            synthControl.setTune(visualObj[0], true).then(function (response) {{
                                document.querySelector(".abcjs-inline-audio")
                                        .classList.remove("disabled");
                            }});
                        }});
                    }} else {{
                        console.log("audio is not supported on this browser");
                    }}
                }});
            </script>
            """,
            height=height + 50
        )

    if clear:
        st.rerun()

with tab2:
    # Example ABC notation
    st.markdown("""
    ### What is ABC Notation?
    ABC notation is a shorthand form of musical notation that uses the letters A through G,
    along with other symbols, to represent music.
    """)

    # Example ABC notation
    st.markdown("""
    ### Example ABC Notation:
    ```
    X: 1
    T: Scale
    M: 4/4
    K: C
    C D E F | G A B c |
    ```
    """)

with tab3:
    # Description of the app
    st.markdown("""
    Welcome to the ABC Notation Renderer! This tool allows you to render ABC notation
    into musical scores and play them back with audio. ABC notation is a shorthand form
    of musical notation that uses the letters A through G, along with other symbols,
    to represent music.
    """)

    # Footer with documentation link
    st.markdown("""
    ---
    For more information on ABC notation, visit the [ABC Notation website](http://abcnotation.com/).
    """)