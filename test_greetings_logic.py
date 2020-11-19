import pytest
from greeting_logic import GreetingGenerator


def test_get_greeting():
    gg = GreetingGenerator()
    assert gg.get_greeting() == "hello world!"
