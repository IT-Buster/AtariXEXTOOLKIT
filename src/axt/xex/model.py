from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Segment:
    """Represents a single XEX segment."""

    start: int
    end: int
    data: bytes

    @property
    def size(self) -> int:
        return self.end - self.start + 1


@dataclass(slots=True)
class XexFile:
    """Represents a parsed Atari executable."""

    segments: list[Segment] = field(default_factory=list)
    run_address: int | None = None
    init_address: int | None = None

    @property
    def segment_count(self) -> int:
        return len(self.segments)

    @property
    def total_data_size(self) -> int:
        return sum(segment.size for segment in self.segments)