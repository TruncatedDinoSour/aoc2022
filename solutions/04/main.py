#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC -- day 4"""

import sys
from warnings import filterwarnings as filter_warnings

import tabulate  # type: ignore


def log(msg: str) -> None:
    print(f" \033[1m\033[32m*\033[0m {msg}")


def part_one(data: list[tuple[int, ...]]) -> int:
    return sum(
        line[0] <= line[2] <= line[3] <= line[1]
        or line[2] <= line[0] <= line[1] <= line[3]
        for line in data
    )


def part_two(data: list[tuple[int, ...]]) -> int:
    return sum(
        line[0] <= line[2] <= line[1] or line[2] <= line[0] <= line[3] for line in data
    )


def main() -> int:
    """Entry/main function"""

    log("Reading and splitting data from stdin")
    data: list[list[str]] = [line.split(",") for line in map(str.strip, sys.stdin)]

    log("Prepating data")
    data_preped: list[tuple[int, ...]] = [
        tuple(map(int, (*line[0].split("-"), *line[1].split("-")))) for line in data
    ]

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
                "Full ranges (pt 1)",
                "Overlapping ranges (pt 2)",
            ),
            tablefmt="grid",
        )
    )

    return 0


if __name__ == "__main__":
    assert main.__annotations__.get("return") is int, "main() should return an integer"

    filter_warnings("error", category=Warning)
    sys.exit(main())
