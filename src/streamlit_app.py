import streamlit as st
import streamlit.components.v1 as components

# Title of the app
st.title("ABC Notation Renderer")

# Text area for ABC notation input
abc_notation = st.text_area("Enter ABC Notation", value="X: 1\nT: Scale\nM: 4/4\nK: C\nC D E F | G A B c |")

# Height for the custom component
height = st.slider("Select height for rendering", 200, 800, 400)

# Custom CSS input
custom_css = st.text_area("Custom CSS", value="pre { color: red; }")

# # Button to render the ABC notation
# if st.button("Render"):
components.html(f"""
        <div id="paper"></div>
        <div id="audio"></div>
        <script src="https://cdn.jsdelivr.net/npm/abcjs@6.3.0/dist/abcjs-basic-min.js"></script>
        
        <script type="text/javascript">
            document.addEventListener('DOMContentLoaded', function() {{
                const abcNotation = `{abc_notation}`;
                const customCss = `{custom_css}`;
                const styleElement = document.createElement('style');
                styleElement.innerHTML = customCss;
                document.head.appendChild(styleElement);

                var visualOptions = {{}};
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
                    // synthControl.disable(true);
                    var midiBuffer = new ABCJS.synth.CreateSynth();
                    midiBuffer.init({{
                        visualObj: visualObj[0],
                        options: {{}}
                    }}).then(function () {{
                        synthControl.setTune(visualObj[0], true).then(function (response) {{
                            document.querySelector(".abcjs-inline-audio").classList.remove("disabled");
                        }});
                    }});
                }} else {{
                    console.log("audio is not supported on this browser");
                }}
            }});
        </script>
    """, height=height + 50)

# # Button to clear the input
# if st.button("Clear"):
#     st.rerun()