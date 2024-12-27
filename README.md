# Streamlit ABC Notation Project

This project is a Streamlit application that showcases a custom component for rendering ABC notation using abc.js. It provides a user-friendly interface for inputting ABC notation, rendering it as sheet music, and includes playback features.

## Project Structure

```
streamlit-abc-notation
├── src
│   ├── components
│   │   └── abc_notation_renderer.js
│   ├── streamlit_app.py
│   └── styles
│       └── custom.css
├── package.json
├── requirements.txt
└── README.md
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-abc-notation
   ```

2. Install the Python dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Install the JavaScript dependencies:
   ```
   cd src
   npm install
   ```

## Usage

To run the Streamlit application, execute the following command in the terminal:

```
streamlit run streamlit_app.py
```

Once the application is running, you can:

- Input ABC notation in the provided text area.
- Click the "Render" button to visualize the sheet music.
- Use the playback controls to listen to the rendered music.

## ABC Notation

ABC notation is a shorthand form of musical notation that uses ASCII characters. It is widely used for notating music in a simple and readable format. For more information on ABC notation, visit [abcnotation.com](http://abcnotation.com).

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.