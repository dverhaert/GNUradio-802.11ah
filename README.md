# GNUradio-802.11ah

This repository contains an IEEE 802.11ah transceiver prototype in GNU Radio.

## Project status and scope

- Status: legacy research prototype, now being modernized incrementally.
- Scope: PHY-focused transceiver experimentation.
- Not included: full production-grade MAC implementation and production hardening.
- Tested hardware in original work: Ettus USRP N210.

## Compatibility matrix

| Component | Legacy path (known) | Modern path (target) |
|---|---|---|
| GNU Radio | 3.7.x flowgraphs in this repo | Current GNU Radio release, migrated step-by-step |
| Python | Python 2 generated scripts | Python 3 |
| GUI | PyQt4 and wxgui generated code | Modern Qt stack (after migration) |
| UHD | UHD/USRP required for over-the-air runs | UHD/USRP required for over-the-air runs |
| External OOT blocks | gr-ieee802-11, gr-foo, correctiq, wifi_phy_hier | Same dependencies, pinned to compatible modern versions |

## Background references

- [Description of IEEE 802.11ah standard](https://arxiv.org/pdf/1402.4675.pdf)
- [Implementation of IEEE 802.11a/g/p receiver in gnuradio](http://conferences.sigcomm.org/sigcomm/2013/papers/srif/p9.pdf)
- [First steps in creating an IEEE 802.11ah transceiver](https://www.colorado.edu/itp/sites/default/files/attached-files/70130-130943_-_jaimin_shah_-_apr_25_2016_1005_pm_-_final_capstone_paper_resubmission_team_1.pdf)

## Quick start

### 1) Smoke test (no SDR hardware)

Use this to run non-hardware repository checks (safe for CI and local machines without GNU Radio/UHD):

```bash
python scripts/smoke_check.py
```

Notes:
- This check validates GRC XML integrity and expected legacy markers.
- It intentionally does not require SDR hardware.

### 2) Open the main flowgraph

Open `802_11_ah_txrx.grc` in GNU Radio Companion and inspect configured device/frequency settings before running.

### 3) SDR run path

For over-the-air tests, ensure:
- UHD and USRP networking are working.
- Required OOT modules are installed and discoverable.
- Device address, center frequency, sample rate, and gains match your hardware setup.

Environment variable overrides are available in legacy scripts to avoid hardcoded edits:

- `transceiver_802_11_ah.py`
	- `GR80211AH_USRP_ADDR`
	- `GR80211AH_CENTER_FREQ`
	- `GR80211AH_SAMP_RATE`
	- `GR80211AH_RX_GAIN`
	- `GR80211AH_TX_GAIN`
- `top_block.py`
	- `GR80211AH_TOPBLOCK_USRP_ADDR`
	- `GR80211AH_TOPBLOCK_CENTER_FREQ`
	- `GR80211AH_TOPBLOCK_SAMP_RATE`
	- `GR80211AH_TOPBLOCK_RX_GAIN`

## Modern install path (recommended for 2026)

Use your distro package manager or a maintained environment manager for GNU Radio and UHD.

On Ubuntu-like systems:

```bash
sudo apt update
sudo apt install gnuradio uhd-host
uhd_find_devices
gnuradio-companion
```

Then install and build required OOT dependencies (gr-ieee802-11, gr-foo, and any additional modules this flowgraph imports) using the dependency instructions from each upstream project.

## Legacy reproduction notes

If you need historical behavior close to the original environment:

- Use GNU Radio 3.7.x and Python 2.
- Follow legacy gr-ieee802-11 and gr-foo build guidance for matching branches.
- PyBOMBS instructions in older guides may still work in controlled legacy environments, but are not the recommended primary path for new setups.

## External dependencies

This repository depends on external blocks and modules that are not bundled here:

- [gr-ieee802-11](https://github.com/bastibl/gr-ieee802-11)
- [gr-foo](https://github.com/bastibl/gr-foo)
- `correctiq`
- `wifi_phy_hier` (generated hierarchical block required by transceiver flowgraphs)

## Troubleshooting

1. Verify GNU Radio, UHD, and Python runtime versions match the flowgraph/code generation era.
2. Confirm OOT modules are installed and importable.
3. Check USRP connectivity with `uhd_find_devices`.
4. Validate local device address, sample rate, center frequency, gain, and antenna settings.

If issues persist, check upstream repositories first, especially gr-ieee802-11 and gr-foo.

## Notes on VMs

GNU Radio plus high-throughput SDR networking can be difficult in virtual machines due to NIC and timing constraints. Native Linux is generally more reliable for over-the-air experiments.

## License

This repository is licensed under the terms in `LICENSE`.
