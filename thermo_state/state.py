"""Work out the state of water at the user's pressure p1 and temperature T1."""

COMPRESSED = "COMPRESSED LIQUID"
SATURATED = "SAT. LIQUID-VAPOR"
SUPERHEATED = "SUPERHEATED VAPOR"


def find_state(table, P1, T1):
    """Return the state of water at (P1, T1) as one of the names above.

    Compare T1 with Tsat(P1):
        T1 < Tsat  ->  compressed liquid
        T1 = Tsat  ->  saturated liquid-vapor   (use a small tolerance)
        T1 > Tsat  ->  superheated vapor
    """
    # TODO: handle inputs above the critical point (no Tsat exists there)
    # TODO: handle inputs outside the range of the tables
    raise NotImplementedError


def specific_volume(table, P1, T1):
    """Specific volume v used to place the point (P1, T1) on the plots."""
    # TODO: decide what v to use in each region.
    #   - inside the dome p and T do not fix v (anywhere between vf and vg)
    #   - outside the dome the saturated tables alone do not give v
    raise NotImplementedError
