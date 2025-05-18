import bmi as bmi

def test_bmi_normal_weight():

    b_mi, ret_value = bmi.calculate_bmi(80, 1.9)
    
    assert (ret_value == 0)


def test_bmi_over_weight():
    b_mi, ret_value = bmi.calculate_bmi(80, 1.6)

    assert (ret_value == 1)

def test_bmi_under_weight():
    b_mi, ret_value = bmi.calculate_bmi(40, 2.2)

    assert (ret_value == -1)