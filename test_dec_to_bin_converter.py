"""Number converter module tester"""

import pytest
import dec_to_bin_converter as converter


def test_correct_conversion():
    """Test if correct number is converted properly"""
    assert converter.dec_to_bin(0) == "0"
    assert converter.dec_to_bin(2) == "10"
    assert converter.dec_to_bin(63) == "111111"


def test_out_of_range():
    """Test if given number is out in range"""
    with pytest.raises(ValueError):
        converter.dec_to_bin(-1)

    with pytest.raises(ValueError):
        converter.dec_to_bin(101)


def test_number_not_int():
    """Test if given number is not of type Int"""
    with pytest.raises(ValueError):
        converter.dec_to_bin(55.77)
