from typing import Optional, Tuple

ACCOUNT_STORAGE_OVERHEAD: int
DEFAULT_BURN_PERCENT: int
DEFAULT_EXEMPTION_THRESHOLD: float
DEFAULT_LAMPORTS_PER_BYTE_YEAR: int

class Rent:
    @property
    def burn_percent(self) -> int: ...
    @property
    def exemption_threshold(self) -> float: ...
    @property
    def lamports_per_byte_year(self) -> int: ...
    def __init__(
        self, burn_percent: int, exemption_threshold: float, lamports_per_byte_year: int
    ) -> None: ...
    def calculate_burn(self, rent_collected: int) -> Tuple[int, int]: ...
    @staticmethod
    def default() -> "Rent": ...
    def due(
        self, balance: int, data_len: int, years_elapsed: float
    ) -> Optional[int]: ...
    def due_amount(self, data_len: int, years_elapsed: float) -> int: ...
    @staticmethod
    def free() -> "Rent": ...
    @staticmethod
    def from_bytes(raw_bytes: bytes) -> "Rent": ...
    @staticmethod
    def from_json(raw: str) -> "Rent": ...
    def is_exempt(self, balance: int, data_len: int) -> bool: ...
    def minimum_balance(self, data_len: int) -> int: ...
    def to_json(self) -> str: ...
    def with_slots_per_epoch(self, slots_per_epoch: int) -> "Rent": ...
    def __bytes__(self) -> bytes: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __richcmp__(self, other: "Rent", op: int) -> bool: ...