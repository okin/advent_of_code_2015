from collections import defaultdict


class PathFinder:
    def __init__(self):
        self.routes = defaultdict(dict)

    def parse(self, data):
        for line in data:
            (start, end), distance = self._split_line(line)

            self.routes[start][end] = distance
            self.routes[end][start] = distance

    @staticmethod
    def _split_line(line):
        route, distance = line.rsplit(' = ', 1)
        distance = int(distance)

        start, end = route.split(' to ')

        return (start, end), distance

    def calculate_shortest_route(self):
        short_route = short_distance = None
        for route, distance in self.get_all_routes():
            if short_distance is None:
                short_distance = distance
                short_route = route

            if short_distance > distance:
                short_distance = distance
                short_route = route

        return short_route, short_distance

    def get_all_routes(self):
        for start in self.routes:
            yield from self.get_possible_routes([start])

    def get_possible_routes(self, travelled_route, distance=0):
        start = travelled_route[-1]
        total_stops = len(self.routes)

        for end, route_distance in self.routes[start].items():
            if end in travelled_route:
                continue

            new_route = travelled_route + [end]
            if len(new_route) == total_stops:
                yield tuple(new_route), route_distance + distance
            else:
                yield from self.get_possible_routes(new_route, route_distance + distance)


if __name__ == '__main__':
    PUZZLE_INPUT = """AlphaCentauri to Snowdin = 66
AlphaCentauri to Tambi = 28
AlphaCentauri to Faerun = 60
AlphaCentauri to Norrath = 34
AlphaCentauri to Straylight = 34
AlphaCentauri to Tristram = 3
AlphaCentauri to Arbre = 108
Snowdin to Tambi = 22
Snowdin to Faerun = 12
Snowdin to Norrath = 91
Snowdin to Straylight = 121
Snowdin to Tristram = 111
Snowdin to Arbre = 71
Tambi to Faerun = 39
Tambi to Norrath = 113
Tambi to Straylight = 130
Tambi to Tristram = 35
Tambi to Arbre = 40
Faerun to Norrath = 63
Faerun to Straylight = 21
Faerun to Tristram = 57
Faerun to Arbre = 83
Norrath to Straylight = 9
Norrath to Tristram = 50
Norrath to Arbre = 60
Straylight to Tristram = 27
Straylight to Arbre = 81
Tristram to Arbre = 90"""

    p = PathFinder()
    p.parse(PUZZLE_INPUT.split('\n'))
    route, distance = p.calculate_shortest_route()

    print("Route {}: {}".format(' -> '.join(route), distance))