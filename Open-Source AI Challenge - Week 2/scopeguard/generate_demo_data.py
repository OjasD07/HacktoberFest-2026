"""
ScopeGuard Demo Data Generator
==============================
Deterministic, local-first utility for generating realistic freelance software audit datasets.

Generates:
1. Historical Freelance Projects CSV (historical_projects.csv):
   Exactly 36 past projects designed for Prior Labs' TabPFN foundation model classification.
2. Three Pre-Built Audit Scenarios (Low Risk, Moderate Gray-Area, Severe Scope Creep):
   - Signed Statement of Work (SOW) in Markdown with deliverables and exclusions
   - Raw Git commit log dump (8-12 commits mixing scope with unapproved additions)
   - Raw Slack/WhatsApp client chat transcript
   - Pre-filled numerical tabular inputs matching TabPFN features
"""

import csv
import io
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

# Seed constant for strict determinism and reproducibility
RANDOM_SEED: int = 42

# ---------------------------------------------------------------------------
# 1. Historical Freelance Projects (36 Records for TabPFN Small-Data Training)
# ---------------------------------------------------------------------------
# Feature schema:
#   agreed_hours: float (20.0 - 200.0)
#   unplanned_commits: int (0 - 45)
#   chat_requests: int (1 - 60)
#   revision_rounds: int (1 - 8)
#   client_retainer_type: int (0: Fixed-Price, 1: Milestone, 2: Hourly Retainer)
# Target schema:
#   overrun_or_dispute: int (0: On-Budget/Smooth, 1: Budget Overrun or Invoice Dispute)
HISTORICAL_PROJECTS_DATA: List[Dict[str, Any]] = [
    # --- 18 On-Budget / Smooth Projects (Target = 0) ---
    {
        "project_name": "Artisan Coffee Roasters Storefront MVP",
        "agreed_hours": 80.0,
        "unplanned_commits": 2,
        "chat_requests": 6,
        "revision_rounds": 1,
        "client_retainer_type": 0,
        "overrun_or_dispute": 0,
    },
    {
        "project_name": "Boutique Architecture Portfolio",
        "agreed_hours": 40.0,
        "unplanned_commits": 1,
        "chat_requests": 4,
        "revision_rounds": 1,
        "client_retainer_type": 0,
        "overrun_or_dispute": 0,
    },
    {
        "project_name": "B2B SaaS Onboarding Tour",
        "agreed_hours": 60.0,
        "unplanned_commits": 3,
        "chat_requests": 8,
        "revision_rounds": 2,
        "client_retainer_type": 1,
        "overrun_or_dispute": 0,
    },
    {
        "project_name": "FinTech Developer Docs & API Sandbox",
        "agreed_hours": 120.0,
        "unplanned_commits": 4,
        "chat_requests": 11,
        "revision_rounds": 2,
        "client_retainer_type": 1,
        "overrun_or_dispute": 0,
    },
    {
        "project_name": "Mobile Logistics Driver Telemetry",
        "agreed_hours": 160.0,
        "unplanned_commits": 6,
        "chat_requests": 15,
        "revision_rounds": 2,
        "client_retainer_type": 2,
        "overrun_or_dispute": 0,
    },
    {
        "project_name": "Cybersecurity Landing Page Refresh",
        "agreed_hours": 35.0,
        "unplanned_commits": 0,
        "chat_requests": 3,
        "revision_rounds": 1,
        "client_retainer_type": 0,
        "overrun_or_dispute": 0,
    },
    {
        "project_name": "DevOps Terraform Cloud Setup",
        "agreed_hours": 90.0,
        "unplanned_commits": 5,
        "chat_requests": 12,
        "revision_rounds": 2,
        "client_retainer_type": 2,
        "overrun_or_dispute": 0,
    },
    {
        "project_name": "Warehouse Inventory Barcode Scanner",
        "agreed_hours": 150.0,
        "unplanned_commits": 7,
        "chat_requests": 18,
        "revision_rounds": 2,
        "client_retainer_type": 1,
        "overrun_or_dispute": 0,
    },
    {
        "project_name": "Stripe Hosted Checkout Integration",
        "agreed_hours": 50.0,
        "unplanned_commits": 1,
        "chat_requests": 5,
        "revision_rounds": 1,
        "client_retainer_type": 0,
        "overrun_or_dispute": 0,
    },
    {
        "project_name": "Next.js Core Web Vitals Optimization",
        "agreed_hours": 110.0,
        "unplanned_commits": 8,
        "chat_requests": 14,
        "revision_rounds": 2,
        "client_retainer_type": 2,
        "overrun_or_dispute": 0,
    },
    {
        "project_name": "Marketing Automation Webhook Relay",
        "agreed_hours": 45.0,
        "unplanned_commits": 2,
        "chat_requests": 7,
        "revision_rounds": 1,
        "client_retainer_type": 1,
        "overrun_or_dispute": 0,
    },
    {
        "project_name": "Snowflake Analytics Ingestion Pipeline",
        "agreed_hours": 130.0,
        "unplanned_commits": 9,
        "chat_requests": 16,
        "revision_rounds": 3,
        "client_retainer_type": 2,
        "overrun_or_dispute": 0,
    },
    {
        "project_name": "Supabase RBAC Auth Migration",
        "agreed_hours": 75.0,
        "unplanned_commits": 3,
        "chat_requests": 10,
        "revision_rounds": 2,
        "client_retainer_type": 0,
        "overrun_or_dispute": 0,
    },
    {
        "project_name": "Micro-Agency Client Portal Phase 1",
        "agreed_hours": 180.0,
        "unplanned_commits": 12,
        "chat_requests": 20,
        "revision_rounds": 3,
        "client_retainer_type": 2,
        "overrun_or_dispute": 0,
    },
    {
        "project_name": "React Component Library Bugfix Sprint",
        "agreed_hours": 25.0,
        "unplanned_commits": 0,
        "chat_requests": 2,
        "revision_rounds": 1,
        "client_retainer_type": 0,
        "overrun_or_dispute": 0,
    },
    {
        "project_name": "GraphQL Mobile BFF Gateway",
        "agreed_hours": 95.0,
        "unplanned_commits": 6,
        "chat_requests": 13,
        "revision_rounds": 2,
        "client_retainer_type": 1,
        "overrun_or_dispute": 0,
    },
    {
        "project_name": "Postgres Read-Replica Sharding",
        "agreed_hours": 140.0,
        "unplanned_commits": 10,
        "chat_requests": 19,
        "revision_rounds": 3,
        "client_retainer_type": 2,
        "overrun_or_dispute": 0,
    },
    {
        "project_name": "Shopify Liquid Theme Redesign",
        "agreed_hours": 65.0,
        "unplanned_commits": 4,
        "chat_requests": 9,
        "revision_rounds": 2,
        "client_retainer_type": 0,
        "overrun_or_dispute": 0,
    },
    # --- 18 Overrun / Disputed Projects (Target = 1) ---
    {
        "project_name": "Digital Creator Marketplace -> FinTech Platform",
        "agreed_hours": 90.0,
        "unplanned_commits": 38,
        "chat_requests": 54,
        "revision_rounds": 7,
        "client_retainer_type": 0,
        "overrun_or_dispute": 1,
    },
    {
        "project_name": "B2B Analytics Dashboard with Creeping Webhooks",
        "agreed_hours": 120.0,
        "unplanned_commits": 14,
        "chat_requests": 28,
        "revision_rounds": 4,
        "client_retainer_type": 1,
        "overrun_or_dispute": 1,
    },
    {
        "project_name": "Healthcare Telehealth MVP Scope Explosion",
        "agreed_hours": 50.0,
        "unplanned_commits": 22,
        "chat_requests": 35,
        "revision_rounds": 5,
        "client_retainer_type": 0,
        "overrun_or_dispute": 1,
    },
    {
        "project_name": "Fitness Tracking App with Crypto Wallet Creep",
        "agreed_hours": 70.0,
        "unplanned_commits": 29,
        "chat_requests": 42,
        "revision_rounds": 6,
        "client_retainer_type": 0,
        "overrun_or_dispute": 1,
    },
    {
        "project_name": "Enterprise Procurement Milestone Stalemate",
        "agreed_hours": 160.0,
        "unplanned_commits": 32,
        "chat_requests": 48,
        "revision_rounds": 6,
        "client_retainer_type": 1,
        "overrun_or_dispute": 1,
    },
    {
        "project_name": "SaaS Marketing Site Quadruple Redesign",
        "agreed_hours": 30.0,
        "unplanned_commits": 15,
        "chat_requests": 24,
        "revision_rounds": 4,
        "client_retainer_type": 0,
        "overrun_or_dispute": 1,
    },
    {
        "project_name": "Custom Shopify App Forced ERP Sync",
        "agreed_hours": 85.0,
        "unplanned_commits": 26,
        "chat_requests": 39,
        "revision_rounds": 5,
        "client_retainer_type": 0,
        "overrun_or_dispute": 1,
    },
    {
        "project_name": "Clinical Trial Portal Milestone Dispute",
        "agreed_hours": 140.0,
        "unplanned_commits": 34,
        "chat_requests": 52,
        "revision_rounds": 7,
        "client_retainer_type": 1,
        "overrun_or_dispute": 1,
    },
    {
        "project_name": "Fleet Dispatch Map Routing Scope Swell",
        "agreed_hours": 110.0,
        "unplanned_commits": 28,
        "chat_requests": 45,
        "revision_rounds": 6,
        "client_retainer_type": 0,
        "overrun_or_dispute": 1,
    },
    {
        "project_name": "Web Scraping Service Anti-Bot Creep",
        "agreed_hours": 45.0,
        "unplanned_commits": 18,
        "chat_requests": 31,
        "revision_rounds": 4,
        "client_retainer_type": 0,
        "overrun_or_dispute": 1,
    },
    {
        "project_name": "Hourly Retainer Bill Shock & Refusal to Pay",
        "agreed_hours": 175.0,
        "unplanned_commits": 41,
        "chat_requests": 58,
        "revision_rounds": 8,
        "client_retainer_type": 2,
        "overrun_or_dispute": 1,
    },
    {
        "project_name": "Support Bot Demanding Custom Fine-Tuning",
        "agreed_hours": 60.0,
        "unplanned_commits": 24,
        "chat_requests": 37,
        "revision_rounds": 5,
        "client_retainer_type": 0,
        "overrun_or_dispute": 1,
    },
    {
        "project_name": "FinTech Reconciliation Milestone Blocked",
        "agreed_hours": 130.0,
        "unplanned_commits": 30,
        "chat_requests": 44,
        "revision_rounds": 6,
        "client_retainer_type": 1,
        "overrun_or_dispute": 1,
    },
    {
        "project_name": "Real Estate Listing Portal Forced CRM Addition",
        "agreed_hours": 80.0,
        "unplanned_commits": 27,
        "chat_requests": 40,
        "revision_rounds": 5,
        "client_retainer_type": 0,
        "overrun_or_dispute": 1,
    },
    {
        "project_name": "Doctor Booking System Timezone Calamity",
        "agreed_hours": 100.0,
        "unplanned_commits": 31,
        "chat_requests": 49,
        "revision_rounds": 7,
        "client_retainer_type": 0,
        "overrun_or_dispute": 1,
    },
    {
        "project_name": "EdTech Video Course Platform Milestone Void",
        "agreed_hours": 155.0,
        "unplanned_commits": 36,
        "chat_requests": 55,
        "revision_rounds": 7,
        "client_retainer_type": 1,
        "overrun_or_dispute": 1,
    },
    {
        "project_name": "Subcription Paywall Custom Tier Explosion",
        "agreed_hours": 40.0,
        "unplanned_commits": 19,
        "chat_requests": 33,
        "revision_rounds": 4,
        "client_retainer_type": 0,
        "overrun_or_dispute": 1,
    },
    {
        "project_name": "Legacy Migration Retainer Runaway Hours Dispute",
        "agreed_hours": 190.0,
        "unplanned_commits": 43,
        "chat_requests": 60,
        "revision_rounds": 8,
        "client_retainer_type": 2,
        "overrun_or_dispute": 1,
    },
]

# Strict verification of row count for small-data TabPFN inference
assert (
    len(HISTORICAL_PROJECTS_DATA) == 36
), f"Expected exactly 36 historical projects, got {len(HISTORICAL_PROJECTS_DATA)}"

# ---------------------------------------------------------------------------
# 2. Three Pre-Built Audit Scenarios (SOW, Git Logs, Chat Transcripts, Inputs)
# ---------------------------------------------------------------------------

SCENARIOS: Dict[str, Dict[str, Any]] = {
    "low_risk": {
        "id": "low_risk",
        "title": "Low Risk: E-Commerce Storefront MVP",
        "client_name": "Artisan Brew Co.",
        "risk_level": "low",
        "tabular_inputs": {
            "agreed_hours": 80.0,
            "unplanned_commits": 2,
            "chat_requests": 6,
            "revision_rounds": 1,
            "client_retainer_type": 0,  # Fixed-Price
        },
        "sow_markdown": """# Statement of Work (SOW): Artisan Brew Co. Storefront MVP

**Client:** Artisan Brew Co., LLC  
**Contractor:** ScopeGuard Solutions / Freelance Engineering  
**Agreement Date:** October 2, 2026  
**Engagement Type:** Fixed-Price Milestone  
**Agreed Total Budget:** $6,800.00 USD (80.0 agreed engineering hours)  
**Agreed Change-Order Hourly Rate:** $85.00 / hour  

---

### 1. Project Overview & Deliverables
The Contractor agrees to design and engineer a lightweight, headless direct-to-consumer web storefront for Artisan Brew Co. Deliverables are strictly limited to the following:

1. **Responsive Next.js Frontend:** Single-page catalog and dedicated product detail page (PDP) built with Next.js 14 App Router and styled with Tailwind CSS.
2. **Slide-Out Cart Drawer:** In-memory and localStorage client cart drawer with line item additions, quantity decrements, and calculated subtotal.
3. **Stripe Checkout Integration:** Standard server-side redirect to Stripe-hosted Checkout for one-time credit card processing and HTTPS success/cancellation redirect pages.
4. **Order Confirmation Webhook:** Signed Stripe webhook endpoint (`/api/webhooks/stripe`) writing completed orders into Supabase PostgreSQL and triggering transactional customer receipts via Resend.
5. **Headless CMS Connection:** Integration with Sanity CMS for product imagery, origin bean descriptions, and roast profiles.
6. **Production Deployment:** Deployment configuration to Vercel production with custom apex domain DNS records and SSL termination.

---

### 2. Explicit Scope Exclusions
The following capabilities are **explicitly excluded** from the fixed-price agreement and require a formal, signed Change Order billed at $85.00/hour:
- Recurring coffee bean subscription memberships or automated refill billing schedules.
- Multi-currency currency conversion or international tax calculation (handled solely by standard Stripe Checkout defaults).
- Custom warehouse inventory management system (WMS) or ERP synchronization.
- Native mobile iOS or Android application wrappers.
- Any manual graphic asset design, logo revisions, or copy photography creation.

---

### 3. Change-Order Policy & Commercial Terms
- All modifications or additions exceeding Clauses 1.1 through 1.6 must be requested in writing.
- Approved Change Orders will be executed at the agreed rate of **$85.00/hr**, invoiced weekly net-7.
- Contractor warrants 30 days of bug fixes following production sign-off.
""",
        "git_commit_log": """commit 7c4a1e9b21d5a83e04f9810427c3a01bf2801e91
Author: Alex Vance <alex@scopeguard.dev>
Date:   Mon Oct 5 09:30:14 2026 -0400

    feat(scaffold): initialize Next.js 14 project with Tailwind and TypeScript

commit 9f2b8d0e741c92a5b6f381029c7d410ae5729f2b
Author: Alex Vance <alex@scopeguard.dev>
Date:   Tue Oct 6 14:15:22 2026 -0400

    feat(catalog): build responsive product grid and category filter components

commit 1a8e4c2b90d7e63f51280a9c41f038d7e29a1a8e
Author: Alex Vance <alex@scopeguard.dev>
Date:   Wed Oct 7 11:42:09 2026 -0400

    feat(cart): implement slide-out cart drawer with localStorage persistence

commit 4e7d3f1a82c09b5e7301648d9a2f7c01b4e7d3f1
Author: Alex Vance <alex@scopeguard.dev>
Date:   Thu Oct 8 16:50:33 2026 -0400

    feat(stripe): add stripe checkout session creation api route

commit 6b0c2a8d39f1e74a5028914c6e3b0a7d9f6b0c2a
Author: Alex Vance <alex@scopeguard.dev>
Date:   Fri Oct 9 10:20:18 2026 -0400

    feat(webhooks): add stripe order fulfillment webhook and resend receipt dispatch

commit 3d9f1b4a70e82c6d5194820a3b7c91f0e43d9f1b
Author: Alex Vance <alex@scopeguard.dev>
Date:   Mon Oct 12 13:05:44 2026 -0400

    feat(cms): wire Sanity CMS schema for roast profiles and tasting notes

commit 8e2a7c5b4109d3e862f0174a9c5d3b1e708e2a7c
Author: Alex Vance <alex@scopeguard.dev>
Date:   Tue Oct 13 15:40:12 2026 -0400

    fix(mobile): resolve cart slide-in animation layout shift on Safari iOS

commit 5c1b9d3e802a4f7b91630d8c2e4f01a7b95c1b9d
Author: Alex Vance <alex@scopeguard.dev>
Date:   Wed Oct 14 17:10:05 2026 -0400

    perf(images): configure next/image avif and webp responsive breakpoints

commit 2f4e8a1c903b7d6e5210948a3c7f01e2b42f4e8a
Author: Alex Vance <alex@scopeguard.dev>
Date:   Thu Oct 15 11:00:27 2026 -0400

    chore(release): configure vercel production dns and security headers
""",
        "chat_transcript": """[2026-10-05 10:14] Marcus (Client): Morning Alex! Excited to kick this off. Contract is signed and deposit sent.
[2026-10-05 10:18] Alex (Dev): Received! Thanks Marcus. Starting on the Next.js scaffold and cart today.
[2026-10-08 14:22] Marcus (Client): Hey Alex, checked the preview link. The product cards look gorgeous.
[2026-10-08 14:25] Marcus (Client): Quick question: On the checkout page, could we change the button label from "Pay Now" to "Order Your Beans"?
[2026-10-08 14:31] Alex (Dev): Easy change, that's supported right in the Stripe Checkout config. Updated and deployed to staging.
[2026-10-14 16:02] Marcus (Client): Tested the webhook on staging with a test credit card, email confirmation landed in my inbox in 2 seconds.
[2026-10-15 11:30] Marcus (Client): Everything matches the SOW perfectly. Ready for production cutover tomorrow morning!
""",
    },
    "moderate_gray_area": {
        "id": "moderate_gray_area",
        "title": "Moderate Gray-Area: B2B Analytics Dashboard with Creeping Webhooks",
        "client_name": "MetricFlow Solutions",
        "risk_level": "moderate",
        "tabular_inputs": {
            "agreed_hours": 120.0,
            "unplanned_commits": 14,
            "chat_requests": 28,
            "revision_rounds": 4,
            "client_retainer_type": 1,  # Milestone
        },
        "sow_markdown": """# Statement of Work (SOW): MetricFlow Analytics Dashboard

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
""",
        "git_commit_log": """commit 3a1f9c0b284e71d5a60391824c7f01e9d3a1f9c0
Author: Alex Vance <alex@scopeguard.dev>
Date:   Mon Sep 21 10:14:02 2026 -0400

    feat(api): scaffold FastAPI timeseries query endpoints with 30s cache

commit 8d7e2b1a904f3c7e512806914a2f8c01b8d7e2b1
Author: Alex Vance <alex@scopeguard.dev>
Date:   Wed Sep 23 16:30:45 2026 -0400

    feat(dashboard): build executive metrics overview and Recharts latency charts

commit 2c4a9f6e8102b5d7a39401826f5d8e03a2c4a9f6
Author: Alex Vance <alex@scopeguard.dev>
Date:   Fri Sep 25 14:20:11 2026 -0400

    feat(export): implement streaming CSV download for telemetry records

commit 9b5e1d3a702c8f4e619028475a3b0c1e89b5e1d3
Author: Alex Vance <alex@scopeguard.dev>
Date:   Tue Sep 29 11:05:39 2026 -0400

    feat(hubspot): add unapproved hubspot webhook dispatcher for contact sync

commit 1f8a7c4b609e2d5a813047295c2f0a1e71f8a7c4
Author: Alex Vance <alex@scopeguard.dev>
Date:   Wed Sep 30 15:40:22 2026 -0400

    fix(hubspot): add exponential backoff for hubspot api rate limits (429)

commit 6e3c0d2a914f5b7e802914836a5c2f01d6e3c0d2
Author: Alex Vance <alex@scopeguard.dev>
Date:   Thu Oct 1 17:15:48 2026 -0400

    refactor(schema): add webhook_delivery_logs table and retry queue

commit 4b9a2e8c501f7d3a928041638e2b0a5f14b9a2e8
Author: Alex Vance <alex@scopeguard.dev>
Date:   Mon Oct 5 09:45:10 2026 -0400

    feat(filter): add multi-tag dimensional filtering to metric explorer

commit 7c1f8a0e492b6d5a810392847c5f0a2e97c1f8a0
Author: Alex Vance <alex@scopeguard.dev>
Date:   Wed Oct 7 13:20:00 2026 -0400

    style(nav): redesign navigation header per client slack feedback

commit 5e2b4d9a801c3f7e619204859a4b0c2e35e2b4d9
Author: Alex Vance <alex@scopeguard.dev>
Date:   Fri Oct 9 16:50:33 2026 -0400

    fix(auth): resolve token refresh loop on expired sessions

commit 0d8e1f5b729a4c6e801293847a5f2c01b0d8e1f5
Author: Alex Vance <alex@scopeguard.dev>
Date:   Mon Oct 12 11:15:20 2026 -0400

    chore(docker): configure staging docker-compose and environment secrets
""",
        "chat_transcript": """[2026-09-28 11:05] Dave (VP Sales): Hey Alex! Loved the staging demo.
[2026-09-28 11:07] Dave (VP Sales): Quick thought: when a customer has p99 latency spikes, my sales reps need that pushed into HubSpot as a contact note right away so we can upsell our enterprise tier.
[2026-09-28 11:12] Dave (VP Sales): It's just a simple webhook right? Should take like 10-15 minutes!
[2026-09-28 11:18] Alex (Dev): Hey Dave, third-party CRM webhooks like HubSpot were explicitly listed as out of scope in Section 2 of our SOW. We can certainly add it via a Change Order at $85/hr!
[2026-09-28 11:22] Dave (VP Sales): Come on man, we're already paying $10k. It's just an HTTP POST payload. We have an investor call on Thursday, don't nickel-and-dime us on a quick webhook.
[2026-09-29 18:30] Alex (Dev): I put together a preliminary webhook dispatcher, but HubSpot's API has strict 429 rate limits, so I had to add a retry queue and delivery log table.
[2026-10-02 09:15] Dave (VP Sales): Wait, why aren't custom HubSpot contact properties syncing? We need lifecycle stage and lead score updated too.
[2026-10-02 09:40] Alex (Dev): That requires custom property mapping and extra validation logic. This is already about 14 unplanned commits.
[2026-10-06 14:10] Dave (VP Sales): Let's sync on Milestone 2 sign-off. We can't approve Milestone 2 until the HubSpot sync works with all 12 custom properties.
""",
    },
    "severe_scope_creep": {
        "id": "severe_scope_creep",
        "title": "Severe Scope Creep: Creator Marketplace Turned FinTech Platform",
        "client_name": "IndieSpark Media",
        "risk_level": "severe",
        "tabular_inputs": {
            "agreed_hours": 90.0,
            "unplanned_commits": 38,
            "chat_requests": 54,
            "revision_rounds": 7,
            "client_retainer_type": 0,  # Fixed-Price
        },
        "sow_markdown": """# Statement of Work (SOW): IndieSpark Creator Download Catalog

**Client:** IndieSpark Media, LLC  
**Contractor:** ScopeGuard Engineering  
**Agreement Date:** August 10, 2026  
**Engagement Type:** Fixed-Price Contract  
**Agreed Total Budget:** $7,650.00 USD (90.0 agreed engineering hours)  
**Agreed Change-Order Hourly Rate:** $85.00 / hour  

---

### 1. Project Deliverables
Contractor agrees to deliver a simple, single-vendor digital asset marketplace where creators list PDF templates and digital assets:

1. **Digital Asset Catalog:** Public directory listing digital assets with thumbnail previews, tags, and category navigation.
2. **Platform Owner Stripe Account:** Single centralized Stripe account collecting customer payments. Platform owner manually reviews orders and distributes vendor earnings manually once a month via external PayPal batch transfers.
3. **Basic Authentication & Admin Panel:** Single admin role with username/password authentication to upload items, edit listings, and view total sales revenue.
4. **Secure Asset Storage:** AWS S3 presigned URL generation granting 15-minute expiring download links to verified purchasers.

---

### 2. Explicit Scope Exclusions
The following complex architectural items are **strictly excluded** from the fixed $7,650 fee:
- Automated multi-party split payouts or marketplace escrow (e.g., Stripe Connect custom/express accounts, split fee deductions, vendor 1099 tax compliance).
- Granular multi-tenant Role-Based Access Control (RBAC) with organizational hierarchies, team invites, and custom role permissions.
- Real-time customer messaging, dispute mediation desk, or automated refund balance clawbacks.
- Native mobile push notification servers or WebSocket connection hubs.

---

### 3. Change-Order Terms & Breach of Scope
Work performed beyond Clauses 1.1-1.4 must be authorized under an executed Change Order at **$85.00/hour**.
In the absence of a signed Change Order, unauthorized feature requests will either be declined or billed as invoice overruns at the agreed change-order rate.
""",
        "git_commit_log": """commit 1a4e9b8c702f3d5a619028475a3b0c1e81a4e9b8
Author: Alex Vance <alex@scopeguard.dev>
Date:   Mon Aug 17 09:20:14 2026 -0400

    feat(catalog): creator asset listing directory and search filters

commit 6f2c0d1a904b7e802914836a5c2f01d66f2c0d1a
Author: Alex Vance <alex@scopeguard.dev>
Date:   Wed Aug 19 14:15:30 2026 -0400

    feat(storage): implement S3 presigned download link generation

commit 9d8b3a7c501e2f4a813047295c2f0a1e79d8b3a7
Author: Alex Vance <alex@scopeguard.dev>
Date:   Fri Aug 21 17:00:22 2026 -0400

    feat(auth): basic JWT login and session cookies for admin

commit 4e1a7c5b609d2e5a813047295c2f0a1e74e1a7c5
Author: Alex Vance <alex@scopeguard.dev>
Date:   Tue Aug 25 11:30:19 2026 -0400

    feat(stripe-connect): integrate stripe connect custom onboarding flow (UNAPPROVED)

commit 8c3f2d9a914e5b7e802914836a5c2f01d8c3f2d9
Author: Alex Vance <alex@scopeguard.dev>
Date:   Thu Aug 27 16:45:02 2026 -0400

    feat(payouts): implement automated split payouts and fee deduction (UNAPPROVED)

commit 2b7e1a0c501f7d3a928041638e2b0a5f12b7e1a0
Author: Alex Vance <alex@scopeguard.dev>
Date:   Mon Aug 31 10:10:45 2026 -0400

    feat(rbac): implement 5-tier role-based access control engine (UNAPPROVED)

commit 0f9a4c8e492b6d5a810392847c5f0a2e90f9a4c8
Author: Alex Vance <alex@scopeguard.dev>
Date:   Wed Sep 2 15:35:10 2026 -0400

    refactor(db): migrate entire schema from single-tenant to multi-org tenancy (UNAPPROVED)

commit 5d2c8e1a801c3f7e619204859a4b0c2e35d2c8e1
Author: Alex Vance <alex@scopeguard.dev>
Date:   Fri Sep 4 18:20:00 2026 -0400

    feat(webhooks): handle account.updated and transfer.created webhooks (UNAPPROVED)

commit 3a8f1b6b729a4c6e801293847a5f2c01b3a8f1b6
Author: Alex Vance <alex@scopeguard.dev>
Date:   Tue Sep 8 13:40:15 2026 -0400

    fix(payouts): prevent negative balance clawback during partial refunds (UNAPPROVED)

commit 7e0d2c4e5102b5d7a39401826f5d8e03a7e0d2c4
Author: Alex Vance <alex@scopeguard.dev>
Date:   Thu Sep 10 16:15:29 2026 -0400

    feat(realtime): add websockets for instantaneous vendor balance alerts (UNAPPROVED)

commit 9c4b7a2a702c8f4e619028475a3b0c1e89c4b7a2
Author: Alex Vance <alex@scopeguard.dev>
Date:   Mon Sep 14 11:05:44 2026 -0400

    fix(security): patch privilege escalation in vendor team invite flow (UNAPPROVED)

commit 6b1e5d0a914f5b7e802914836a5c2f01d6b1e5d0
Author: Alex Vance <alex@scopeguard.dev>
Date:   Wed Sep 16 17:50:11 2026 -0400

    fix(db): repair broken migration locks caused by multi-tenant schema refactor
""",
        "chat_transcript": """[2026-08-24 23:42] Jason (Client): ALEX! EMERGENCY! Pick up your phone man!
[2026-08-24 23:45] Jason (Client): We just had dinner with an angel syndicate. They said single-account PayPal manual payout is a JOKE. We will never get funded.
[2026-08-24 23:46] Jason (Client): We MUST have full Stripe Connect Custom accounts where vendors onboard and get automated split payouts directly to their bank accounts!
[2026-08-25 08:30] Alex (Dev): Jason, Stripe Connect automated split payouts is a massive financial engine. Section 2 of our SOW literally specifies Stripe Connect and split payouts as explicit exclusions. Building that safely requires KYC verification, webhook listeners, negative balance handling, and at least 40+ hours of engineering.
[2026-08-25 08:34] Jason (Client): I know what the contract says, but this is the survival of our company! Just grind it out over the next few days. Don't worry about paperwork right now, I promise we'll take care of you once the round closes.
[2026-08-30 22:15] Jason (Client): Also we realized enterprise studios want to use this, so we can't just have one admin. We need Owner, Billing Manager, Product Lead, and Creator roles with distinct invite permissions.
[2026-09-03 14:20] Alex (Dev): That requires completely refactoring our database from single-tenant to multi-tenant organization keys. I am working 14-hour days here.
[2026-09-18 10:00] Alex (Dev): Jason, the platform with Stripe Connect and Multi-Tenant RBAC is deployed. Attached is the final invoice: $7,650 for base SOW + $6,460 (76 hours of Change Orders @ $85/hr for Stripe Connect, RBAC, WebSockets, and database migrations).
[2026-09-18 10:14] Jason (Client): Are you OUT OF YOUR MIND?! An extra $6,460?!
[2026-09-18 10:16] Jason (Client): The contract was FIXED-PRICE $7,650! Show me a single signed Change Order document! You never sent one for signature. I am NOT paying a single cent above $7,650. You can talk to my lawyer if you dispute this.
""",
    },
}

# ---------------------------------------------------------------------------
# 3. Public In-Memory Accessors & Export Helpers (No Disk Race Conditions)
# ---------------------------------------------------------------------------


def get_historical_projects() -> List[Dict[str, Any]]:
    """Return historical freelance projects in-memory as a list of dictionaries."""
    return [dict(p) for p in HISTORICAL_PROJECTS_DATA]


def get_historical_projects_csv() -> str:
    """Return historical freelance projects formatted as a deterministic CSV string."""
    output = io.StringIO()
    fieldnames = [
        "agreed_hours",
        "unplanned_commits",
        "chat_requests",
        "revision_rounds",
        "client_retainer_type",
        "overrun_or_dispute",
    ]
    writer = csv.DictWriter(output, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    for row in HISTORICAL_PROJECTS_DATA:
        writer.writerow(
            {
                "agreed_hours": f"{row['agreed_hours']:.1f}",
                "unplanned_commits": row["unplanned_commits"],
                "chat_requests": row["chat_requests"],
                "revision_rounds": row["revision_rounds"],
                "client_retainer_type": row["client_retainer_type"],
                "overrun_or_dispute": row["overrun_or_dispute"],
            }
        )
    return output.getvalue()


def get_audit_scenarios() -> Dict[str, Dict[str, Any]]:
    """Return all pre-built audit scenarios in-memory."""
    return {k: dict(v) for k, v in SCENARIOS.items()}


def get_audit_scenario(scenario_id: str) -> Dict[str, Any]:
    """Retrieve a single audit scenario by ID ('low_risk', 'moderate_gray_area', 'severe_scope_creep')."""
    if scenario_id not in SCENARIOS:
        raise KeyError(
            f"Scenario '{scenario_id}' not found. Available scenarios: {list(SCENARIOS.keys())}"
        )
    return dict(SCENARIOS[scenario_id])


def get_tabular_inputs(scenario_id: str) -> Dict[str, Any]:
    """Retrieve pre-filled TabPFN tabular inputs for a scenario."""
    scenario = get_audit_scenario(scenario_id)
    return dict(scenario["tabular_inputs"])


# ---------------------------------------------------------------------------
# 4. Standalone File Generator (Writes to demo_data/ subfolder)
# ---------------------------------------------------------------------------


def generate_all_demo_data(
    target_dir: Optional[Union[str, Path]] = None, force_write: bool = True
) -> Dict[str, Any]:
    """
    Generate all demo data artifacts on disk inside demo_data/ folder.

    Creates:
    - demo_data/historical_projects.csv
    - demo_data/scenarios.json
    - demo_data/<scenario_id>_sow.md
    - demo_data/<scenario_id>_git.log
    - demo_data/<scenario_id>_chat.txt

    Returns a summary dictionary of generated paths and memory references.
    """
    if target_dir is None:
        target_dir = Path(__file__).resolve().parent / "demo_data"
    else:
        target_dir = Path(target_dir)

    target_dir.mkdir(parents=True, exist_ok=True)

    # 1. Write historical_projects.csv
    csv_path = target_dir / "historical_projects.csv"
    if force_write or not csv_path.exists():
        csv_content = get_historical_projects_csv()
        csv_path.write_text(csv_content, encoding="utf-8")

    # 2. Write scenarios.json and scenario individual text files
    scenarios_json_path = target_dir / "scenarios.json"
    if force_write or not scenarios_json_path.exists():
        scenarios_json_path.write_text(
            json.dumps(SCENARIOS, indent=2), encoding="utf-8"
        )

    saved_scenario_files: Dict[str, Dict[str, Path]] = {}
    for scenario_id, scenario in SCENARIOS.items():
        sow_path = target_dir / f"{scenario_id}_sow.md"
        git_path = target_dir / f"{scenario_id}_git.log"
        chat_path = target_dir / f"{scenario_id}_chat.txt"

        if force_write or not sow_path.exists():
            sow_path.write_text(scenario["sow_markdown"].strip() + "\n", encoding="utf-8")
        if force_write or not git_path.exists():
            git_path.write_text(scenario["git_commit_log"].strip() + "\n", encoding="utf-8")
        if force_write or not chat_path.exists():
            chat_path.write_text(scenario["chat_transcript"].strip() + "\n", encoding="utf-8")

        saved_scenario_files[scenario_id] = {
            "sow": sow_path,
            "git": git_path,
            "chat": chat_path,
        }

    return {
        "status": "success",
        "target_dir": str(target_dir),
        "historical_csv_path": str(csv_path),
        "scenarios_json_path": str(scenarios_json_path),
        "scenario_files": {
            k: {sk: str(sp) for sk, sp in sv.items()}
            for k, sv in saved_scenario_files.items()
        },
        "row_count": len(HISTORICAL_PROJECTS_DATA),
        "scenario_count": len(SCENARIOS),
    }


if __name__ == "__main__":
    print("=" * 60)
    print("ScopeGuard: Generating Local Demo Datasets & Audit Scenarios")
    print("=" * 60)

    # Execute deterministic artifact generation
    summary = generate_all_demo_data()

    print(f"[OK] Generated {summary['row_count']} historical projects in CSV format:")
    print(f"     Path: {summary['historical_csv_path']}")
    print(f"[OK] Generated {summary['scenario_count']} pre-built audit scenarios:")
    print(f"     JSON Catalog: {summary['scenarios_json_path']}")
    for sc_id, files in summary["scenario_files"].items():
        print(f"     - Scenario '{sc_id}':")
        for ftype, fpath in files.items():
            print(f"       * {ftype.upper()}: {fpath}")

    # Self-validation checks
    csv_text = get_historical_projects_csv()
    lines = csv_text.strip().split("\n")
    header = lines[0]
    data_rows = lines[1:]

    assert len(data_rows) == 36, f"Expected 36 data rows, found {len(data_rows)}"
    expected_header = "agreed_hours,unplanned_commits,chat_requests,revision_rounds,client_retainer_type,overrun_or_dispute"
    assert header == expected_header, f"Header mismatch: {header} vs {expected_header}"

    for scenario_key in ["low_risk", "moderate_gray_area", "severe_scope_creep"]:
        sc = get_audit_scenario(scenario_key)
        assert "sow_markdown" in sc and len(sc["sow_markdown"]) > 100
        assert "git_commit_log" in sc and "commit " in sc["git_commit_log"]
        assert "chat_transcript" in sc and len(sc["chat_transcript"]) > 50
        assert "agreed_hours" in sc["tabular_inputs"]

    print("\n[SUCCESS] Self-validation passed: 36 rows, balanced targets, 3 complete scenarios.")
