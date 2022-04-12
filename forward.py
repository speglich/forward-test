from functools import reduce
import sys

import numpy as np

from examples.seismic.acoustic.acoustic_example import acoustic_setup

from devito import configuration
configuration["language"] = "openmp"

def test_forward_with_breaks(shape, block_size):
    """ Test running forward in one go and "with breaks"
    and ensure they produce the same result
    """
    spacing = tuple([15.0 for _ in shape])
    tn = 10000.

    solver = acoustic_setup(shape=shape, spacing=spacing, tn=tn,
                            space_order=4, kernel='OT2')

    rec1, u1, summary = solver.forward(save=True, block_size=block_size)
    #rec1, u1, summary = solver.forward(save=False, block_size=block_size)

if __name__ == "__main__":
    shape = (500, 500, 500)
    block_size = int(sys.argv[1])
    print("Running With %d" % block_size)
    test_forward_with_breaks(shape, block_size)
