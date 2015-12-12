from day9 import PathFinder


EXAMPLE_INPUT = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""


def test_parsing_input():
    p = PathFinder()
    assert not p.routes

    p.parse(EXAMPLE_INPUT.split('\n'))

    assert p.routes['London']['Belfast'] == 518
    assert p.routes['London']['Dublin'] == 464
    assert p.routes['Dublin']['Belfast'] == 141
    assert p.routes['Belfast']['London'] == 518
    assert p.routes['Dublin']['London'] == 464
    assert p.routes['Belfast']['Dublin'] == 141

    assert len(p.routes) == 3
    for start, destinations in p.routes.items():
        assert len(destinations) == 2


def test_calculating_possible_routes():
    p = PathFinder()
    p.parse(EXAMPLE_INPUT.split('\n'))

    possible_routes = set([
        (('Dublin', 'London', 'Belfast'), 982),
        (('London', 'Dublin', 'Belfast'), 605),
        (('London', 'Belfast', 'Dublin'), 659),
        (('Dublin', 'Belfast', 'London'), 659),
        (('Belfast', 'Dublin', 'London'), 605),
        (('Belfast', 'London', 'Dublin'), 982)
    ])

    filled = False
    for match in p.get_all_routes():
        filled = True
        assert match in possible_routes

    assert filled


def test_calculating_shortest_route():
    p = PathFinder()
    p.parse(EXAMPLE_INPUT.split('\n'))

    route, distance = p.calculate_shortest_route()

    assert distance == 605
    assert route == ('London', 'Dublin', 'Belfast')