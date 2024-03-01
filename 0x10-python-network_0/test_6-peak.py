def test_find_peak():
    # Test case 1: List with a single element
    assert find_peak([5]) == 5

    # Test case 2: List with two elements, peak at the beginning
    assert find_peak([10, 5]) == 10

    # Test case 3: List with two elements, peak at the end
    assert find_peak([5, 10]) == 10

    # Test case 4: List with three elements, peak at the middle
    assert find_peak([5, 10, 7]) == 10

    # Test case 5: List with three elements, peak at the beginning
    assert find_peak([10, 5, 7]) == 10

    # Test case 6: List with three elements, peak at the end
    assert find_peak([5, 7, 10]) == 10

    # Test case 7: List with multiple elements, peak in the middle
    assert find_peak([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == 6

    # Test case 8: List with multiple elements, peak at the beginning
    assert find_peak([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10

    # Test case 9: List with multiple elements, peak at the end
    assert find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10

    print("All test cases pass")

test_find_peak()