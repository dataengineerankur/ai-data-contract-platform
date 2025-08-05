"""Data contract agent orchestrating generation, enforcement and communication."""

import json
from pathlib import Path
from typing import Any, Dict

from .contract import DataContract
from .generator import ContractGenerator
from .enforcer import ContractEnforcer
from .communicator import Communicator


class DataContractAgent:
    """Agent that orchestrates contract generation, enforcement and communication."""

    def __init__(self, generator: ContractGenerator, enforcer: ContractEnforcer, communicator: Communicator) -> None:
        self.generator = generator
        self.enforcer = enforcer
        self.communicator = communicator

    def run(self, producer_schema_path: str, consumer_requirements_path: str):
        """Load schemas and run generation/enforcement workflow."""
        with open(producer_schema_path, "r") as f:
            producer_schema = json.load(f)
        with open(consumer_requirements_path, "r") as f:
            consumer_req = json.load(f)
        # Generate contract
        contract = self.generator.generate(producer_schema, consumer_req)
        # Enforce contract and get issues
        issues = self.enforcer.enforce(contract, producer_schema, consumer_req)
        # Communicate results
        self.communicator.notify(contract, issues)
        return contract, issues


if __name__ == "__main__":
    # Example usage
    generator = ContractGenerator()
    enforcer = ContractEnforcer()
    communicator = Communicator()
    agent = DataContractAgent(generator, enforcer, communicator)
    project_root = Path(__file__).resolve().parents[1]
    producer_schema_path = project_root / "sample_data" / "producer_schema.json"
    consumer_requirements_path = project_root / "sample_data" / "consumer_requirements.json"
    contract, issues = agent.run(str(producer_schema_path), str(consumer_requirements_path))
    print("Generated contract:")
    print(contract)
    print("\nIssues:")
    for issue in issues:
        print("-", issue)
