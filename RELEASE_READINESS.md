# Release Readiness Summary

## Modernization changes completed

- README modernized with status, compatibility, and quick-start guidance.
- Legacy hardware defaults parameterized in key Python flowgraphs.
- CONTRIBUTING and CHANGELOG added.
- .gitignore added.
- Non-hardware smoke checks added with CI workflow.
- Migration roadmap added.
- Parallel modern reference script added for low-risk migration.

## Remaining known issues / technical debt

- Core flowgraph scripts are still Python 2 generated.
- PyQt4 and wxgui usage remains in legacy files.
- OOT dependency versions are not pinned in-repo yet.
- No automated hardware-in-loop validation.

## Suggested next version tag

- `v0.2.0-modernization-foundation`

## Draft release notes

### Highlights
- Documentation and contribution workflow refreshed for current development.
- Added CI-backed non-hardware validation.
- Started safe migration path with parallel modern reference files.
- Parameterized hardcoded SDR settings while preserving default behavior.

### Upgrade notes
- Legacy scripts remain available and unchanged in role.
- New environment variables can override SDR defaults in selected scripts.

## Next 3 recommended improvements

1. Migrate `basictest` flowgraph fully to modern GNU Radio and Python 3.
2. Add dependency pinning/build docs for gr-ieee802-11, gr-foo, and correctiq.
3. Add one reproducible hardware validation procedure for USRP-based PR checks.
