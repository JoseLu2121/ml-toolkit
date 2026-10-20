import csv
import random
from collections.abc import Iterator
from pathlib import Path
from typing import Iterable

def rows_generator(n: int, feats: int, seed: int | None, debug: bool = False) -> Iterator:
    counter: int = 0
    r = random.Random(seed)
    while counter < n:
        row: list = [counter] + [ r.random() for _ in range(feats)]
        row.append(r.randint(0,1))
        if debug:
            print(str(row))
        yield row
        counter += 1


def generate_fake_csv(n: int, path: str, feats: int, seed: int | None, debug: bool = False) -> None:
    if Path(path).suffix != ".csv":
        raise ValueError("Path must end in .csv")

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows_generator(n, feats, seed, debug))

def read_csv(path: str, splitter: str = ",") -> Iterator[str, str]:
    if Path(path).suffix != ".csv":
        raise ValueError("Path must end in .csv")

    with open(path, "r") as f:
        header_row: str | None = next(f, None)
        if header_row is None:
            return

        clean_header = header_row.strip().removesuffix("\n")
        splitted_header: list[str] = clean_header.split(splitter)

        for line in f:
            splitted_line: list[str] = line.strip().split(splitter)
            zipped = dict(zip(splitted_header, splitted_line))
            yield zipped



