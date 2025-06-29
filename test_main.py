# test_main.py
from main import greet, unused, unusedagain

def test_greet():
    assert greet() == "Hello, CI!"

def test_unused():
    assert unused() == "This function is not covered by tests"

def test_unusedagain():
    assert unusedagain == "Not covered"