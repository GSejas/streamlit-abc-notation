
from streamlit.testing.v1 import AppTest


def test_streamlit_app():
    at = AppTest.from_file("src/streamlit_app.py")
    at.run()
    assert not at.exception