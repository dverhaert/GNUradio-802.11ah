# Contributing

Thanks for contributing to GNUradio-802.11ah.

## Project reality

This is a legacy GNU Radio 3.7-era repository being modernized in safe increments. Please prioritize small, reviewable changes.

## Environment and dependencies

Required for over-the-air testing:
- GNU Radio + UHD
- Compatible USRP device and networking setup
- External OOT modules used by this repo:
  - gr-ieee802-11
  - gr-foo
  - correctiq
  - wifi_phy_hier

Recommended for contributors:
- Linux host for SDR experiments
- Python 3 for scripts and CI checks (legacy generated scripts are Python 2-style)

## Local checks before opening a PR

Run non-hardware smoke checks:

```bash
python scripts/smoke_check.py
```

Optional legacy syntax check (expected to fail under Python 3 until migration is complete):

```bash
python -m py_compile basictest.py top_block.py transceiver_802_11_ah.py
```

## Issue reporting checklist

When filing issues, include:
- OS and version
- GNU Radio version
- UHD version
- SDR model and connection type
- Which flowgraph/script was run
- Exact runtime command and logs
- Device address, center frequency, sample rate, gain, antenna settings used

## Pull request guidance

- Keep changes scoped to one migration step.
- Do not rewrite legacy files unless needed for the step.
- Keep original behavior as default when parameterizing values.
- Prefer adding parallel modernized files over risky in-place rewrites.
- Update README and CHANGELOG when behavior changes.
