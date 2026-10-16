"""
ScopeGuard: Local-First Scope Creep & Invoice Overrun Auditor
Open-Source AI Challenge - Week 2
"""

from .generate_demo_data import (
    get_historical_projects,
    get_historical_projects_csv,
    get_audit_scenarios,
    get_audit_scenario,
    get_tabular_inputs,
    generate_all_demo_data,
)

__all__ = [
    "get_historical_projects",
    "get_historical_projects_csv",
    "get_audit_scenarios",
    "get_audit_scenario",
    "get_tabular_inputs",
    "generate_all_demo_data",
]
