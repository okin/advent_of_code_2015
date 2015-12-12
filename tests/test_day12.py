from day12 import count_numbers


def test_counting():
    assert 6 == count_numbers("[1,2,3]")
    assert 6 == count_numbers('{"a":2,"b":4}')

    assert 3 == count_numbers("[[[3]]]")
    assert 3 == count_numbers('{"a":{"b":4},"c":-1}')

    assert 0 == count_numbers('{"a":[-1,1]}')
    assert 0 == count_numbers('[-1,{"a":1}]')

    assert 0 == count_numbers("[]")
    assert 0 == count_numbers("{}")


def test_counting_and_ignoring_red():
    assert 6 == count_numbers('[1,2,3]', ignore_red=True)
    assert 4 == count_numbers('[1,{"c":"red","b":2},3]', ignore_red=True)
    assert 0 == count_numbers('{"d":"red","e":[1,2,3,4],"f":5}', ignore_red=True)
    assert 6 == count_numbers('[1,"red",5]', ignore_red=True)
