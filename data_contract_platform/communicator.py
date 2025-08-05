"""Communicator module for the AI data contract platform.

This module defines a Communicator class that notifies producers and consumers
about generated data contracts and any contract enforcement issues. In a real
implementation, this might integrate with Slack, Jira, or email APIs. Here,
we simply print messages to the console.
"""

from __future__ import annotations

from dataclasses import dataclass

class Communicator:
    """Simple communicator to display contract and enforcement issues."""

    def notify_contract(self, contract) -> None:
        """Notify producers/consumers about the generated contract.

        Args:
            contract: DataContract object containing columns and types.
        """
        print("Generated Data Contract:\n")
        for column, dtype in contract.columns.items():
            print(f"- {column}: {dtype}")
        print()

    def notify_issues(self, issues: list[str]) -> None:
        """Notify producers/consumers about contract enforcement issues.

        Args:
            issues: List of human-readable issue descriptions.
        """
        if not issues:
            print("All data conforms to the contract!\n")
            return
        print("Contract Enforcement Issues:\n")
        for issue in issues:
            print(f"- {issue}")
        print()
