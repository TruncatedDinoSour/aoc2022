#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC -- day 3"""

import string
import sys
from warnings import filterwarnings as filter_warnings

import tabulate  # type: ignore

SCORES: dict[str, int] = {
    letter: score for score, letter in enumerate(string.ascii_letters, 1)
}


def log(msg: str) -> None:
    print(f" \033[1m\033[32m*\033[0m {msg}")


def part_one(data: list[tuple[str, str]]) -> int:
    total: int = 0
    common: str = ""

    for sack in data:
        for item in sack[0]:
            for item1 in sack[1]:
                if item == item1 and item not in common:
                    common += item

        total += sum(SCORES[c] for c in common)
        common = ""

    return total


def part_two(data: list[tuple[str, str]]) -> int:
    total: int = 0

    while data:
        a, b, c = ("".join(data.pop()) for _ in range(3))
        common: str = ""

        for item in a:
            for item1 in b:
                for item2 in c:
                    if item == item1 and item == item2 and item not in common:
                        common += item

        total += sum(SCORES[c] for c in common)

    return total


def main() -> int:
    """Entry/main function"""

    log("Reading and prepating data from stdin")
    data: list[tuple[str, str]] = [
        (line[: len(line) // 2], line[len(line) // 2 :])
        for line in map(str.strip, sys.stdin)
    ]

    log("Solving problems")
    print(
        "\n"
        + tabulate.tabulate(
            (
                (
                    len(data),
                    part_one(data),
                    part_two(data),
                ),
            ),
            headers=(
                "Data size",
                "Sum of priorities (pt 1)",
                "3 elf priorities (pt 2)",
            ),
            tablefmt="grid",
        )
    )

    return 0


if __name__ == "__main__":
    assert main.__annotations__.get("return") is int, "main() should return an integer"

    filter_warnings("error", category=Warning)
    sys.exit(main())
