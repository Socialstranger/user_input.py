from collections.abc import Callable

from ._pygit2 import FilterSource

class Filter:
    attributes: str
    @classmethod
    def nattrs(cls) -> int: ...
    def check(self, src: FilterSource, attr_values: list[str | None]) -> None: ...
    def write(self, data: bytes, src: FilterSource, write_next: Callable[[bytes], None]) -> None: ...
    def close(self, write_next: Callable[[bytes], None]) -> None: ...
