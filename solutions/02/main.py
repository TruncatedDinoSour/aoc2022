#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC -- day 2"""

import sys
from warnings import filterwarnings as filter_warnings

import tabulate  # type: ignore

RPS: dict[str, str] = {
    "A": "R",
    "B": "P",
    "C": "S",
    "X": "R",
    "Y": "P",
    "Z": "S",
}

WIN: dict[str, tuple[str, int]] = {
    "R": ("S", 1),
    "P": ("R", 2),
    "S": ("P", 3),
}


def log(msg: str) -> None:
    print(f" \033[1m\033[32m*\033[0m {msg}")


def part_one(data: list[str]) -> int:
    points: int = 0

    for line in data:
        oponent, us = line.split()

        if oponent == us:
            points += 3
        elif WIN[oponent][0] != us:
            points += 6

        points += WIN[us][1]

    return points


def part_two(data: list[str]) -> int:
    lose: dict[str, str] = {v[0]: k for k, v in WIN.items()}

    points: int = 0

    for line in data:
        oponent, us = line.split()

        match us:
            case "R":
                points += WIN[WIN[oponent][0]][1]

            case "P":
                points += WIN[oponent][1] + 3

            case "S":
                points += WIN[lose[oponent]][1] + 6

    return points


def main() -> int:
    """Entry/main function"""

    log("Reading data from stdin")
    data: str = sys.stdin.read().strip()

    log("Preparing data")
    for replace, sub in RPS.items():
        data = data.replace(replace, sub)

    data_preped: list[str] = data.splitlines()

    log("Solving problems")
    print(
        "\n"
        + tabulate.tabulate(
            (
                (
                    len(data_preped),
                    part_one(data_preped),
                    part_two(data_preped),
                ),
            ),
            headers=(
                "Data size",
                "Strategy (pt 1)",
                "Total strategy (pt 2)",
            ),
            tablefmt="grid",
        )
    )

    return 0


if __name__ == "__main__":
    assert main.__annotations__.get("return") is int, "main() should return an integer"

    filter_warnings("error", category=Warning)
    sys.exit(main())
