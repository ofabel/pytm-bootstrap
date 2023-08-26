from app import Exercise


def test_magnitude_calculation():
    assert Exercise._magnitude(0, 0, 1, 0) == 1
    assert Exercise._magnitude(0, 0, 2, 0) == 2
    assert Exercise._magnitude(1, 1, 1, 5) == 4
    assert Exercise._magnitude(-1, -2, 3, 5) - 8.062 < 0.1


def test_check_with_all_wrong_magnitudes():
    assert Exercise.check(a_b=1, b_c=2, a_c=3,
                          a_x=1, a_y=1,
                          b_x=3, b_y=3,
                          c_x=2, c_y=1) == 0.0


def test_check_with_one_correct_magnitude():
    assert Exercise.check(a_b=16.55, b_c=2, a_c=3,
                          a_x=4, a_y=8,
                          b_x=19, b_y=15,
                          c_x=16, c_y=4) == 0.2


def test_check_with_two_correct_magnitudes():
    assert Exercise.check(a_b=13.453, b_c=2, a_c=6,
                          a_x=7, a_y=3,
                          b_x=16, b_y=13,
                          c_x=13, c_y=3) == 0.5


def test_check_with_all_correct_magnitudes():
    assert Exercise.check(a_b=17.029, b_c=10.198, a_c=11.045,
                          a_x=5, a_y=5,
                          b_x=18, b_y=16,
                          c_x=16, c_y=6) == 1.0
