import pytest
from src import handlers

def test_print_list_to_str():
    ma_liste = ["3","4","5", "Fabrice"]
    assert handlers.print_list_to_str(ma_liste) == "3, 4, 5, Fabrice."
    
def test_print_list_to_str_wrong_sep():
    ma_liste = ["3","4","5", "Fabrice"]
    assert handlers.print_list_to_str(ma_liste) != "3 - 4 - 5 - Fabrice."
    
