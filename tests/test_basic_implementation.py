import pytest
from src.wushu_code.code_fu.merge_strings_alt import BasicImplementations



def test_manage_alternatively(): 

    bs = BasicImplementations()
    test1 = bs.mergeAlternatively("abc", "pqrs")
    test2 = bs.mergeAlternatively("ab", "pqrs")
    test3 = bs.mergeAlternatively("abcd", "pq")

    assert test1 == "apbqcrs"
    assert test2 == "apbqrs"
    assert test3 == "apbqcd"
