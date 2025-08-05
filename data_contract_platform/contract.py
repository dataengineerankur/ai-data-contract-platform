"""Data contract definitions for the AI-powered data contract platform."""

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class DataContract:
    """Represents a simple data contract between producer and consumer.

    The contract specifies expected columns and their data types.
    """
    columns: Dict[str, str] = field(default_factory=dict)

    def __str__(self) -> str:
        lines = [f"{col}: {dtype}" for col, dtype in self.columns.items()]
        return "DataContract(columns=\n  " + "\n  ".join(lines) + ")"
