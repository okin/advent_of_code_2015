from day6 import (split_command, Command, turn_off, turn_on, toggle, generate_grid, count_activated_lamps,
                  process_command, print_grid, sum_brightness, improved_action_factory)


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
    test_grid = generate_grid(5, 5)
    assert count_activated_lamps(test_grid) == 0

    process_command(test_grid, Command(toggle, (2, 2), (3, 3)))
    print_grid(test_grid)

    assert 4 == count_activated_lamps(test_grid)
    assert test_grid[2][2]
    assert test_grid[2][3]
    assert test_grid[3][2]
    assert test_grid[3][3]

    process_command(test_grid, Command(toggle, (2, 2), (3, 3)))
    print_grid(test_grid)

    assert 0 == count_activated_lamps(test_grid)


def test_working_on_grid_with_improved_instructions():
    test_grid = generate_grid(1000, 1000)
    process_command(test_grid, split_command("turn on 0,0 through 0,0", improved_action_factory))
    assert 1 == sum_brightness(test_grid)

    test_grid = generate_grid(1000, 1000)
    process_command(test_grid, split_command("toggle 0,0 through 999,999", improved_action_factory))
    assert 2000000 == sum_brightness(test_grid)
