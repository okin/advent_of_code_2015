from day6 import split_command, Command, turn_off, turn_on, toggle, generate_grid


def test_splitting_actions():
    assert Command(turn_on, (0, 0), (999, 999)) == split_command("turn on 0,0 through 999,999")
    assert Command(toggle, (0, 0), (999, 0)) == split_command("toggle 0,0 through 999,0")
    assert Command(turn_off, (499, 499), (500, 500)) == split_command("turn off 499,499 through 500,500")


def test_grid_creation():
    assert [[False, False, False],
            [False, False, False],
            [False, False, False]] == generate_grid(3, 3)