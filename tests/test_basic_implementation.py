import pytest
from src.wushu_code.code_fu.merge_strings_alt import BasicImplementations



def test_manage_alternatively(): 

    bs = BasicImplementations()
    test1 = bs.mergeAlternatively("abc", "pqrs")

    assert test1 == "apbqcrs"
