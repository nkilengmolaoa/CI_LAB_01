# test_main.py
from main import greet

def test_greet():
    assert greet() == "Hello, CI!"