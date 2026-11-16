"""Isotherm for the p-v plot and isobar for the T-v plot."""


def isotherm_pv(table, T1):
    """Return v and P arrays for the isotherm at temperature T1 (p-v diagram).

    Inside the dome it is a horizontal line at Psat(T1) from vf to vg.
    """
    # TODO: liquid part (left of the dome)
    # TODO: horizontal part inside the dome
    # TODO: vapor part (right of the dome)
    raise NotImplementedError


def isobar_tv(table, P1):
    """Return v and T arrays for the isobar at pressure P1 (T-v diagram).

    Inside the dome it is a horizontal line at Tsat(P1) from vf to vg.
    """
    # TODO: liquid part, horizontal part, vapor part
    raise NotImplementedError
