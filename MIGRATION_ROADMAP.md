# Migration Roadmap (GNU Radio 3.7 -> modern)

## Goals

- Preserve legacy behavior in-place where possible.
- Add modernized equivalents in parallel when migration risk is high.
- Keep each migration change testable without SDR hardware first.

## Priority order

1. `basictest` (smallest graph)  
2. `802_11_ah_rx` (receive chain)  
3. `802_11_ah_tx` (transmit chain)  
4. `802_11_ah_txrx` (full transceiver integration)

## Expected compatibility issues

- Python 2 generated code (`print` statements, `xrange`, old shebangs)
- PyQt4 and wxgui usage
- GRC block parameter/schema differences between 3.7 and current
- OOT module API drift (`gr-ieee802-11`, `gr-foo`, `correctiq`)
- UHD and timing behavior differences across versions

## Validation checklist per graph

1. Open and save in modern GRC (do not run yet).
2. Resolve block-parameter or missing-block warnings.
3. Regenerate Python code and ensure script starts.
4. Run non-hardware smoke checks.
5. Run hardware-in-loop test with known-good USRP setup.
6. Record deltas in `CHANGELOG.md`.

## Step 9 implemented here

Because full migration is risky in one pass, this repo now includes a parallel modern reference file:
- `modern/basictest_py3_reference.py`

This file is intentionally isolated from legacy flowgraphs and provides a Python 3 starter top block for incremental modernization experiments.
