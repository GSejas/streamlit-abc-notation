# Streamlit ABC Notation Project

This project is a Streamlit application that showcases a custom component for rendering ABC notation using abc.js. It provides a user-friendly interface for inputting ABC notation, rendering it as sheet music, and includes playback features.

## Project Structure

```
streamlit-abc-notation
├── src
│   ├── tabs
│   │   ├── demo_tab.py
│   │   ├── examples_tab.py
│   │   └── about_tab.py
│   └── streamlit_app.py
├── package.json
├── pyproject.toml
├── poetry.lock
└── README.md
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-abc-notation
   ```

2. Install Poetry if you haven't already:
   ```
   pip install poetry
   ```

3. Install the Python dependencies using Poetry:
   ```
   poetry install
   ```

## Usage

To run the Streamlit application, execute the following command in the terminal:

```
poetry run streamlit run src/streamlit_app.py
```

Once the application is running, you can:

- Input ABC notation in the provided text area.
- Click the "Render" button to visualize the sheet music.
- Use the playback controls to listen to the rendered music.

## ABC Notation

ABC notation is a shorthand form of musical notation that uses ASCII characters. It is widely used for notating music in a simple and readable format. For more information on ABC notation, visit [abcnotation.com](http://abcnotation.com).

### Examples of ABC Notation

Here are some popular melodies and harmonies you can try:

**Twinkle Twinkle Little Star**
```abc
X: 1
T: Twinkle Twinkle Little Star
M: 4/4
K: C
C C G G | A A G2 | F F E E | D D C2 |
```

**Ode to Joy (Beethoven)**
```abc
X: 1
T: Ode to Joy
M: 4/4
K: D
E E F G | G F E D | C C D E | E D D2 |
```

**Happy Birthday**
```abc
X: 1
T: Happy Birthday
M: 3/4
K: C
G G A G | C B | G G A G | D C | G G G E | C B A | F F E C | D C |
```

**Jingle Bells**
```abc
X: 1
T: Jingle Bells
M: 4/4
K: G
E E E | E E E | E G C D E | F F F F | F E E E | E D D E | D G2 |
```

**Mary Had a Little Lamb**
```abc
X: 1
T: Mary Had a Little Lamb
M: 4/4
K: C
E D C D | E E E2 | D D D2 | E G G2 | E D C D | E E E E | D D E D | C3 |
```

**Silent Night**
```abc
X: 1
T: Silent Night
M: 3/4
K: G
G A G E | G A G E | D2 G2 | G A G E | G A G E | D2 G2 |
```

## Roadmap

### Current Progress

- **Basic Rendering and Playback**: Implemented a basic demo for rendering ABC notation and playing it back using abc.js.
- **Modular Code Structure**: Refactored the code into separate modules for better maintainability.

### Future Plans

- **Enhanced ABC.js Integration**: Create new components to explore more features of the abc.js library and enhance the notation capabilities.
- **Community Testing and Feedback**: Deploy the project to Streamlit for community testing and feedback.

## Deployment

The project is deployed on Streamlit and can be accessed at [https://abc-notation.streamlit.app/](https://abc-notation.streamlit.app/). The goal is to inspire and help grow the intersection between technology and music.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.