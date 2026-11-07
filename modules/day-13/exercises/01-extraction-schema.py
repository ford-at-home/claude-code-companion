"""
Exercise: Claims Extraction Schema
Day: 13 | Domain: D4
API Required: No

You are designing a JSON schema for extracting structured data from insurance
claims documents. The schema must be strict: true compatible and handle the
reality that not all fields are present in every document.

Instructions:
1. Implement `build_claims_schema` that returns a dict representing a JSON schema
2. Required fields (always present): claim_id (string), date_of_loss (string),
   policy_number (string)
3. Optional-but-typed fields: witness_name (string, may not exist in document)
4. Nullable fields: estimated_damage (number or null -- document may not have an estimate)
5. Enum-with-other: loss_type with values ["collision", "theft", "weather",
   "liability", "other"] PLUS a loss_type_detail field (string or null) for
   when loss_type is "other"
6. The schema must be compatible with strict: true (all properties listed,
   additionalProperties: false)

Hints:
- Nullable = ["number", "null"] -- Claude can honestly return null when data is missing
- Optional fields in strict mode: include them in "required" but make them nullable
  (strict: true requires all properties in "required")
- enum-with-other: the detail field should be nullable (null when loss_type != "other")
- additionalProperties must be false for strict: true compatibility
"""

from typing import Any


def build_claims_schema() -> dict[str, Any]:
    """
    Build a JSON schema for insurance claims extraction.

    Returns:
        A dict representing a JSON schema that is strict: true compatible.
        Must include required fields, nullable fields, and enum-with-other pattern.
    """
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

schema = build_claims_schema()
assert isinstance(schema, dict), f"Expected dict, got {type(schema)}"

# Verify it's a proper JSON schema
assert schema.get("type") == "object", "Schema must be type 'object'"
assert "properties" in schema, "Schema must have 'properties'"
assert "required" in schema, "Schema must have 'required'"

props = schema["properties"]

# Verify required fields exist
for field in ["claim_id", "date_of_loss", "policy_number"]:
    assert field in props, f"Missing required field: {field}"
    assert field in schema["required"], f"{field} must be in 'required' array"

# Verify nullable field
assert "estimated_damage" in props, "Missing nullable field: estimated_damage"
damage_type = props["estimated_damage"].get("type")
assert isinstance(damage_type, list) and "null" in damage_type, \
    "estimated_damage must be nullable (type should include 'null')"

# Verify witness_name exists
assert "witness_name" in props, "Missing field: witness_name"

# Verify enum-with-other pattern
assert "loss_type" in props, "Missing enum field: loss_type"
assert "enum" in props["loss_type"], "loss_type must have an enum"
assert "other" in props["loss_type"]["enum"], "loss_type enum must include 'other'"
assert "loss_type_detail" in props, "Missing detail field: loss_type_detail"

# Verify strict: true compatibility
assert schema.get("additionalProperties") is False, \
    "Schema must have additionalProperties: false for strict: true"

# Verify all properties are in required (strict mode requirement)
for prop_name in props:
    assert prop_name in schema["required"], \
        f"In strict mode, all properties must be in 'required'. Missing: {prop_name}"

print("All structural checks passed.")
