<a href="https://www.ojasdeshpande.in" target="_blank"><img src="https://raw.githubusercontent.com/OjasD07/OjasD07/main/Logo.svg" alt="Logo" style="float: ; width: 88px; height: 88px; background: #ffffff; border-radius: 10px; padding: 8px; margin: 0 0 8px 8px;" /></a>


# HacktoberFest-2026

Welcome to the **Hacktoberfest 2026** repository containing open-source challenges, artificial intelligence systems, and full-stack developer tools.

---

## Repository Projects

### 🛡️ [Open-Source AI Challenge - Week 2: ScopeGuard](./Open-Source%20AI%20Challenge%20-%20Week%202/)

**ScopeGuard** is a local-first, air-gapped Scope Creep & Invoice Overrun Auditor designed for freelance software engineers and micro-agencies.

* **Dual-Model Inference Pipeline**:
  * **Prior Labs' TabPFN**: In-context Bayesian tabular foundation model trained on historical agency delivery metrics to predict invoice budget overrun probabilities in under 10ms.
  * **Google Gemma 3 (via local Ollama)**: Local-first LLM (`gemma3:4b` / `gemma3:12b`) enforcing strict Pydantic JSON schemas to diff Git commits and client chat logs against SOW contracts.
* **Sentry Agent Tracing**: Distributed OpenTelemetry-compatible span tracing (`scopeguard.agent.pipeline`, `tabpfn.overrun_forecast`, `gemma.sow_diff_audit`).
* **Zero-PII Privacy Protection**: Automatic regex redactor for sensitive API keys, tokens, emails, and credentials with SSRF-safe loopback enforcement.
* **Developer Financial Terminal**: Polished dark-slate web UI with live TabPFN metric sliders, itemized recovery ledger, and one-click Change Order markdown drafting.

```
HacktoberFest-2026/
├── Open-Source AI Challenge - Week 2/   # ScopeGuard Auditor implementation
│   ├── demo_data/                       # Historical project CSVs and scenario fixtures
│   ├── generate_demo_data.py            # Deterministic dataset and fixture generator
│   ├── index.html                       # Developer financial terminal UI
│   ├── main.py                          # Dual-model FastAPI server & Sentry tracing
│   ├── render.yaml                      # One-click Render Blueprint deployment
│   ├── requirements.txt                 # Production dependencies
│   └── README.md                        # Detailed project documentation
└── README.md                            # Root workspace guide
```

---

## Author

Ojas Deshpande [contact@ojasdeshpande.in]
