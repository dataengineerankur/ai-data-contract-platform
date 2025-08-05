"""Contract generator that builds a data contract from producer schema and consumer requirements."""

from typing import Dict, Any

from .contract import DataContract


class ContractGenerator:
    """Generates a data contract based on producer schema and consumer requirements."""

    def generate(self, producer_schema: Dict[str, Any], consumer_requirements: Dict[str, Any]) -> DataContract:
        """Generate a DataContract instance based on producer schema and consumer requirements.

        Args:
            producer_schema: A dict with key 'columns' mapping column names to their data types.
            consumer_requirements: A dict with keys 'required_columns' and optional 'optional_columns', both mapping column names to desired types.

        Returns:
            A DataContract representing the agreed-upon schema.
        """
        contract_columns: Dict[str, str] = {}
        # Handle required columns from consumer
        req_cols = consumer_requirements.get("required_columns", {})
        for col, dtype in req_cols.items():
            # Use producer's type if producer has it, otherwise consumer's suggested type
            if producer_schema.get("columns") and col in producer_schema["columns"]:
                contract_columns[col] = producer_schema["columns"][col]
            else:
                contract_columns[col] = dtype
        # Handle optional columns from consumer
        opt_cols = consumer_requirements.get("optional_columns", {})
        for col, dtype in opt_cols.items():
            if producer_schema.get("columns") and col in producer_schema["columns"]:
                contract_columns.setdefault(col, producer_schema["columns"][col])
            else:
                contract_columns.setdefault(col, dtype)
        # Include remaining producer columns
        for col, dtype in producer_schema.get("columns", {}).items():
            contract_columns.setdefault(col, dtype)
        return DataContract(columns=contract_columns)
