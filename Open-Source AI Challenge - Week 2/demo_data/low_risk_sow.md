# Statement of Work (SOW): Artisan Brew Co. Storefront MVP

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
