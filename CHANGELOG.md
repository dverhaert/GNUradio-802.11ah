# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- Modernized README with status, compatibility matrix, modern install guidance, legacy notes, and quick-start paths.
- CONTRIBUTING guide with environment, check, and issue-reporting expectations.
- Repository .gitignore tuned for GNU Radio, Python, and editor artifacts.
- Non-hardware smoke check script (`scripts/smoke_check.py`).
- GitHub Actions CI workflow for fast non-hardware validation.
- Migration roadmap document and release-readiness summary.
- Parallel modern reference script (`modern/basictest_py3_reference.py`) for stepwise migration.

### Changed
- Parameterized legacy hardware defaults in:
  - `transceiver_802_11_ah.py`
  - `top_block.py`

### Migration notes
- Legacy generated scripts remain Python 2-style for compatibility with original flowgraphs.
- Modernization follows a parallel-file strategy where full in-place migration is high risk.
