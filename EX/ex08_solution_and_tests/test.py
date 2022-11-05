"""Tests for solution.py."""
from solution import fruit_order
from solution import lottery
from solution import students_study

"""These are for testing student_study function in solution.py."""


def test__student_study__day_coffee_true():
    """Test day coffee true."""
    assert students_study(14, True) is True


def test__student_study__day_coffee_false():
    """Test day coffee false."""
    assert students_study(12, False) is False


def test__student_study__day_edge_case_coffee_true():
    """Test day edge case coffee true."""
    assert students_study(5, True) is True
    assert students_study(17, True) is True


def test__student_study__day_edge_case_coffee_false():
    """Test day edge case coffee false."""
    assert students_study(5, False) is False
    assert students_study(17, False) is False


def test__student_study__evening_coffee_true():
    """Test evening coffee true."""
    assert students_study(19, True) is True


def test__student_study__evening_coffee_false():
    """Test evening coffee false."""
    assert students_study(19, False) is True


def test__student_study__evening_edge_case_coffee_true():
    """Test evening edge case coffee true."""
    assert students_study(18, True) is True
    assert students_study(24, True) is True


def test__student_study__evening_edge_case_coffee_false():
    """Test evening edge case coffee false."""
    assert students_study(18, False) is True
    assert students_study(24, False) is True


def test__student_study__night_coffee_false():
    """Test night coffee false."""
    assert students_study(3, False) is False


def test__student_study__night_edge_case_coffee_true():
    """Test evening edge case coffee true."""
    assert students_study(1, True) is False
    assert students_study(4, True) is False


def test__student_study__night_coffee_true():
    """Test night coffee true."""
    assert students_study(2, True) is False


def test__student_study__night_edge_case_coffee_false():
    """Test evening edge case coffee false."""
    assert students_study(1, False) is False
    assert students_study(4, False) is False


"""These are for testing lottery function in solution.py."""


def test__lottery__all_fives():
    """Test all fives."""
    assert lottery(5, 5, 5) == 10


def test__lottery__all_same_zero():
    """Test all same zero."""
    assert lottery(0, 0, 0) == 5


def test__lottery__all_same_positive():
    """Test all same positive."""
    assert lottery(3, 3, 3) == 5


def test__lottery__all_same_negative():
    """Test all same negative."""
    assert lottery(-2, -2, -2) == 5


def test__lottery__b_c_same_a_diff():
    """Test b, c same a different."""
    assert lottery(2, 3, 3) == 1


def test__lottery__all_diff():
    """Test all different."""
    assert lottery(2, 5, 3) == 1


def test__lottery__a_b_same_c_diff():
    """Test a, b same c different."""
    assert lottery(3, 3, 2) == 0


def test__lottery__a_c_same_b_diff():
    """Test a, c same b different."""
    assert lottery(3, 2, 3) == 0


"""These are for testing fruit_order function in solution.py."""


def test__fruit_order__zero_amount_zero_big():
    """Test zero amount zero big."""
    assert fruit_order(4, 0, 0) == 0


def test__fruit_order__zero_amount_others_not_zero():
    """Test zero amount others not zero."""
    assert fruit_order(4, 7, 0) == 0


def test__fruit_order__all_zero():
    """Test all zero."""
    assert fruit_order(0, 0, 0) == 0


def test__fruit_order__zero_amount_zero_small():
    """Test zero amount zero small."""
    assert fruit_order(0, 5, 0) == 0


def test__fruit_order__only_big_exact_match():
    """Test only big exact match."""
    assert fruit_order(0, 2, 10) == 0


def test__fruit_order__only_big_not_enough_but_multiple_of_5():
    """Test not enough but multiple of 5."""
    assert fruit_order(0, 2, 15) == -1


def test__fruit_order__only_big_more_than_required_match():
    """Test only big more than required match."""
    assert fruit_order(0, 5, 15) == 0


def test__fruit_order__only_big_more_than_required_no_match():
    """Test only big more than required no match."""
    assert fruit_order(0, 5, 17) == -1


def test__fruit_order__only_big_not_enough():
    """Test only big not enough."""
    assert fruit_order(0, 1, 10) == -1


def test__fruit_order__only_small_match_more_than_5_smalls():
    """Test only small_match_more_than_5_smalls."""
    assert fruit_order(10, 0, 10) == 10


def test__fruit_order__only_small_not_enough():
    """Test only small not enough."""
    assert fruit_order(4, 0, 11) == -1


def test__fruit_order__only_small_more_than_required():
    """Test only small more than required."""
    assert fruit_order(15, 0, 7) == 7


def test__fruit_order__only_small_not_enough_more_than_5_smalls():
    """Test only small not enough more than 5 smalls."""
    assert fruit_order(11, 0, 14) == -1


def test__fruit_order__only_small_exact_match():
    """Test only small exact match."""
    assert fruit_order(11, 0, 11) == 11


def test__fruit_order__match_with_more_than_5_smalls():
    """Test match with more than 5 smalls."""
    assert fruit_order(13, 0, 13) == 13


def test__fruit_order__use_some_smalls_all_bigs():
    """Test use some smalls all bigs."""
    assert fruit_order(9, 2, 12) == 2


def test__fruit_order__use_some_smalls_some_bigs():
    """Test use some smalls some bigs."""
    assert fruit_order(6, 5, 13) == 3


def test__fruit_order__all_positive_exact_match():
    """Test all positive exact match."""
    assert fruit_order(3, 2, 13) == 3


def test__fruit_order__enough_bigs_not_enough_smalls_large_numbers():
    """Test enough bigs not enough smalls large numbers."""
    assert fruit_order(3, 500, 2474) == -1


def test__fruit_order__match_large_numbers():
    """Test match large numbers."""
    assert fruit_order(627, 282, 2034) == 624


def test__fruit_order__use_all_smalls_some_bigs():
    """Test use all smalls some bigs."""
    assert fruit_order(3, 5, 13) == 3


def test__fruit_order__not_enough():
    """Test not enough."""
    assert fruit_order(6, 1, 16) == -1


def test__fruit_order__enough_bigs_not_enough_smalls():
    """Test enough bigs not enough smalls."""
    assert fruit_order(3, 14, 64) == -1


def test__fruit_order__not_enough_with_more_than_5_smalls():
    """Test not enough with more than 5 smalls."""
    assert fruit_order(7, 1, 18) == -1
