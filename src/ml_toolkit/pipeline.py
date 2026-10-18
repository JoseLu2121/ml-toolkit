import csv
import random
from collections.abc import Iterator
from pathlib import Path


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

