# Statement of Work (SOW): MetricFlow Analytics Dashboard

**Client:** MetricFlow Solutions, Inc.  
**Contractor:** ScopeGuard Engineering  
**Agreement Date:** September 14, 2026  
**Engagement Type:** 3-Stage Milestone Agreement  
**Agreed Total Budget:** $10,200.00 USD (120.0 agreed engineering hours)  
**Agreed Change-Order Hourly Rate:** $85.00 / hour  

---

### 1. Milestones & Project Deliverables
Contractor will develop a dedicated B2B telemetry metrics dashboard divided into three distinct milestone deliverables:

1. **Milestone 1 - Backend Aggregations (40 hrs):** FastAPI REST backend with endpoints returning pre-aggregated timeseries records (daily active users, telemetry event counts, and HTTP p99 response times) queried from TimescaleDB with 30-second Redis caching.
2. **Milestone 2 - Interactive Dashboard UI (50 hrs):** Single-tenant React analytics dashboard incorporating Recharts visualizations, date-range range picker, and dimensional metric filters.
3. **Milestone 3 - Snapshot Data Export (30 hrs):** Backend streaming CSV download utility allowing authenticated managers to export query results matching selected date windows.

---

### 2. Explicit Scope Exclusions
The following functionalities are **strictly excluded** from this agreement and require a formal Change Order billed at $85.00/hour:
- Real-time continuous WebSocket bidirectional event streaming (dashboard relies solely on 30-second interval polling).
- External CRM or marketing synchronization webhooks (e.g., HubSpot, Marketo, Salesforce).
- Granular Role-Based Access Control (RBAC) or multi-tenant organizational isolation (single organization tenant assumed).
- Automated scheduled PDF report compilation or email distribution.

---

### 3. Change Order Requirement
Any work outside Clauses 1.1-1.3 must be authorized under a countersigned Change Order prior to development.
Unilateral requests made via communication channels do not constitute an agreement to perform unpaid engineering.
