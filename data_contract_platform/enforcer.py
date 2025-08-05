"""Contract enforcer that checks producer schema against the data contract and suggests actions."""

from typing import Dict, Any, List

from .contract import DataContract


class ContractEnforcer:
    """Checks compliance of producer schema with a contract and suggests fixes."""

    def enforce(
        self,
        contract: DataContract,
        producer_schema: Dict[str, Any],
        consumer_requirements: Dict[str, Any],
    ) -> List[str]:
        """Validate the producer schema against the data contract and consumer requirements.

        Args:
            contract: The DataContract defining agreed-upon columns and types.
            producer_schema: Producer's actual schema (contains 'columns' dict).
            consumer_requirements: Consumer's required and optional columns dicts.

        Returns:
            A list of human-readable issue descriptions indicating mismatches or missing columns.
        """
        issues: List[str] = []
        producer_cols = producer_schema.get("columns", {})
        # Check for missing required columns specified by consumer
        req_cols = consumer_requirements.get("required_columns", {})
        for col, dtype in req_cols.items():
            if col not in producer_cols:
                issues.append(f"Producer missing required column '{col}' of type '{dtype}'.")
        # Check for type mismatches based on the contract
        for col, contract_type in contract.columns.items():
            if col in producer_cols:
                prod_type = producer_cols[col]
                if prod_type != contract_type:
                    issues.append(
                        f"Column '{col}' type mismatch: producer '{prod_type}', contract '{contract_type}'."
                    )
        return issues
