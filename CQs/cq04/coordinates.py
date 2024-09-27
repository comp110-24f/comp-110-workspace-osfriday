"""get_coords function for CQ04."""

__author__ = "730566893"


def get_coords(xs: str, ys: str) -> None:
    """Print formatted pairs of each char in 2 input strings."""
    idx1: int = 0
    idx2: int = 0
    while idx1 < len(xs):
        idx2 = 0  # have to reset idx2 to 0 to restart the pairing
        while idx2 < len(ys):
            print(
                "(" + xs[idx1] + "," + ys[idx2] + ")"
            )  # want it to be coords, need ()
            idx2 += 1
        idx1 += 1  # dont add one to idx1 until all the pairs of idx=0 are run
