"""
ScopeGuard: Module proxy pointing to core main.py implementation
"""

import sys
from pathlib import Path

# Ensure parent directory is on sys.path for direct script execution
_parent_dir = str(Path(__file__).resolve().parent.parent)
if _parent_dir not in sys.path:
    sys.path.insert(0, _parent_dir)

from main import (
    app,
    AuditRequest,
    CombinedAuditResponse,
    FlaggedCreepItem,
    GemmaAuditOutput,
    TabPFNRiskOutput,
    TabularRiskInput,
    UnitEconomicsTelemetry,
    TraceMetadata,
    tabpfn_engine,
    ollama_client,
)

__all__ = [
    "app",
    "AuditRequest",
    "CombinedAuditResponse",
    "FlaggedCreepItem",
    "GemmaAuditOutput",
    "TabPFNRiskOutput",
    "TabularRiskInput",
    "UnitEconomicsTelemetry",
    "TraceMetadata",
    "tabpfn_engine",
    "ollama_client",
]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
