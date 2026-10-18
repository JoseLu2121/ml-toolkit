from dataclasses import dataclass, replace, asdict, fields, field
from typing import Any, Self
import json
from pathlib import Path

@dataclass(slots=True, frozen=True, order=True)
class ExperimentConfig:

    name: str = field(compare=False)
    lr: float = 0.1
    batch_size: int = 64
    epochs: int = 10
    seed: int | None = field(compare=False, default=None)
    tags: tuple[str, ...] = field(compare=False, default=())

    def __post_init__(self) -> None:
        if self.name == "":
            raise ValueError("name cannot be empty")
        if self.lr <= 0.0:
            raise ValueError("lr cannot be negative or zero")
        if self.epochs <= 0:
            raise ValueError("epochs cannot be negative or zero")
        if self.batch_size <= 0:
            raise ValueError("batch size cannot be negative or zero")
        if self.batch_size & (self.batch_size - 1) != 0:
            raise ValueError("batch size must be power of two")

    def with_overrides(self, **kwargs: Any) -> Self:
        return replace(self, **kwargs)

    def to_json(self, path: str) -> None:
        if Path(path).suffix != ".json":
            raise ValueError("Path must end in json")

        d: dict = asdict(self)

        with open(path, "w") as f:
            f.write(json.dumps(d, indent=4))

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> Self:
        valid_names = { f.name for f in fields(cls)}
        filtered_names = { k: v for k,v in d.items() if k in valid_names}

        if "tags" in filtered_names:
            filtered_names["tags"] = tuple(filtered_names["tags"])

        return cls(**filtered_names)



    

