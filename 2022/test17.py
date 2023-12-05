from __future__ import annotations
import sys
import math
import itertools
import typing as t
from dataclasses import dataclass


@dataclass(frozen=True)
class Coord:
    x: int
    y: int

    def __add__(self: Coord, other: Coord) -> Coord:
        if not isinstance(other, Coord):
            return NotImplemented
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self: Coord, other: Coord) -> Coord:
        if not isinstance(other, Coord):
            return NotImplemented
        return Coord(self.x - other.x, self.y - other.y)


Shape = t.NewType("Shape", set[Coord])
raw_shapes = """\
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
""".strip().split(
    "\n\n"
)
SHAPES = [
    Shape(
        {
            Coord(x, y)
            for y, line in enumerate(reversed(raw_shape.splitlines()))
            for x, char in enumerate(line)
            if char == "#"
        }
    )
    for raw_shape in raw_shapes
]
WIDTH = 7


def xs(coords: t.Iterable[Coord]) -> t.Iterable[int]:
    return {c.x for c in coords}


def ys(coords: t.Iterable[Coord]) -> t.Iterable[int]:
    return {c.y for c in coords}


def move(rock: set[Coord], delta: Coord) -> set[Coord]:
    return {coord + delta for coord in rock}


def crop(coords: set[Coord], miny, maxy) -> set[Coord]:
    return {c for c in coords if miny <= c.y <= maxy}


@dataclass
class State:
    jets: list[Coord]
    jet_idx: int
    shapes: list[Shape]
    shape_idx: int
    filled: set[Coord]

    @dataclass(frozen=True)
    class Fingerprint:
        jet_idx: int
        shape_idx: int
        top: frozenset[Coord]

    def add_rock(self) -> None:
        shape = self.shapes[self.shape_idx]
        self.shape_idx += 1
        self.shape_idx %= len(self.shapes)

        top = 1 + max(ys(self.filled), default=-1)
        offset = Coord(2, top + 3)
        rock = move(shape, offset)

        down = Coord(0, -1)
        while True:
            left_or_right = self.jets[self.jet_idx]
            self.jet_idx += 1
            self.jet_idx %= len(self.jets)

            moved = move(rock, left_or_right)
            if (
                not moved & self.filled
                and min(xs(moved)) >= 0
                and max(xs(moved)) < WIDTH
            ):
                rock = moved

            moved = move(rock, down)
            if moved & self.filled or min(ys(moved)) < 0:
                break
            rock = moved

        self.filled |= rock

    def add_rocks(self, n: int) -> None:
        for _ in range(n):
            self.add_rock()

    @property
    def fingerprint(self) -> State.Fingerprint:
        # Determine the shape of the void at the top of the
        # tower using a flood-fill. Hopefully it's not too large.
        #
        # ...nevermind, I cba with that. I'm just going to assume
        # that the top 20 rows are sufficient for detecting cycles
        # instead.
        return State.Fingerprint(
            jet_idx=self.jet_idx,
            shape_idx=self.shape_idx,
            top=frozenset(
                move(
                    crop(self.filled, self.height - 20, self.height),
                    Coord(0, -self.height),
                )
            ),
        )

    @property
    def height(self) -> int:
        return max(ys(self.filled), default=-1) + 1


def main() -> int:
    raw = sys.stdin.read()

    # Parsing
    left_or_right = {"<": Coord(-1, 0), ">": Coord(+1, 0)}
    JETS = [left_or_right[char] for char in raw.strip()]

    try:
        iterations = int(sys.argv[1])
    except IndexError:
        iterations = 2022

    # Part 1
    state = State(
        jets=JETS,
        jet_idx=0,
        shapes=SHAPES,
        shape_idx=0,
        filled=set(),
    )
    state.add_rocks(iterations)
    view_top(state.filled, 10)
    part1 = state.height
    print(part1)

    # Part 2
    bignum = 1000000000000

    state = State(
        jets=JETS,
        jet_idx=0,
        shapes=SHAPES,
        shape_idx=0,
        filled=set(),
    )

    seen: dict[State.Fingerprint, tuple[int, int]] = {}
    idx, cycle_len, height_change = -1, -1, -1
    for idx in itertools.count(0):
        if state.fingerprint in seen:
            prev_idx, prev_height = seen[state.fingerprint]
            cycle_len = idx - prev_idx
            height_change = state.height - prev_height
            break
        seen[state.fingerprint] = (idx, state.height)
        state.add_rock()

    rocks_added = idx
    height = state.height
    print(f"Cycle detected! {rocks_added=} {cycle_len=} {height=} {height_change=}")

    remaining = bignum - rocks_added
    div, mod = divmod(remaining, cycle_len)

    state.add_rocks(mod)
    part2 = state.height + div * height_change
    print(part2)

    return 0


def vis(filled: set[Coord]):
    draw(
        charmap={
            "#": filled,
            ".": {Coord(6, min(ys(filled)))},
        },
        empty=".",
    )


def view_top(coords: set[Coord], n: int = 10):
    top = max(ys(coords), default=0)
    vis(crop(coords, top - n, top))


def draw(charmap: dict[str, set[Coord]], empty: str = ".") -> None:
    ps = set.union(*charmap.values())
    minx = min(xs(ps))
    maxx = max(xs(ps))
    miny = min(ys(ps))
    maxy = max(ys(ps))
    xrange = range(minx, maxx + 1)
    yrange = range(miny, maxy + 1)
    margin = max(len(str(y)) for y in yrange)
    for y in reversed(yrange):
        print(f"{y:>{margin}} ", end="")
        for x in xrange:
            point = Coord(x, y)
            for char, point_set in charmap.items():
                if point in point_set:
                    print(char, end="")
                    break
            else:
                print(empty, end="")
        print()
    print()


if __name__ == "__main__":
    sys.exit(main())
