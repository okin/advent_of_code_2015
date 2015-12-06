from collections import namedtuple

Command = namedtuple('command', ['action', 'start', 'end'])


def turn_on(lightbulb):
    return True


def turn_off(lightbulb):
    return False


def toggle(lightbulb):
    return not lightbulb


def split_command(text):
    def coordinates_to_tuple(coordinates):
        x, y = coordinates.split(',')
        return int(x), int(y)

    pre, end_text = text.split(' through ')
    action, start_text = pre.rsplit(' ', 1)

    if action == 'turn on':
        action = turn_on
    elif action == 'turn off':
        action = turn_off
    else:
        action = toggle
    return Command(action, coordinates_to_tuple(start_text), coordinates_to_tuple(end_text))


def generate_grid(width, height):
    grid = [False] * width
    return [grid] * height