from feez_buzz_handler import FeezBuzzHandler
import pytest
import re

def test_get_player_value_FEEZ():
    n=3
    assert FeezBuzzHandler.get_value_to_show(n) == "FEEZ"

def test_get_player_value_BUZZ():
    n=5
    assert FeezBuzzHandler.get_value_to_show(n) == "BUZZ"

def test_get_player_value_FEEZ_BUZZ():
    n=15
    assert FeezBuzzHandler.get_value_to_show(n) == "FEEZ-BUZZ"

def test_get_player_value_strInt():
    n="4"
    assert FeezBuzzHandler.get_value_to_show(n) == 4

def test_get_player_value_float():
    n=4.6
    assert FeezBuzzHandler.get_value_to_show(n) == 4

def test_get_player_value_negative_FEEZA():
    n=-3
    assert FeezBuzzHandler.get_value_to_show(n) == "FEEZ"

def test_get_player_value_negative_BUZZ():
    n=-5
    assert FeezBuzzHandler.get_value_to_show(n) == "BUZZ"

def test_get_player_value_str():
    n="I am a string value"
    expected = f"number have to be an integer, not {type(n)} -> ({n})"
    with pytest.raises(ValueError,match=re.escape(expected)):
        FeezBuzzHandler.get_value_to_show(n)
    
def test_get_player_value_none():
    n=None
    expected = f"number have to be an integer, not {type(n)} -> ({n})"
    with pytest.raises(ValueError,match=re.escape(expected)):
        FeezBuzzHandler.get_value_to_show(n)

def test_get_player_value_zero():
    n=0
    expected = "number can be 0."
    with pytest.raises(ValueError,match=re.escape(expected)):
        FeezBuzzHandler.get_value_to_show(n)

