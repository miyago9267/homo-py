# tests/test_homo.py
import pytest
from homo_py import homo

def test_homo_positive_integer():
    result = homo(229028)
    assert result == "114514+114514"

def test_homo_negative_integer():
    result = homo(-114514)
    assert result == "(11-4-5+1-4)*114514"

def test_homo_float():
    result = homo(1145.14)
    assert "114514" in result

def test_homo_min_one():
    result = homo(114513)
    assert "114*514+11*4514+114*51+4-1-1+451-4" in result

def test_homo_zero():
    result = homo(0)
    assert result == "(1-1)*4514"

def test_homo_non_digit_string():
    result = homo("abc")
    assert result == "這麼惡臭的abc有必要論證嗎（惱"