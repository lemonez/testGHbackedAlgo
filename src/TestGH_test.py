from . import TestGH

def test_TestGH():
    assert TestGH.apply("Jane") == "hello Jane"
