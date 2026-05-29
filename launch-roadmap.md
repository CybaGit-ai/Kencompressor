# Kencompressor (Fraser Valley Agent Intel) — Launch Roadmap

> **⚠️ READ THIS FIRST.** Every AI session working on this project must inspect this file before starting work.

---

## Current State

| Component | Status |
|-----------|--------|
| Backend (FastAPI + SQLite) | ✅ Running |
| Frontend (React + Vite + TS) | ✅ Running |
| Agent portal | ✅ Stub |
| Listings table | ✅ Stub |
| Property intelligence view | ✅ Stub |
| AI outputs (webLLM mocks) | ✅ Deterministic mocks |
| Data sources (ParcelMapBC, ALR, etc.) | ❌ All stubbed |
| Real GIS / municipal data | ❌ Not connected |
| Production deployment | ❌ Not done |
| Authentication | ❌ Not implemented |

---

## P0 — Launch Blockers

### 1. Real Data Integrations
- **Status:** ❌ All stubbed
- **What:** Replace mock data with real API connections
- **Deliverables:**
  - ParcelMapBC API integration (property data)
  - ALR (Agricultural Land Reserve) layer
  - BC hazard layers (fire, flood, earthquake)
  - Municipal GIS data
  - OSM / TransLink transit data
  - StatCan demographics
  - BC Stats housing data
  - FVRD (Fraser Valley Regional District) data
  - Weather data (ECCC)
  - Crime/health statistics
  - Imagery integration

### 2. Production Deployment
- **Status:** ❌ Local only
- **What:** Deploy to production
- **Deliverables:**
  - Backend on production host
  - Frontend on static host
  - Postgres database (replace SQLite)
  - Environment config
  - Health checks + monitoring

### 3. Authentication
- **Status:** ❌ None
- **What:** Protect agent portal
- **Deliverables:**
  - Agent login (email/password or SSO)
  - Role-based access (agent vs admin)
  - Session management
  - Password reset flow

---

## P1 — Feature Completion

### Agent Portal
- [ ] Agent profile management
- [ ] Client management
- [ ] Listing assignment workflow
- [ ] Activity log

### Property Intelligence
- [ ] Real AI analysis (replace webLLM mocks with actual LLM)
- [ ] Comparable sales analysis
- [ ] Price prediction model
- [ ] Investment ROI calculator
- [ ] Neighborhood insights

### Charts + Visualizations
- [ ] Real chart data (replace mock specs)
- [ ] Interactive maps
- [ ] Price trend graphs
- [ ] Market heat maps

---

## P2 — Post-Launch

- [ ] **Mobile app** — React Native for agents in the field
- [ ] **Client portal** — Homeowners can view their property intel
- [ ] **Email reports** — Automated weekly market reports
- [ ] **CRM integration** — Sync with Salesforce, HubSpot
- [ ] **White-label** — Rebrand for other real estate companies
- [ ] **API access** — Third-party integrations

---

## Execution Rules

1. **Real data before deployment** — stubbed data is not launchable
2. **One data source at a time** — test each integration independently
3. **Auth before public exposure** — never expose without authentication
4. **Replace webLLM mocks before launch** — deterministic output is not production-ready
5. **BC data compliance** — respect data licensing terms for government sources
