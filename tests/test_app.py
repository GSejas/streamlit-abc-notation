
from streamlit.testing.v1 import AppTest
import pytest

@pytest.mark.smoke
def test_streamlit_app():
    at = AppTest.from_file("src/streamlit_app.py")
    at.run()
    assert not at.exception