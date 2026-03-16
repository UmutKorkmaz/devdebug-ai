# DevDebug AI

> AI-first debugging platform for finding, explaining, and fixing application issues across code, runtime behavior, APIs, performance, and security.

## Overview

DevDebug AI is focused on **practical, end-to-end software debugging** rather than challenge-specific integrations. It is designed to help teams detect issues early, triage them faster, and ship safer fixes with AI-assisted analysis.

The project direction emphasizes broad issue discovery across the full application lifecycle:

- Static code quality and bug-risk detection
- Runtime error analysis and root-cause hints
- API contract and integration mismatch detection
- Performance bottleneck discovery
- Security and dependency-risk checks
- Actionable remediation suggestions with prioritization

## Product Vision

DevDebug AI aims to become a unified debugging assistant that can:

1. **Ingest context** from source code, logs, traces, test output, and configuration.
2. **Correlate findings** across multiple signals (e.g., stack trace + recent diff + failing endpoint).
3. **Explain root causes** clearly for developers and reviewers.
4. **Recommend fixes** with confidence levels and impact estimates.
5. **Support continuous quality** through CI-friendly checks and repeatable workflows.

## Core Debugging Capabilities

- **Code-level analysis**
  - Detect likely bugs, anti-patterns, and edge-case risks
  - Highlight fragile code paths and missing validation
- **Runtime diagnostics**
  - Cluster recurring exceptions and identify top crash drivers
  - Convert noisy logs into prioritized debug tasks
- **API and integration debugging**
  - Find schema drift, contract mismatch, and timeout/retry flaws
  - Identify cascading failures between services
- **Performance analysis**
  - Surface slow endpoints, heavy queries, and costly loops
  - Suggest targeted optimization opportunities
- **Security-oriented checks**
  - Flag unsafe patterns and high-risk dependency issues
  - Suggest mitigation steps and safer defaults

## Tech Stack (Current Direction)

- **Language:** Python
- **Backend:** FastAPI (planned/active direction)
- **AI Layer:** LLM-assisted analysis workflows
- **Data Inputs:** Source code, logs, traces, test results, and app configuration

## Getting Started

```bash
# Clone the repo
git clone https://github.com/UmutKorkmaz/devdebug-ai.git
cd devdebug-ai

# Install dependencies (as implemented in your local branch)
pip install -r requirements.txt

# Run the application entrypoint (as implemented in your local branch)
python main.py
```

> Note: The repository direction has shifted to a general-purpose debugging assistant. If your branch introduces a new runtime/CLI entrypoint, update this section accordingly.

## Development Priorities

- Strong debugging workflows over demo-only architecture
- Clear issue classification and severity scoring
- Explainable AI outputs with reproducible evidence
- CI/CD integration for continuous issue detection
- Extensible modules for language/framework-specific analyzers

## License

MIT License — see [LICENSE](LICENSE) for details.
