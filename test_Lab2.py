import Lab2 as lab2

def test_min_max():
    test_arr = [1, 10, 100, 1000, 9999]

    result = lab2.find_min_max(test_arr)

    assert (result == [1, 9999])

def test_average():
    test_arr = [1, 3, 5, 7, 9]

    result = lab2.calc_average(test_arr)

    assert (result == 5)
