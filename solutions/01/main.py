#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC 2022 -- day 1"""


import sys
from warnings import filterwarnings as filter_warnings

import tabulate  # type: ignore


def log(msg: str) -> None:
    print(f" \033[1m\033[32m*\033[0m {msg}")


def part_one(data: list[int]) -> int:
    return data[-1]


def part_two(data: list[int]) -> int:
    return sum(data[-3:])


def main() -> int:
    """Entry/main function"""

    log("Reading data from stdin")
    data: list[int] = []
    tmp: int = 0

    for line in sys.stdin:
        if line.strip():
            tmp += int(line)
        else:
            data.append(tmp)
            tmp = 0

    data.append(tmp)

    log("Preparing data")
    data = sorted(data)

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
                "Cals top (pt 1)",
                "Cals top 3 (pt 2)",
            ),
            tablefmt="grid",
        )
    )

    return 0


if __name__ == "__main__":
    assert main.__annotations__.get("return") is int, "main() should return an integer"

    filter_warnings("error", category=Warning)
    sys.exit(main())
