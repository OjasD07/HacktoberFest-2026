# Statement of Work (SOW): IndieSpark Creator Download Catalog

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
