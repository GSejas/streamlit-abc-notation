"""
@moduleName: examples_tab
@version: 1.0
@since: 10-03-2023
@lastUpdated: 10-03-2023
@completionTag: TO_DO

@projectSummary: 
 This module renders the Examples tab of the ABC Notation Renderer app.

@techStack: Python, Streamlit

@dependency: streamlit

@interModuleDependency: 
 - main.py: Utilizes examples_tab for rendering the Examples section.

@requirementsTraceability:
 - RQ_ExamplesTab: Should provide examples of ABC notation.

@briefDescription: 
 examples_tab encapsulates the functionalities related to rendering the Examples section of the app.

@methods:
 - render: Renders the Examples tab content.

@contributors: 
 - Jorge Sequeira Rojas

@examples: 
 import examples_tab
 examples_tab.render()
"""

import streamlit as st

def render():
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

    # Additional examples from famous works
    st.markdown("""
    ### Additional Examples from Famous Works:
Here are some popular melodies and harmonies you can add as examples:

### Twinkle Twinkle Little Star
```abc
X: 1
T: Twinkle Twinkle Little Star
M: 4/4
K: C
C C G G | A A G2 | F F E E | D D C2 |
```

### Ode to Joy (Beethoven)
```abc
X: 1
T: Ode to Joy
M: 4/4
K: D
E E F G | G F E D | C C D E | E D D2 |
```

### Happy Birthday
```abc
X: 1
T: Happy Birthday
M: 3/4
K: C
G G A G | C B | G G A G | D C | G G G E | C B A | F F E C | D C |
```

### Jingle Bells
```abc
X: 1
T: Jingle Bells
M: 4/4
K: G
E E E | E E E | E G C D E | F F F F | F E E E | E D D E | D G2 |
```

### Mary Had a Little Lamb
```abc
X: 1
T: Mary Had a Little Lamb
M: 4/4
K: C
E D C D | E E E2 | D D D2 | E G G2 | E D C D | E E E E | D D E D | C3 |
```

### Silent Night
```abc
X: 1
T: Silent Night
M: 3/4
K: G
G A G E | G A G E | D2 G2 | G A G E | G A G E | D2 G2 |
```
    """)
