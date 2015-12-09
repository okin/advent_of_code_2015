from day6 import split_command, Command, turn_off, turn_on, toggle, generate_grid, count_activated_lamps, process_command, print_grid


def test_splitting_actions():
    assert Command(turn_on, (0, 0), (999, 999)) == split_command("turn on 0,0 through 999,999")
    assert Command(toggle, (0, 0), (999, 0)) == split_command("toggle 0,0 through 999,0")
    assert Command(turn_off, (499, 499), (500, 500)) == split_command("turn off 499,499 through 500,500")


def test_grid_creation():
    assert [[False, False, False],
            [False, False, False],
            [False, False, False]] == generate_grid(3, 3)


def test_turn_off():
    assert not turn_off(False)
    assert not turn_off(True)


def test_turn_on():
    assert turn_on(False)
    assert turn_on(True)


def test_toggle():
    assert not toggle(True)
    assert toggle(False)


def test_work_on_grid():
    testGrid = generate_grid(5, 5)
    assert count_activated_lamps(testGrid) == 0

    process_command(testGrid, Command(toggle, (2, 2), (3, 3)))
    print_grid(testGrid)

    assert 4 == count_activated_lamps(testGrid)
    assert testGrid[2][2]
    assert testGrid[2][3]
    assert testGrid[3][2]
    assert testGrid[3][3]

    process_command(testGrid, Command(toggle, (2, 2), (3, 3)))
    print_grid(testGrid)

    assert 0 == count_activated_lamps(testGrid)
