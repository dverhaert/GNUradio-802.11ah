#!/usr/bin/env python3
"""Modern Python 3 reference scaffold for the legacy basictest flow.

This does not replace the original files. It provides a safe parallel starting
point for GNU Radio 3.10+ style migration experiments.
"""

from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr


class BasicTestModern(gr.top_block):
    def __init__(self, samp_rate: float = 10e6, tone_hz: float = 250e3):
        super(BasicTestModern, self).__init__("Basictest Modern Reference")

        self.samp_rate = samp_rate
        self.tone_hz = tone_hz

        self.src = analog.sig_source_c(self.samp_rate, analog.GR_COS_WAVE, self.tone_hz, 1.0, 0.0)
        self.throttle = blocks.throttle(gr.sizeof_gr_complex, self.samp_rate, True)
        self.sink = blocks.null_sink(gr.sizeof_gr_complex)

        self.connect(self.src, self.throttle, self.sink)


def main() -> None:
    tb = BasicTestModern()
    tb.start()
    tb.stop()
    tb.wait()


if __name__ == "__main__":
    main()
