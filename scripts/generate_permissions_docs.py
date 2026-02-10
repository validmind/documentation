#!/usr/bin/env python3
"""
Generate permissions documentation from backend source files.

This script reads the permission definitions from the backend repository
and generates Quarto markdown tables for the documentation.

Source files:
- backend/src/backend/templates/platform_resources/data.json
- backend/src/backend/templates/platform_resources/org_initials.json

Usage:
    python scripts/generate_permissions_docs.py

Output:
    site/guide/configuration/_permissions-generated.qmd
"""

import json
import os
import re
from pathlib import Path
from typing import Any

# Paths relative to documentation repo root
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
BACKEND_ROOT = REPO_ROOT.parent / "backend"

DATA_JSON = BACKEND_ROOT / "src/backend/templates/platform_resources/data.json"
ROLES_JSON = BACKEND_ROOT / "src/backend/templates/platform_resources/org_initials.json"
OUTPUT_FILE = REPO_ROOT / "site/guide/configuration/_permissions-generated.qmd"

# UI terminology mapping (Finding -> Artifact)
TERMINOLOGY_MAP = {
    "Finding": "Artifact",
    "finding": "artifact",
}


def format_action_name(action_id: str, action_name: str | None = None) -> str:
    """Format action ID into human-readable name."""
    # Use provided name if available
    if action_name:
        name = action_name
    else:
        name = action_id
    
    # Remove common prefixes
    for prefix in ["read_", "create_", "update_", "delete_", "add_", "manage_"]:
        if name.startswith(prefix):
            name = name[len(prefix):]
            break
    
    # Replace underscores with spaces
    name = name.replace("_", " ")
    
    # Capitalize first letter of each word
    name = " ".join(word.capitalize() for word in name.split())
    
    # Apply terminology mapping
    for old, new in TERMINOLOGY_MAP.items():
        name = name.replace(old, new)
    
    return name


def format_resource_name(name: str) -> str:
    """Format resource name for display."""
    # Apply terminology mapping
    for old, new in TERMINOLOGY_MAP.items():
        name = name.replace(old, new)
    return name


def get_action_display_name(action: dict) -> str:
    """Get display name for an action."""
    action_id = action.get("id", "")
    action_name = action.get("name", "")
    description = action.get("description", "")
    
    # Build display name from action name or ID
    if action_name and action_name not in ["read", "create", "update", "delete", "add"]:
        display = action_name.replace("_", " ").title()
    else:
        # Use action_id but format it nicely
        display = action_id.replace("_", " ").title()
    
    # Apply terminology mapping
    for old, new in TERMINOLOGY_MAP.items():
        display = display.replace(old, new)
    
    return display


def checkbox(checked: bool) -> str:
    """Return HTML checkbox markup."""
    if checked:
        return '<input type="checkbox" disabled checked />'
    return '<input type="checkbox" disabled />'


def load_json(path: Path) -> Any:
    """Load JSON file."""
    with open(path, "r") as f:
        return json.load(f)


def get_role_permissions(roles_data: dict) -> dict:
    """Extract permissions for each role."""
    defaults = roles_data.get("defaults", {})
    all_roles_perms = set(defaults.get("all_roles", []))
    model_scope_perms = set(defaults.get("model_scope_roles", []))
    
    role_perms = {}
    for role_name, role_data in roles_data.get("roles", {}).items():
        if role_name in ["Staff"]:  # Skip internal roles
            continue
        perms = set(role_data.get("permissions", []))
        scope = role_data.get("scope", "Organization")
        is_basic = role_data.get("is_basic_role", False)
        
        # Add default permissions
        if scope == "Organization":
            perms = perms.union(all_roles_perms)
        elif scope == "Model":
            perms = perms.union(model_scope_perms).union(all_roles_perms)
        
        role_perms[role_name] = {
            "permissions": perms,
            "scope": scope,
            "is_basic": is_basic,
        }
    
    return role_perms


def has_permission(role_perms: dict, role_name: str, action_id: str) -> bool:
    """Check if a role has a specific permission."""
    if role_name not in role_perms:
        return False
    
    perms = role_perms[role_name]["permissions"]
    
    # Direct match
    if action_id in perms:
        return True
    
    # Wildcard match (e.g., read_cf_* matches read_cf_anything)
    for perm in perms:
        if perm.endswith("*"):
            prefix = perm[:-1]
            if action_id.startswith(prefix):
                return True
    
    # Customer Admin has all permissions
    if role_name == "Customer Admin":
        return True
    
    return False


def generate_org_permissions_table(
    resources: list, role_perms: dict, org_roles: list
) -> str:
    """Generate markdown table for organization-level permissions."""
    lines = []
    
    for resource in resources:
        resource_id = resource.get("id", "")
        resource_name = format_resource_name(resource.get("name", resource_id))
        parent_id = resource.get("parent_id")
        actions = resource.get("actions", [])
        
        # Skip if no actions or if model-scoped
        if not actions or parent_id == "Model":
            continue
        
        # Skip internal resources
        if resource_id.startswith("dt_") or resource_id in ["WorkflowStatus"]:
            continue
        
        lines.append(f"\n#### {resource_name}\n")
        
        # Build header
        header = "| Permission |"
        sep = "|---|"
        for role in org_roles:
            header += f" {role} |"
            sep += ":---:|"
        lines.append(header)
        lines.append(sep)
        
        # Build rows
        for action in actions:
            action_id = action.get("id", "")
            is_visible = action.get("is_visible", True)
            if not is_visible:
                continue
            
            display_name = get_action_display_name(action)
            row = f"| {display_name} |"
            
            for role in org_roles:
                checked = has_permission(role_perms, role, action_id)
                row += f" {checkbox(checked)} |"
            
            lines.append(row)
        
        lines.append(f': **{resource_name}** permissions {{.hover tbl-colwidths="[40,20,20,20]"}}')
    
    return "\n".join(lines)


def generate_model_permissions_table(
    resources: list, role_perms: dict, model_roles: list
) -> str:
    """Generate markdown table for model-level permissions."""
    lines = []
    
    for resource in resources:
        resource_id = resource.get("id", "")
        resource_name = format_resource_name(resource.get("name", resource_id))
        parent_id = resource.get("parent_id")
        actions = resource.get("actions", [])
        
        # Only include model-scoped resources
        if parent_id != "Model" or not actions:
            continue
        
        # Skip dt_ resources (document types) - internal
        if resource_id.startswith("dt_"):
            continue
        
        lines.append(f"\n#### {resource_name}\n")
        
        # Build header
        header = "| Permission |"
        sep = "|---|"
        for role in model_roles:
            header += f" {role} |"
            sep += ":---:|"
        lines.append(header)
        lines.append(sep)
        
        # Build rows
        for action in actions:
            action_id = action.get("id", "")
            is_visible = action.get("is_visible", True)
            if not is_visible:
                continue
            
            display_name = get_action_display_name(action)
            row = f"| {display_name} |"
            
            for role in model_roles:
                checked = has_permission(role_perms, role, action_id)
                row += f" {checkbox(checked)} |"
            
            lines.append(row)
        
        lines.append(f': **{resource_name}** permissions {{.hover tbl-colwidths="[28,18,18,18,18]"}}')
    
    return "\n".join(lines)


def main():
    """Generate permissions documentation."""
    print(f"Loading {DATA_JSON}")
    resources = load_json(DATA_JSON)
    
    print(f"Loading {ROLES_JSON}")
    roles_data = load_json(ROLES_JSON)
    role_perms = get_role_permissions(roles_data)
    
    # Define role groups
    org_roles = ["Customer Admin", "Developer", "Validator"]
    model_roles = ["Model Owner", "Model Developer", "Model Validator", "Basic User"]
    
    # Generate output
    output = []
    
    output.append("""<!---
This file is auto-generated by scripts/generate_permissions_docs.py
Do not edit directly. Re-run the script to update.

Source files:
- backend/src/backend/templates/platform_resources/data.json
- backend/src/backend/templates/platform_resources/org_initials.json
--->

## Organization-level permissions

Organization-level permissions apply to all users in your organization based on their assigned role. These permissions control access to platform-wide settings and configurations.

::: {.callout-note}
The [{{< fa hand >}} Customer Admin]{.bubble} role has full access to all organization-level permissions and cannot be modified.
:::
""")
    
    output.append(generate_org_permissions_table(resources, role_perms, org_roles))
    
    output.append("""

## Model-level permissions

Model-level permissions control what users can do within the context of a specific model. Users are assigned model-level roles when they are added as stakeholders to a model.

::: {.callout-tip}
Model-level permissions are additive to organization-level permissions. A user with the Validator role at the organization level who is also assigned as Model Validator on a specific model will have both sets of permissions for that model.
:::
""")
    
    output.append(generate_model_permissions_table(resources, role_perms, model_roles))
    
    output.append("""

## Role descriptions

### Organization-level roles

| Role | Description |
|------|-------------|
| Customer Admin | Full administrative access to the organization. Can manage users, roles, and all settings. |
| Validator | Can create and manage models, templates, guidelines, and perform validation activities. |
| Developer | Can create models and view organization settings. Limited administrative access. |
| Basic User | Minimal permissions. Can only access models they are explicitly added to as stakeholders. |

### Model-level roles

| Role | Description |
|------|-------------|
| Model Owner | Full control over a specific model including deletion and stakeholder management. |
| Model Developer | Can edit model documentation and monitoring. |
| Model Validator | Can perform validation activities, add findings, and edit validation reports. |
: Role descriptions {.hover}
""")
    
    # Write output
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        f.write("\n".join(output))
    
    print(f"Generated {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
