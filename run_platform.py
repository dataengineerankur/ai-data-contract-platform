#!/usr/bin/env python3
"""Entry point script for the AI data contract enforcement platform.

This script loads sample producer schema and consumer requirements from the
sample_data directory, generates a data contract, enforces it against the
producer schema, and uses the communicator to display the contract and
any enforcement issues.
"""
from __future__ import annotations

from pathlib import Path

from data_contract_platform.agent import DataContractAgent
from data_contract_platform.generator import ContractGenerator
from data_contract_platform.enforcer import ContractEnforcer
from data_contract_platform.communicator import Communicator


def main() -> None:
    """Run the data contract platform demo using sample data."""
    base_dir = Path(__file__).resolve().parent
    producer_schema_path = base_dir / "sample_data" / "producer_schema.json"
    consumer_requirements_path = base_dir / "sample_data" / "consumer_requirements.json"

    # Initialize components
    generator = ContractGenerator()
    enforcer = ContractEnforcer()
    communicator = Communicator()

    # Run the agent to generate and enforce the contract
    agent = DataContractAgent(generator, enforcer, communicator)
    agent.run(producer_schema_path, consumer_requirements_path)


if __name__ == "__main__":
    main()
